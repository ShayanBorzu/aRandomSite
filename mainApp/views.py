from django.shortcuts import render

# Create your views here.

def indexView(request):
    return render(request, 'mainApp/index.html')

def aboutView(request):
    return render(request, 'mainApp/about.html')

def contactView(request):
    return render(request, 'mainApp/contact.html')