from django.urls import path
from . import views

urlpatterns = [
    # Directs to the soundkit listing page
    path('', views.soundkit_list, name='soundkit_list'),
    # Directs to individual soundkit detail pages
    path('<int:pk>/', views.soundkit_detail, name='soundkit_detail'),
]
