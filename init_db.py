import os
import sqlite3

DATABASE_PATH = os.environ.get('DATABASE_PATH', 'database.db')


def init_database(database_path=DATABASE_PATH):
    """Create the SQLite database and posts table if they do not exist."""
    database_folder = os.path.dirname(database_path)
    if database_folder:
        os.makedirs(database_folder, exist_ok=True)

    connection = sqlite3.connect(database_path)
    with connection:
        connection.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            );
        ''')
    connection.close()


if __name__ == '__main__':
    init_database()
    print(f'Base de datos lista en: {DATABASE_PATH}')
