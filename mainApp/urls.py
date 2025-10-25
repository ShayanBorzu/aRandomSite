from django.urls import path
from mainApp.views import indexView, aboutView, contactView

app_name = "main"

urlpatterns = [
    path("", indexView, name="index"),
    path("about/", aboutView, name="about"),
    path("contact/", contactView, name="contact"),    
]
