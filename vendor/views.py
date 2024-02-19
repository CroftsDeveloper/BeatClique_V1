from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages 
from .forms import SoundKitForm
from soundkit.models import SoundKit
from django.conf import settings 

@login_required
def dashboard(request):
    # Retrieve the AWS S3 bucket name from settings
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to view this page.")
    soundkits = SoundKit.objects.all()
    return render(request, 'vendor/dashboard.html', {'soundkits': soundkits, 'bucket_name': bucket_name})

@login_required
def add_soundkit(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to view this page.")
    if request.method == 'POST':
        form = SoundKitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sound kit successfully added.')  # Success message
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
            messages.success(request, 'Sound kit successfully updated.')  # success message for update
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
        messages.success(request, 'Sound kit successfully deleted.')  # Success message for deletion
        return redirect('vendor_dashboard')
    return render(request, 'vendor/delete_soundkit.html', {'soundkit': soundkit})
