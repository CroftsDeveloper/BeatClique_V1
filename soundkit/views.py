from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Render the home page template

def soundkit_list(request):
    return render(request, 'soundkit/soundkit_list.html')  # Render the sound kit listing page template
