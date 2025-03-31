import sqlite3

def create_database():
    conn = sqlite3.connect("kitchen.db")
    cursor = conn.cursor()

    # Create the inventory table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            expiry_date TEXT,
            category TEXT,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Insert default items
    default_items = [
        ("tomato", 10, "2025-04-30", "vegetable"),
        ("onion", 5, "2025-04-25", "vegetable"),
        ("chicken", 3, "2025-04-20", "meat"),
        ("potato", 8, "2025-05-01", "vegetable"),
        ("carrot", 7, "2025-04-28", "vegetable"),
    ]

    # Check if the table is empty before inserting default items
    cursor.execute("SELECT COUNT(*) FROM inventory")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO inventory (item_name, quantity, expiry_date, category) VALUES (?, ?, ?, ?)", default_items)
        print("Default items inserted into the database.")
    else:
        print("Database already contains items. No default items inserted.")

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("✅ Database setup completed.")