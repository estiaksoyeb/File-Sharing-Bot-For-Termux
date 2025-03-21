import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('bot_database.db')
cursor = conn.cursor()

# Create a table for users if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY
)
''')
conn.commit()

async def present_user(user_id: int):
    """
    Check if a user exists in the database.
    """
    cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,))
    return cursor.fetchone() is not None

async def add_user(user_id: int):
    """
    Add a user to the database.
    """
    cursor.execute('INSERT OR IGNORE INTO users (user_id) VALUES (?)', (user_id,))
    conn.commit()

async def full_userbase():
    """
    Retrieve all user IDs from the database.
    """
    cursor.execute('SELECT user_id FROM users')
    return [row[0] for row in cursor.fetchall()]

async def del_user(user_id: int):
    """
    Delete a user from the database.
    """
    cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
    conn.commit()