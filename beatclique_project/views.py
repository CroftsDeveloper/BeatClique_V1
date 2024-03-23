from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseServerError

def home(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('vendor_dashboard')
    return render(request, 'home.html')

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)
