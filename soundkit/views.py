from django.shortcuts import render, get_object_or_404
from .models import SoundKit

def soundkit_list(request):
    soundkits = SoundKit.objects.all()
    return render(request, 'soundkit/soundkit_list.html', {'soundkits': soundkits})

def soundkit_detail(request, pk):
    soundkit = get_object_or_404(SoundKit, pk=pk)
    return render(request, 'soundkit/soundkit_detail.html', {'soundkit': soundkit})
