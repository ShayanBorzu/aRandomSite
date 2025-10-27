from django.shortcuts import render, redirect
from accountsApp.forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def accounts_index_view(request):
    if request.method == 'POST':
        signupform = SignUpForm(request.POST)
        loginform = LoginForm(request.POST)
        if signupform.is_valid():
            signupform.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your account has been created successfully.",
            )
            return redirect('accounts:index')
        elif loginform.is_valid():
            username = loginform.cleaned_data["username"]
            password = loginform.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "You've been logged in successfully.",
                )
                return redirect('main:index')
            else:
                messages.add_message(request, messages.ERROR, "Invalid Credential")
        else:
            messages.add_message(
                request, messages.ERROR, "Error encountered."
            )
    return render(request, 'accountsApp/accounts_index.html')

def accounts_logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.SUCCESS, "Logged out successfully.")
        return redirect("main:index")
    messages.add_message(request, messages.ERROR, "Error encountered.")
    return redirect("main:index")