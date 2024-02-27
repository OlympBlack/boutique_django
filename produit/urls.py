from django.urls import path
from . import views

urlpatterns = [
    path('/index', views.index, name='index'),
    path('/acceuil', views.acceuil, name='acceuil'),
    path('/list_produit', views.list_produit, name='list_produit'),
    path('/<int:id>', views.supprimer_produit, name='supprimer_produit'),
    path('/<str:id>', views.modifier_produit, name='modifier_produit')
]
