from flask import Flask, request, redirect, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "123"

USER = "admin"
PASS = "123"

def db():
    return sqlite3.connect("agendamentos.db")

def init():
    conn = db()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        data TEXT,
        hora TEXT,
        servico TEXT,
        status TEXT
    )
    """)
    conn.commit()
    conn.close()

init()

# HOME (🔥 VISUAL PROFISSIONAL)
@app.route("/")
def home():
    return """
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Barbearia Paulista</title>

    <style>
    body {
        margin:0;
        font-family:Segoe UI;
        background:#0a0a0a;
        color:white;
    }

    .hero {
        height:90vh;
        background:url('https://images.unsplash.com/photo-1517836357463-d25dfeac3438') center/cover;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        text-align:center;
    }

    .hero h1 {
        font-size:40px;
        color:gold;
        text-shadow:2px 2px 10px black;
    }

    .btn {
        background:gold;
        padding:15px 25px;
        border-radius:10px;
        text-decoration:none;
        color:black;
        font-weight:bold;
    }

    .container {
        max-width:900px;
        margin:auto;
        padding:20px;
    }

    .section {
        margin-top:40px;
    }

    .servicos {
        display:flex;
        gap:15px;
        flex-wrap:wrap;
    }

    .card {
        flex:1;
        min-width:250px;
        background:#1c1c1c;
        padding:20px;
        border-radius:15px;
        text-align:center;
    }

    input, select {
        width:100%;
        padding:12px;
        margin-top:10px;
        border-radius:10px;
        border:none;
    }

    button {
        width:100%;
        padding:14px;
        margin-top:15px;
        background:gold;
        border:none;
        border-radius:10px;
        font-weight:bold;
        cursor:pointer;
    }

    a {
        color:gold;
        text-align:center;
        display:block;
        margin-top:20px;
    }
    </style>
    </head>

    <body>

    <div class="hero">
        <h1>💈 Barbearia Paulista</h1>
        <p>Estilo e experiência premium</p>
        <a href="#agendar" class="btn">Agendar Agora</a>
    </div>

    <div class="container">

    <div class="section">
        <h2 style="text-align:center;color:gold;">Serviços</h2>

        <div class="servicos">
            <div class="card"><h3>Corte</h3><p>R$30</p></div>
            <div class="card"><h3>Barba</h3><p>R$20</p></div>
            <div class="card"><h3>Completo</h3><p>R$45</p></div>
        </div>
    </div>

    <div class="section">
        <h2 style="text-align:center;color:gold;">Sobre</h2>
        <p style="text-align:center;">
        Ambiente moderno com estilo clássico, oferecendo qualidade e conforto.
        </p>
    </div>

    <div class="section" id="agendar">
        <h2 style="text-align:center;color:gold;">Agendar</h2>

        <form action="/agendar" method="POST">
            <input name="nome" placeholder="Nome" required>
            <input type="date" name="data" required>
            <input type="time" name="hora" required>

            <select name="servico">
                <option>Corte</option>
                <option>Barba</option>
                <option>Completo</option>
            </select>

            <button>Confirmar</button>
        </form>
    </div>

    <a href="/login">🔐 Painel</a>

    </div>

    </body>
    </html>
    """

# AGENDAR (🔥 COM REGRA DE 30 MIN)
@app.route("/agendar", methods=["POST"])
def agendar():
    nome = request.form["nome"]
    data = request.form["data"]
    hora = request.form["hora"]
    servico = request.form["servico"]

    conn = db()
    c = conn.cursor()

    c.execute("SELECT hora FROM agendamentos WHERE data=?", (data,))
    horarios = c.fetchall()

    hora_nova = datetime.strptime(hora, "%H:%M")

    for h in horarios:
        hora_existente = datetime.strptime(h[0], "%H:%M")
        diferenca = abs((hora_nova - hora_existente).total_seconds() / 60)

        if diferenca < 30:
            conn.close()
            return "<h2>Horário muito próximo (mínimo 30min)</h2><a href='/'>Voltar</a>"

    c.execute("INSERT INTO agendamentos (nome,data,hora,servico,status) VALUES (?,?,?,?,?)",
              (nome,data,hora,servico,"Agendado"))

    conn.commit()
    conn.close()

    return redirect("/")

# LOGIN
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        if request.form["user"] == USER and request.form["senha"] == PASS:
            session["logado"] = True
            return redirect("/painel")

    return """
    <body style="background:#111;color:white;text-align:center">
    <h2>Login</h2>
    <form method="POST">
        <input name="user"><br>
        <input type="password" name="senha"><br>
        <button>Entrar</button>
    </form>
    </body>
    """

# PAINEL
@app.route("/painel")
def painel():
    if not session.get("logado"):
        return redirect("/login")

    conn = db()
    c = conn.cursor()
    dados = c.execute("SELECT * FROM agendamentos").fetchall()
    conn.close()

    total = len(dados)
    faturamento = total * 30

    linhas = ""
    for d in dados:
        linhas += f"""
        <tr>
            <td>{d[1]}</td>
            <td>{d[2]}</td>
            <td>{d[3]}</td>
            <td>{d[4]}</td>
            <td>{d[5]}</td>
            <td>
                <a href='/finalizar/{d[0]}'>✔</a>
                <a href='/excluir/{d[0]}'>❌</a>
            </td>
        </tr>
        """

    return f"""
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    body {{ background:#0d0d0d; color:white; font-family:Segoe UI; }}
    .container {{ max-width:700px; margin:auto; padding:20px; }}
    h1 {{ text-align:center; color:gold; }}

    .stats {{
        display:flex;
        justify-content:space-around;
        margin-top:20px;
    }}

    .box {{
        background:#1c1c1c;
        padding:15px;
        border-radius:10px;
    }}

    table {{
        width:100%;
        margin-top:20px;
        border-collapse:collapse;
    }}

    th {{ background:gold; color:black; }}
    td, th {{ padding:10px; text-align:center; }}

    tr:nth-child(even) {{ background:#1a1a1a; }}
    </style>
    </head>

    <body>
    <div class="container">

    <h1>📊 Dashboard</h1>

    <div class="stats">
        <div class="box">Clientes: {total}</div>
        <div class="box">R$: {faturamento}</div>
    </div>

    <table>
    <tr>
    <th>Nome</th><th>Data</th><th>Hora</th><th>Serviço</th><th>Status</th><th>Ação</th>
    </tr>
    {linhas}
    </table>

    <br><a href="/logout">Sair</a>

    </div>
    </body>
    </html>
    """

@app.route("/finalizar/<int:id>")
def finalizar(id):
    conn = db()
    c = conn.cursor()
    c.execute("UPDATE agendamentos SET status='Finalizado' WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/painel")

@app.route("/excluir/<int:id>")
def excluir(id):
    conn = db()
    c = conn.cursor()
    c.execute("DELETE FROM agendamentos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/painel")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
