from hashlib import sha256
import sqlite3

admin_pass = 'admin'

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS manager (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

def menu():
    print('******************************')
    print('*   i: insert new password   *')
    print('*   s: show all services     *')
    print('*   r: recover a password    *')
    print('*   q: quit                  *')
    print('******************************')

conn.close()