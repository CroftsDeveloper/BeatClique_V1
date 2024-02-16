from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<int:soundkit_id>/', views.add_to_cart, name='add_to_cart'),
    path('view/', views.view_cart, name='view_cart'),
    path('update/', views.update_cart, name='update_cart'),
]
