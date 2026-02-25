# Ce fichier n'existe pas par defaut, il faut le creer
from django.urls import path
from . import views   # Importer les vues du meme dossier

# Liste des URLs de l'application "accueil"
urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('saluer/<str:nom>/', views.saluer, name='saluer'),
]
