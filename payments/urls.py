from django.urls import path
from . import views

urlpatterns = [
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancelled, name='payment_cancelled'),
    path('order-history/', views.order_history, name='order_history'),
    # URL pattern for downloading product files
    path('download/<int:order_item_id>/', views.download_product_file, name='download_product_file'),
]
