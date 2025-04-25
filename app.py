from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('shayari.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS shayari (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('shayari.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shayari ORDER BY id DESC")
    shayaris = c.fetchall()
    conn.close()
    return render_template('index.html', shayaris=shayaris)

@app.route('/add', methods=['POST'])
def add_shayari():
    content = request.form['content']
    if content:
        conn = sqlite3.connect('shayari.db')
        c = conn.cursor()
        c.execute("INSERT INTO shayari (content) VALUES (?)", (content,))
        conn.commit()
        conn.close()
    return redirect('/')

@app.route('/delete')
def delete_page():
    conn = sqlite3.connect('shayari.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shayari ORDER BY id DESC")
    shayaris = c.fetchall()
    conn.close()
    return render_template('delete.html', shayaris=shayaris)

@app.route('/delete/<int:shayari_id>', methods=['POST'])
def delete_shayari(shayari_id):
    conn = sqlite3.connect('shayari.db')
    c = conn.cursor()
    c.execute("DELETE FROM shayari WHERE id = ?", (shayari_id,))
    conn.commit()
    conn.close()
    return redirect('/delete')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
