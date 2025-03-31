import sqlite3

DB_PATH = "kitchen.db"

def connect_db():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def get_inventory():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT item_name, quantity FROM inventory WHERE quantity > 0;")
    inventory = cursor.fetchall()
    conn.close()
    return inventory

def add_item(item_name, quantity, expiry_date, category):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO inventory (item_name, quantity, expiry_date, category)
        VALUES (?, ?, ?, ?)
    """, (item_name, quantity, expiry_date, category))
    conn.commit()
    conn.close()

def update_item(item_id, item_name, quantity, expiry_date, category):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE inventory
        SET item_name = ?, quantity = ?, expiry_date = ?, category = ?
        WHERE id = ?
    """, (item_name, quantity, expiry_date, category, item_id))
    conn.commit()
    conn.close()

def get_recipe():
    from recipe_ai import get_recipe
    return get_recipe()