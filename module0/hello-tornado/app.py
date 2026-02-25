# Tornado utilise la programmation asynchrone
import tornado.ioloop
import tornado.web


# Un Handler est l'equivalent d'une vue/route dans Tornado
class AccueilHandler(tornado.web.RequestHandler):
    """
    RequestHandler est la classe de base pour
    traiter les requetes HTTP dans Tornado.
    """

    def get(self):
        """
        Methode appelee pour les requetes GET.
        self.write() ecrit la reponse.
        """
        self.write("<h1>Bonjour depuis Tornado !</h1>")
        self.write("<p>Framework asynchrone Python</p>")


class SaluerHandler(tornado.web.RequestHandler):
    """Handler avec parametre dans l'URL"""

    def get(self, nom):
        self.set_header("Content-Type", "text/html; charset=utf-8")
        self.write(f"<h2>Bonjour, {nom} ! depuis Tornado</h2>")


def make_app():
    """
    Cree et configure l'application Tornado.
    Chaque tuple (pattern, handler) definit une route.
    """
    return tornado.web.Application([
        (r"/",               AccueilHandler),        # Route vers la page d'accueil
        (r"/saluer/([^/]+)", SaluerHandler),         # Route avec capture de groupe regex
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    # Ecoute sur le port 8888
    app.listen(8888)
    print("Serveur Tornado demarre sur http://localhost:8888")
    # Demarre la boucle d'evenements (IOLoop) - coeur de Tornado
    tornado.ioloop.IOLoop.current().start()
