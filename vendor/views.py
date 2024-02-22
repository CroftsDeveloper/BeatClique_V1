from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .forms import SoundKitForm
from soundkit.models import SoundKit
from django.conf import settings
from payments.models import Order, OrderItem
from django.db.models import Prefetch

@login_required
def dashboard(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to view this page.")

    # Retrieve the AWS S3 bucket name from settings
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    soundkits = SoundKit.objects.all()
    # Fetch recent orders
    recent_orders = Order.objects.filter(paid=True).order_by('-created_at')[:10].prefetch_related(
        Prefetch('orderitem_set', queryset=OrderItem.objects.select_related('soundkit'))
    )

    context = {
        'soundkits': soundkits,
        'recent_orders': recent_orders,
        'bucket_name': bucket_name,
    }
    return render(request, 'vendor/dashboard.html', context)

@login_required
def add_soundkit(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to view this page.")
    if request.method == 'POST':
        form = SoundKitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sound kit successfully added.')
            return redirect('vendor_dashboard')
    else:
        form = SoundKitForm()
    return render(request, 'vendor/add_soundkit.html', {'form': form})

@login_required
def edit_soundkit(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to view this page.")
    soundkit = get_object_or_404(SoundKit, pk=pk)
    if request.method == 'POST':
        form = SoundKitForm(request.POST, request.FILES, instance=soundkit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sound kit successfully updated.')
            return redirect('vendor_dashboard')
    else:
        form = SoundKitForm(instance=soundkit)
    return render(request, 'vendor/edit_soundkit.html', {'form': form, 'soundkit': soundkit})

@login_required
def delete_soundkit(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to view this page.")
    soundkit = get_object_or_404(SoundKit, pk=pk)
    if request.method == 'POST':
        soundkit.delete()
        messages.success(request, 'Sound kit successfully deleted.')
        return redirect('vendor_dashboard')
    return render(request, 'vendor/delete_soundkit.html', {'soundkit': soundkit})
