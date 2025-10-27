from django.shortcuts import render

# Create your views here.
def accounts_index_view(request):
    return render(request, "accountsApp/accounts_index.html")