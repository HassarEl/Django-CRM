from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpFrom
from .models import Record


def home(request):
    records = Record.objects.all()

    #check to see if loging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Loggin In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out...')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpFrom(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, " You Have Successfully Register")
            return redirect('home')
    else:
        form = SignUpFrom()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

def produit(request):
    return render (request, 'produits/produit.html')

def affectation(request):
    return render(request, 'produits/prod_categorie.html')

def categorie(request):
    return render(request, 'categories/categorie.html')

def add_ctgr(request):
    return render(request, 'categories/create_ctgr.html')

def commande(request):
    return render(request, 'commandes/commande.html')

def stock(request):
    return render(request, 'stock/stock.html')