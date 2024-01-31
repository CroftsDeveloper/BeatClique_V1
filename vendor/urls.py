from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='vendor_dashboard'),  # Root URL of vendor app
    path('dashboard/', views.dashboard, name='vendor_dashboard'),  # URL for dashboard
    path('add_soundkit/', views.add_soundkit, name='add_soundkit'),
    path('edit_soundkit/<int:pk>/', views.edit_soundkit, name='edit_soundkit'),
    path('delete_soundkit/<int:pk>/', views.delete_soundkit, name='delete_soundkit'),
]
