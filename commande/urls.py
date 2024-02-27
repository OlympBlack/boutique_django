from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_commande, name='commande'),
    path('/<int:id>', views.supprimer_commande, name='supprimer_commande')

]
