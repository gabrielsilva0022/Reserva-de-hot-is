from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)


#   CAMINHO ABSOLUTO DO BANCO
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "hotel.db")


#   BANCO DE DADOS
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quartos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero TEXT,
            tipo TEXT,
            preco REAL,
            status TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            quarto_id INTEGER,
            data TEXT,
            FOREIGN KEY(quarto_id) REFERENCES quartos(id)
        )
    """)

    # Inserir quartos se estiver vazio
    cursor.execute("SELECT COUNT(*) FROM quartos")
    if cursor.fetchone()[0] == 0:
        quartos_default = [
            ("101", "Solteiro", 150.0, "livre"),
            ("102", "Casal", 220.0, "livre"),
            ("201", "Luxo", 350.0, "livre"),
        ]
        cursor.executemany(
            "INSERT INTO quartos (numero, tipo, preco, status) VALUES (?, ?, ?, ?)",
            quartos_default
        )
        conn.commit()

    conn.close()


#   ROTAS
@app.route("/")
def index():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quartos")
    quartos = cursor.fetchall()
    conn.close()
    return render_template("index.html", quartos=quartos)


@app.route("/reservar/<int:id>", methods=["GET", "POST"])
def reservar(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM quartos WHERE id = ?", (id,))
    quarto = cursor.fetchone()

    if request.method == "POST":
        nome = request.form["nome"]
        data = request.form["data"]

        cursor.execute("INSERT INTO reservas (nome, quarto_id, data) VALUES (?, ?, ?)",
                       (nome, id, data))
        cursor.execute("UPDATE quartos SET status = 'ocupado' WHERE id = ?", (id,))
        conn.commit()
        conn.close()

        return redirect("/reservas")

    conn.close()
    return render_template("reservar.html", quarto=quarto)


@app.route("/reservas")
def reservas():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT reservas.id, reservas.nome, reservas.data,
               quartos.numero, quartos.tipo
        FROM reservas
        JOIN quartos ON reservas.quarto_id = quartos.id
    """)
    dados = cursor.fetchall()
    conn.close()
    return render_template("reservas.html", dados=dados)


#   EXECUÇÃO
if __name__ == "__main__":
    print("Inicializando banco...")
    init_db()
    print("Banco pronto! Executando servidor...\n")
    app.run(debug=True)
