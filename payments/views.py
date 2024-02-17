from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe
from cart.models import Cart, CartItem
from .models import Order, OrderItem
from soundkit.models import SoundKit

# Set Stripe's API key
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def create_checkout_session(request):
    try:
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
    except Cart.DoesNotExist:
        # Redirect or show an error if the cart is empty or does not exist
        return render(request, 'payments/empty_cart.html')
    except Exception as e:
        # Handle any other exceptions
        return render(request, 'payments/error.html', {'message': str(e)})

@login_required
def payment_success(request):
    try:
        user_cart = Cart.objects.get(user=request.user)
        # Calculate total cost for the order
        total_cost = sum([item.soundkit.price * item.quantity for item in user_cart.items.all()])
        # Create an order
        order = Order.objects.create(user=request.user, total=total_cost, paid=True)
        for item in user_cart.items.all():
            OrderItem.objects.create(order=order, soundkit=item.soundkit, quantity=item.quantity)
        # Clear user's cart after successful payment
        user_cart.delete()
        # Render the payment success template
        return render(request, 'payments/payment_success.html')
    except Cart.DoesNotExist:
        return render(request, 'payments/error.html', {'message': 'No cart found for user.'})

@login_required
def payment_cancelled(request):
    # Render the payment cancelled template
    return render(request, 'payments/payment_cancelled.html')

@login_required
def order_history(request):
    try:
        # Retrieve payment-related order history for the current user
        orders = Order.objects.filter(user=request.user)
        return render(request, 'payments/order_history.html', {'orders': orders})
    except Order.DoesNotExist:
        # Handle case where no orders are found for the user
        return render(request, 'payments/order_history.html', {'orders': []})
