from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .forms import CommandeForm
from .models import Commande
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='connexion')
def list_commande(request):
    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('/')
    else:
        form = CommandeForm()
    commandes = Commande.objects.all()
    context = {'form': form, 'commandes': commandes}
    return render(request, 'commande/commande.html', context)

# la fonction pour supprimer une commande
def supprimer_commande(request, id):
    if request.method == 'POST':
        elem = Commande.objects.get(pk=id)
        elem.delete()
    return redirect('/commande')
