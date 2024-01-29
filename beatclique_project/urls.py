"""
URL configuration for beatclique_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from soundkit import views as soundkit_views  # Import views from soundkit app
from accounts import views as accounts_views  # Import views from accounts app
from django.conf import settings  # Import for static files
from django.conf.urls.static import static  # Import for static files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', soundkit_views.home, name='home'),  # URL for the home page
    path('soundkits/', soundkit_views.soundkit_list, name='soundkit_list'),  # URL for the sound kit listing page
    path('register/', accounts_views.register, name='register'),  # URL for the user registration page
]

# Serving static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
