from app.db import get_db

def get_products_by_category(categoria_id):
    """
    Recupera tutti i prodotti di una categoria.
    """
    db = get_db()
    query = """
        SELECT id, categoria_id, nome, prezzo
        FROM partite
        WHERE categorie_id = ?
        ORDER BY data DESC
    """
    prodotti = db.execute(query, (categoria_id,)).fetchall()
    return [dict(prodotto) for prodotto in prodotti]


def get_product_by_id(prodotti_id):
    """Recupera un singolo prodotto per ID."""
    db = get_db()
    query = """
        SELECT id, categoria_id, nome, prezzo
        FROM prodotti
        WHERE id = ?
    """
    prodotto = db.execute(query, (prodotti_id,)).fetchone()
    if prodotto:
        return dict(prodotto)
    return None
 
 
def create_prodotto(gioco_id, data, vincitore, punteggio_vincitore):
    """Crea una nuova partita."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO partite (gioco_id, data, vincitore, punteggio_vincitore) VALUES (?, ?, ?, ?)",
        (gioco_id, data, vincitore, punteggio_vincitore),
    )
    db.commit()
    return cursor.lastrowid

