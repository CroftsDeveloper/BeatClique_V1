from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from soundkit.models import SoundKit
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

@login_required
def add_to_cart(request, soundkit_id):
    soundkit = get_object_or_404(SoundKit, id=soundkit_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, 
        soundkit=soundkit,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.info(request, f"Quantity updated for {soundkit.name}.")
    else:
        messages.success(request, f"{soundkit.name} added to your cart.")
    return redirect('cart:view_cart')

@login_required
def view_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        items = cart.items.all()
    except Cart.DoesNotExist:
        cart = None
        items = []
        # Display an error message for empty cart
        messages.error(request, "Your cart is empty.")
    return render(request, 'cart/view_cart.html', {'cart': cart, 'items': items})

@login_required
def update_cart(request):
    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)
        for key, value in request.POST.items():
            if key.startswith('quantity_'):
                item_id = key.split('_')[1]
                try:
                    cart_item = CartItem.objects.get(id=item_id, cart=cart)
                except CartItem.DoesNotExist:
                    # Handle case where the requested item does not exist in the cart
                    messages.error(request, "Item not found in your cart.")
                    return redirect('cart:view_cart')
                if 'update' in request.POST and request.POST['update'] == item_id:
                    cart_item.quantity = int(value)
                    cart_item.save()
                    messages.success(request, f"Quantity updated for {cart_item.soundkit.name}.")
                elif 'remove' in request.POST and request.POST['remove'] == item_id:
                    cart_item.delete()
                    messages.warning(request, f"{cart_item.soundkit.name} removed from your cart.")
        return HttpResponseRedirect(reverse('cart:view_cart'))
