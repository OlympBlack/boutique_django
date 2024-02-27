from django.shortcuts import render
#from django.http import HttpResponse
from .models import Client
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ClientForm

# Create your views here.
@login_required(login_url='connexion')
def list_client(request, pk):
    client = Client.objects.get(id=pk)
    commandes = client.commande_set.all()
    commande_total = commandes.count()
    return render(request, 'client/client.html', {'client': client, 'commandes': commandes, 'commande_total': commande_total})

# la fonction pour supprimer un client
def supprimer_client(request, id):
    if request.method == 'POST':
        elem = Client.objects.get(kp=id)
        elem.delete()
    return redirect('client/client')