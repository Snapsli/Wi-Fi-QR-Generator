from flask import Flask, request, render_template, redirect, url_for
import qrcode
import io
import base64
import sqlite3
import os
import threading
import webview

app = Flask(__name__)
DB_FILE = 'history.db'

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS history (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ssid TEXT NOT NULL,
                            qr_base64 TEXT NOT NULL,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )""")

def save_to_db(ssid, qr_base64):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("INSERT INTO history (ssid, qr_base64) VALUES (?, ?)", (ssid, qr_base64))
        conn.commit()

def get_history():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute("SELECT id, ssid, qr_base64, created_at FROM history ORDER BY created_at DESC")
        return cursor.fetchall()

def delete_qr(item_id):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("DELETE FROM history WHERE id = ?", (item_id,))
        conn.commit()

def generate_qr_base64(wifi_string):
    qr = qrcode.make(wifi_string)
    img_io = io.BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)
    return base64.b64encode(img_io.getvalue()).decode()

@app.route('/', methods=['GET', 'POST'])
def index():
    last_qr = None
    if request.method == 'POST':
        ssid = request.form['ssid']
        password = request.form['password']
        wifi_string = f"WIFI:S:{ssid};T:WPA;P:{password};;"
        qr_base64 = generate_qr_base64(wifi_string)
        save_to_db(ssid, qr_base64)
        last_qr = (ssid, qr_base64)

    history = get_history()
    return render_template('form.html', last_qr=last_qr, history=history)

@app.route('/delete/<int:item_id>')
def delete_route(item_id):
    delete_qr(item_id)
    return redirect(url_for('index'))

def start_flask():
    app.run()

if __name__ == '__main__':
    init_db()
    threading.Thread(target=start_flask, daemon=True).start()
    webview.create_window("Wi-Fi QR Generator", "http://127.0.0.1:5000", width=600, height=800, resizable=True)
    webview.start()
