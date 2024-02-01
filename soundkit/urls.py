from django.urls import path
from . import views

urlpatterns = [
    path('', views.soundkit_list, name='soundkit_list'),
    path('<int:pk>/', views.soundkit_detail, name='soundkit_detail'),
]
