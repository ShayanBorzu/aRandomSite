from django.urls import path
from mainApp.views import helloworld_view

urlpatterns = [
    path("", helloworld_view, name="helloworld"),
]
