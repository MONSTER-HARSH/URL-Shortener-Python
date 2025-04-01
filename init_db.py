import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())


cur = connection.cursor()

cur.execute("INSERT INTO url_shortener (full_url, hash_code) VALUES (?, ?)",
            ('https://www.youtube.com/@lowlyminions', 'a1b2c3d4e5')
            )

connection.commit()
connection.close()