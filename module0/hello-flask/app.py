# Importation de Flask
from flask import Flask, jsonify
from datetime import datetime

# Creation de l'instance de l'application
app = Flask(__name__)


# ─── TP1 : Routes de base ─────────────────────────────────────────────────────

@app.route('/')
def accueil():
    return '<h1>Bonjour depuis Flask !</h1>'


@app.route('/saluer/<nom>')
def saluer(nom):
    return f'<h2>Bonjour, {nom} ! Bienvenue a l\'Universite de Kara.</h2>'


@app.route('/a-propos')
def a_propos():
    return '''
    <h1>A propos</h1>
    <p>Application Flask - Cours Frameworks Python</p>
    <p>Departement de Mathematiques - Universite de Kara</p>
    '''


# ─── Exercice 2 : Routes enrichies ────────────────────────────────────────────

@app.route('/heure')
def heure():
    """Affiche l'heure actuelle du serveur."""
    maintenant = datetime.now().strftime('%H:%M:%S le %d/%m/%Y')
    return f'<h2>Il est actuellement : {maintenant}</h2>'


@app.route('/calculer/<int:a>/<int:b>')
def calculer(a, b):
    """Somme, difference, produit et quotient de deux entiers."""
    quotient = round(a / b, 4) if b != 0 else 'indefini (division par zero)'
    return f'''
    <h2>Calcul sur {a} et {b}</h2>
    <ul>
        <li>Somme      : {a} + {b} = <strong>{a + b}</strong></li>
        <li>Difference : {a} - {b} = <strong>{a - b}</strong></li>
        <li>Produit    : {a} x {b} = <strong>{a * b}</strong></li>
        <li>Quotient   : {a} / {b} = <strong>{quotient}</strong></li>
    </ul>
    '''


@app.route('/json')
def reponse_json():
    """Retourne une reponse au format JSON avec jsonify."""
    donnees = {
        'message': 'Bonjour depuis Flask !',
        'framework': 'Flask',
        'version': '3.0.3',
        'universite': 'Universite de Kara',
        'heure_serveur': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }
    return jsonify(donnees)


# ─── Exercice 2 : Erreur 404 personnalisee ────────────────────────────────────

@app.errorhandler(404)
def page_non_trouvee(erreur):
    return '''
    <h1 style="color:red;">404 - Page introuvable</h1>
    <p>La page que vous cherchez n'existe pas.</p>
    <a href="/">Retourner a l'accueil</a>
    ''', 404


# ─── Point d'entree ───────────────────────────────────────────────────────────

if __name__ == '__main__':
    app.run(debug=True, port=5000)
