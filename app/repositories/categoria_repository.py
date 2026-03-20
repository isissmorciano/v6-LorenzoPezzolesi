from app.db import get_db

def get_all_categories():
    """
    Recupera tutte le categorie.
    """
    db = get_db()
    query = """
        SELECT id, nome
        FROM categorie
        ORDER BY nome
    """
    categoria = db.execute(query).fetchall()
    return [dict(categorie) for categorie in categoria]

def get_category_by_id(categoria_id):
    """Recupera una singola categoria per ID."""
    db = get_db()
    query = """
        SELECT id, nome
        FROM categorie
        WHERE id = ?
    """
    categorie = db.execute(query, (categoria_id,)).fetchone()
    if categorie:
        return dict(categorie)
    return None


def create_category(nome):
    """Crea una nuova categoria."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO categorie (nome) VALUES (?)", 
        (nome)
    )
    db.commit()
    return cursor.lastrowid

