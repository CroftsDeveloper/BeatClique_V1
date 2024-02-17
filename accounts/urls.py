from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    # Login URL
    path('login/', views.user_login, name='login'),

    # Registration URL
    path('register/', views.register, name='register'),

    # Account URL
    path('account/', views.account_view, name='account'),

    # Logout URL
    path('logout/', views.logout_view, name='logout'),  # Updated view function name

    # Account Update URL
    path('account/update/', views.account_update, name='account_update'),

]
