from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe
from cart.models import Cart, CartItem
from .models import Order, OrderItem
from soundkit.models import SoundKit
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse, Http404
from django.core.files.base import ContentFile
import os
import boto3
from botocore.exceptions import NoCredentialsError



# Set Stripe's API key
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def create_checkout_session(request):
    # Retrieve the current user's cart
    cart = Cart.objects.get(user=request.user)
    line_items = []

    # Create a line item for each soundkit in the cart
    for item in cart.items.all():
        line_item = {
            'price_data': {
                'currency': 'gbp',
                'product_data': {
                    'name': item.soundkit.name,
                },
                'unit_amount': int(item.soundkit.price * 100),  # Price in pence
            },
            'quantity': item.quantity,
        }
        line_items.append(line_item)

    # Create Stripe Checkout Session
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri('/') + 'payments/success/',
        cancel_url=request.build_absolute_uri('/') + 'payments/cancel/',
    )

    # Redirect to Stripe Checkout
    return redirect(checkout_session.url, code=303)

@login_required
def payment_success(request):
    # Retrieve the current user's cart
    user_cart = Cart.objects.get(user=request.user)
    # Calculate total cost for the order
    total_cost = sum([item.soundkit.price * item.quantity for item in user_cart.items.all()])
    # Create an order
    order = Order.objects.create(user=request.user, total=total_cost, paid=True)
    for item in user_cart.items.all():
        OrderItem.objects.create(order=order, soundkit=item.soundkit, quantity=item.quantity)
    # Clear user's cart after successful payment
    user_cart.delete()

    # Prepare email content
    context = {
        'username': request.user.username,
        'order_id': order.id,
        'total_amount': total_cost,
    }
    email_html_message = render_to_string('payments/emails/purchase_confirmation.html', context)
    subject = 'Your BeatClique Purchase Confirmation'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email, ]

    # Send email
    send_mail(subject, "", email_from, recipient_list, html_message=email_html_message)

    # Render the payment success template
    return render(request, 'payments/payment_success.html')

@login_required
def payment_cancelled(request):
    # Render the payment cancelled template
    return render(request, 'payments/payment_cancelled.html')

@login_required
def order_history(request):
    # Retrieve payment-related order history for the current user
    orders = Order.objects.filter(user=request.user)
    return render(request, 'payments/order_history.html', {'orders': orders})

@login_required
def download_product_file(request, order_item_id):
    """
    Redirects the user to the AWS S3 URL to securely download the product file
    if they have purchased it.
    """
    # Retrieve the specific order item to ensure the user has purchased it
    order_item = get_object_or_404(OrderItem, id=order_item_id, order__user=request.user)
    
    # Ensure there's a file associated with the sound kit
    if not order_item.soundkit.zip_file:
        return HttpResponse("No file available for download.", status=404)
    
    # Generate the S3 URL
    s3_client = boto3.client('s3',
                             aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                             region_name=settings.AWS_S3_REGION_NAME)

    try:
        file_url = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                                                            'Key': str(order_item.soundkit.zip_file)})
    except NoCredentialsError:
        return HttpResponse("Could not generate the download link.", status=500)

    return redirect(file_url)
