from django.shortcuts import render

# Create your views here.
def helloworld_view(request):
    return render(request, 'mainApp/helloworld.html')