from django.shortcuts import render, redirect
from mainApp.forms import ContactForm
from django.contrib import messages

# Create your views here.


def indexView(request):
    return render(request, "mainApp/index.html")


def aboutView(request):
    return render(request, "mainApp/about.html")


def contactView(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Thank you for contacting us. We'll get back to you within 24 hours.",
            )
            return redirect('main:contact')
        else:
            messages.add_message(
                request, messages.ERROR, "Error encountered. empty cache and try again."
            )
    return render(request, "mainApp/contact.html", {"form": form})
