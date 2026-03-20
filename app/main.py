from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from app.repositories import categoria_repository, product_repository

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    # 1. Prendiamo le categorie dal database
    categorie = categoria_repository.get_all_categories()

    # 2. Passiamo la variabile 'categorie' al template
    return render_template("index.html", categorie=categorie)


@bp.route("categoria/<id>")
def category_detail(id):
    # 1. Prendiamo la categoria
    categorie = categoria_repository.get_category_by_id(id)
    if categorie is None:
        abort(404, "Categoria non trovata.")

    # 2. Prendiamo i prodotti della categoria
    prodotti = product_repository.get_products_by_category(id)

    # 3. Passiamo al template
    return render_template("categorie_detail.html", categorie=categorie, prodotti=prodotti)


@bp.route("/crea_categoria", methods=("GET", "POST"))
def create_category():
    if request.method == "POST":
        nome = request.form["nome"]
        error = None

        if not nome:
            error = "Il nome è obbligatorio."

        if error is not None:
            flash(error)
        else:
            # Creiamo la categoria
            categoria_repository.create_category(nome)
            return redirect(url_for("main.index"))

    return render_template("create_category.html")


@bp.route("/create_match", methods=("GET", "POST"))
def create_match():
    if request.method == "POST":
        gioco_id = request.form.get("gioco_id", type=int)
        data = request.form["data"]
        vincitore = request.form["vincitore"]
        punteggio_vincitore = request.form.get("punteggio_vincitore", type=int)
        error = None

        if gioco_id is None:
            error = "Seleziona un gioco."
        if not data:
            error = "La data è obbligatoria."
        if not vincitore:
            error = "Il vincitore è obbligatorio."
        if punteggio_vincitore is None or punteggio_vincitore < 0:
            error = "Il punteggio vincitore deve essere un numero non negativo."

        if error is not None:
            flash(error)
        else:
            # Creiamo la partita
            match_repository.create_match(gioco_id, data, vincitore, punteggio_vincitore)
            return redirect(url_for("main.game_detail", id=gioco_id))

    # Per GET, passiamo i giochi per il select
    games = game_repository.get_all_games()
    return render_template("create_match.html", games=games)