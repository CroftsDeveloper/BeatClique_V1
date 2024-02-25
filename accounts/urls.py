from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

app_name = 'accounts'

urlpatterns = [
    # Login URL
    path('login/', views.user_login, name='login'),

    # Registration URL
    path('register/', views.register, name='register'),
    path('verify-email/<uidb64>/<token>/', views.verify_email, name='verify_email'),  # URL for email verification

    # Account URL
    path('account/', views.account_view, name='account'),  # Account details view

    # Logout URL
    path('logout/', views.logout_view, name='logout'),
]

