import sqlite3
import hashlib
import os
from kivy.app import App

# هذه الدالة تضمن أن قاعدة البيانات تُحفظ في مكان مسموح به على الأندرويد
def get_db_path():
    try:
        # المجلد الخاص ببيانات التطبيق على الأندرويد
        data_dir = App.get_running_app().user_data_dir
    except:
        # إذا كان التشغيل على ويندوز، استخدم المجلد الحالي
        data_dir = "data"
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    return os.path.join(data_dir, 'ptrap.db')

def get_conn():
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # التأكد من وجود الجداول في كل مرة نفتح فيها الاتصال (للأمان)
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, brand TEXT, category TEXT, buy_price REAL, sell_price REAL, stock INTEGER, compatibility TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS sales (id INTEGER PRIMARY KEY AUTOINCREMENT, product_id INTEGER, quantity INTEGER, total REAL, discount REAL, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
    conn.commit()
    return conn

# --- الآن قم بتحديث كل الدوال لتستخدم get_conn() ---
def login(email, pw):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, hashlib.sha256(pw.encode()).hexdigest()))
    user = c.fetchone()
    conn.close()
    return (True, user) if user else (False, "Invalid credentials")

# ... وبالمثل لبقية الدوال (register, add_prod, get_prods, process_sale, get_sales) ...
