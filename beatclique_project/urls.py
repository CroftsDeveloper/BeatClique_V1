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

from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views as project_views
from django.contrib import admin

# Define URL patterns
urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # Home URL
    path('', project_views.home, name='home'),

    # Soundkits URL
    path('soundkits/', include('soundkit.urls')),  # Include URLs for soundkits app

    # Accounts URL with namespace
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),  # Include URLs for accounts app

    # Vendor URL
    path('vendor/', include('vendor.urls')),  # Include URLs for vendor app

    # Payments URL
    path('payments/', include('payments.urls')),  # Include URLs for payments app

    # Cart URL with namespace
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),  # Include URLs for cart app
]

handler404 = 'beatclique_project.views.handler404'  # Custom view for 404 error
handler500 = 'beatclique_project.views.handler500'  # Custom view for 500 error

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

