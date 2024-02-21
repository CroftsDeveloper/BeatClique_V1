from django.urls import path
from . import views

urlpatterns = [
    # URL pattern to add a sound kit to the cart
    path('add-to-cart/<int:soundkit_id>/', views.add_to_cart, name='add_to_cart'),
    
    # URL pattern to view the contents of the cart
    path('view/', views.view_cart, name='view_cart'),
    
    # URL pattern to update the cart contents
    path('update/', views.update_cart, name='update_cart'),
]
