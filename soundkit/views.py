from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def soundkit_list(request):
    return render(request, 'soundkit/soundkit_list.html')
