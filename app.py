from flask import Flask, redirect, url_for, request, render_template
import sqlite3
import os

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    
    if request.method == 'POST':
        full_url = request.form.get('full_url')
        hash_range = request.form.get('hash_range')

        if not full_url or not hash_range.isdigit():
            return "Invalid input", 400

        hash_range = int(hash_range)
        if not (5 <= hash_range <= 10):
            return "Hash range out of bounds", 400

        hash_code = os.urandom(hash_range).hex()

        conn.execute("INSERT INTO url_shortener (full_url, hash_code) VALUES (?, ?)", (full_url, hash_code))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    url_shortener = conn.execute('SELECT * FROM url_shortener').fetchall()
    conn.close()

    return render_template('index.html', url_shortener=url_shortener)

@app.route('/<hash_code>')
def redirect_url(hash_code):
    conn = get_db_connection()
    url_shortener = conn.execute(f"SELECT * FROM url_shortener WHERE hash_code='{hash_code}'").fetchone()
    conn.close()
    if url_shortener:
        print(url_shortener['full_url'])
        return redirect(url_shortener['full_url'], code=301)
    else:
        return redirect(url_for('index'))
if __name__ == '__main__':
    app.run()
