from django.http import HttpResponse


def accueil(request):
    """
    Vue Django simple.
    'request' contient toutes les informations de la requete HTTP.
    On retourne un objet HttpResponse avec le contenu HTML.
    """
    return HttpResponse("<h1>Bonjour depuis Django !</h1>")


def saluer(request, nom):
    """
    Vue avec parametre capture depuis l'URL.
    """
    return HttpResponse(f"<h2>Bonjour, {nom} ! depuis Django</h2>")
