from django.urls import path, reverse_lazy
from accountsApp.views import accounts_index_view, accounts_logout_view, ResetPasswordView
from django.contrib.auth import views as auth_views
app_name = "accounts"

urlpatterns = [
    path("", accounts_index_view, name="index"),
    path("logout/", accounts_logout_view, name="logout"),
    path(
        "password-reset/",
        ResetPasswordView.as_view(),
        name="password_reset"
    ),

    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accountsApp/password_reset_done.html"
        ),
        name="password_reset_done"
    ),

    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accountsApp/password_reset_confirm.html",
            success_url = reverse_lazy("accounts:password_reset_complete")
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accountsApp/password_reset_complete.html"
        ),
        name="password_reset_complete"
    ),
]
