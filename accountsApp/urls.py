from django.urls import path
from accountsApp.views import accounts_index_view, accounts_logout_view

app_name = "accounts"

urlpatterns = [
    path("", accounts_index_view, name="index"),
    path("logout/", accounts_logout_view, name="logout"),

]
