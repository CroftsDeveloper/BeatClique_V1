from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('vendor_dashboard')
    return render(request, 'home.html')
