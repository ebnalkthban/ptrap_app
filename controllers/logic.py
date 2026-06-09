import sqlite3
import hashlib

DB_PATH = 'data/ptrap.db'

# --- Auth Logic ---
def hash_pw(pw): return hashlib.sha256(pw.encode()).hexdigest()

def login(email, pw):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, hash_pw(pw)))
    user = c.fetchone()
    conn.close()
    return (True, user) if user else (False, "Invalid credentials")

def register(email, pw):
    if len(pw) < 8: return False, "Password too short"
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO users (email, password) VALUES (?,?)", (email, hash_pw(pw)))
        conn.commit()
        conn.close()
        return True, "Registered successfully"
    except: return False, "Email already exists"

# --- Inventory Logic ---
def add_prod(name, brand, cat, buy, sell, stock, compat):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO products (name, brand, category, buy_price, sell_price, stock, compatibility) VALUES (?,?,?,?,?,?,?)",
              (name, brand, cat, buy, sell, stock, compat))
    conn.commit()
    conn.close()
    return True

def get_prods(query=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if query:
        c.execute("SELECT * FROM products WHERE name LIKE ? OR brand LIKE ? OR compatibility LIKE ?", (f'%{query}%', f'%{query}%', f'%{query}%'))
    else:
        c.execute("SELECT * FROM products")
    data = c.fetchall()
    conn.close()
    return data

# --- Sales Logic ---
def process_sale(p_id, qty, disc):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT sell_price, stock FROM products WHERE id=?", (p_id,))
    res = c.fetchone()
    if not res or res[1] < int(qty): return False, "Stock issue"
    total = (res[0] * int(qty)) - float(disc)
    c.execute("INSERT INTO sales (product_id, quantity, total, discount) VALUES (?,?,?,?)", (p_id, qty, total, disc))
    c.execute("UPDATE products SET stock = stock - ? WHERE id = ?", (qty, p_id))
    conn.commit()
    conn.close()
    return True, f"Total: {total}"

def get_sales():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT s.id, p.name, s.quantity, s.total, s.date FROM sales s JOIN products p ON s.product_id = p.id ORDER BY s.date DESC")
    data = c.fetchall()
    conn.close()
    return data

# --- I18N Logic ---
LANGS = {
    'ar': {'app':'PTRAP','log':'دخول','reg':'جديد','inv':'مخزن','sal':'بيع','set':'ضبط','lang':'اللغة','wel':'مرحباً','email':'بريد','pass':'كلمة'},
    'en': {'app':'PTRAP','log':'Login','reg':'New','inv':'Stock','sal':'Sale','set':'Set','lang':'Lang','wel':'Welcome','email':'Email','pass':'Pass'},
    'es': {'app':'PTRAP','log':'Entrar','reg':'Nuevo','inv':'Stock','sal':'Venta','set':'Ajuste','lang':'Idioma','wel':'Hola','email':'Email','pass':'Pass'},
    'ru': {'app':'PTRAP','log':'Вход','reg':'Новый','inv':'Склад','sal':'Продажа','set':'Настр','lang':'Язык','wel':'Привет','email':'Email','pass':'Пароль'}
}
current_lang = 'ar'
def get_t(key): return LANGS.get(current_lang, LANGS['en']).get(key, key)
