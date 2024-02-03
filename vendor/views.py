# vendor/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import SoundKitForm
from soundkit.models import SoundKit

@login_required
def dashboard(request):
    # TODO: implement a group-based access control for vendor functionalities
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to view this page.")
    soundkits = SoundKit.objects.all()
    return render(request, 'vendor/dashboard.html', {'soundkits': soundkits})

@login_required
def add_soundkit(request):
    # TODO: Review if additional user roles need access to this functionality
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to view this page.")
    if request.method == 'POST':
        form = SoundKitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vendor_dashboard')
    else:
        form = SoundKitForm()
    return render(request, 'vendor/add_soundkit.html', {'form': form})

@login_required
def edit_soundkit(request, pk):
    # TODO: Ensure that only authorized users can edit sound kits
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to view this page.")
    soundkit = get_object_or_404(SoundKit, pk=pk)
    if request.method == 'POST':
        form = SoundKitForm(request.POST, request.FILES, instance=soundkit)
        if form.is_valid():
            form.save()
            return redirect('vendor_dashboard')
    else:
        form = SoundKitForm(instance=soundkit)
    return render(request, 'vendor/edit_soundkit.html', {'form': form, 'soundkit': soundkit})

@login_required
def delete_soundkit(request, pk):
    # TODO: Add confirmation dialogue before deletion to improve UX
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to view this page.")
    soundkit = get_object_or_404(SoundKit, pk=pk)
    if request.method == 'POST':
        soundkit.delete()
        return redirect('vendor_dashboard')
    return render(request, 'vendor/delete_soundkit.html', {'soundkit': soundkit})
