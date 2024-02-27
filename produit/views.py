from django.shortcuts import render, HttpResponseRedirect, redirect
#from django.http import HttpResponse
from client.models import Client
from commande.models import Commande 
from .models import Produit
from django.contrib.auth.decorators import login_required
from .forms import ProduitForm
from client.forms import ClientForm

# Create your views here.
@login_required(login_url='connexion')
def index(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('/')
    else:
        form = ClientForm()
    clients = Client.objects.all()
    #commandes = Commande.objects.all() 
    return render(request, 'produit/index.html', {'clients': clients, 'form': form})

# la fonction qui renvoit la page d'acceuil
def acceuil(request):
    clients = Client.objects.all()
    commandes = Commande.objects.all()
    produits = Produit.objects.all()
    commande_total = commandes.count()
    client_total = clients.count()  
    produit_total = produits.count()
    context = {'clients': clients, 'commandes': commandes, 'commande_total': commande_total, 'produit_total': produit_total, 'produit_total': produit_total}
    return render(request, 'produit/acceuil.html', context)   

# la fonction pour lister tous les produits
def list_produit(request):
    # ajouter un produit
    #form = ProduitForm()
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('/produit/list_produit')
    else:
        form = ProduitForm()
    produits = Produit.objects.all()
    context = {'produits': produits, 'form': form}
    return render(request, 'produit/list_produit.html', context)

# la fonction qui supprime un produit par son id
def supprimer_produit(request, id):
    if request.method == 'POST':
        elem = Produit.objects.get(pk=id)
        elem.delete()
    return HttpResponseRedirect('/produit/list_produit')


# la fonction pour modifier un produit 
def modifier_produit(request, id):
    produit = Produit.objects.get(pk=id)
    form = ProduitForm(instance=produit)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            #return redirect('/produit/list_produit')
    produits = Produit.objects.all()
    context = {'produits': produits, 'form': form}
    return render(request, 'produit/list_produit.html', context)


