from flask import Flask, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "segredo_super_forte_987"

USER = "admin"
PASS = "123"

# ---------------- BANCO ----------------
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

# ---------------- HOME ----------------
@app.route("/")
def home():
    return """
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Barbearia Paulista</title>

    <style>
    body { margin:0; font-family:Segoe UI; background:#0a0a0a; color:white; }
    .topo { text-align:center; padding:60px 20px; background:linear-gradient(black,#111); }
    .topo h1 { font-size:32px; color:gold; }

    .btn {
        background:gold; padding:15px; border-radius:10px;
        text-decoration:none; color:black; font-weight:bold;
    }

    .container { max-width:420px; margin:auto; padding:20px; }

    .card {
        background:#1c1c1c;
        padding:20px;
        border-radius:15px;
        margin-top:20px;
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

    .servico {
        display:flex;
        justify-content:space-between;
        padding:10px 0;
        border-bottom:1px solid #333;
    }

    a { color:gold; text-align:center; display:block; margin-top:20px; }
    </style>
    </head>

    <body>

    <div class="topo">
        <h1>💈 Barbearia Paulista</h1>
        <p>Estilo e qualidade</p>
        <a href="#agendar" class="btn">Agendar Agora</a>
    </div>

    <div class="container">

    <div class="card">
        <h3>Serviços</h3>
        <div class="servico"><span>Corte</span><span>R$30</span></div>
        <div class="servico"><span>Barba</span><span>R$20</span></div>
        <div class="servico"><span>Completo</span><span>R$45</span></div>
    </div>

    <div class="card" id="agendar">
        <h3>Agendar</h3>

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

# ---------------- AGENDAR ----------------
@app.route("/agendar", methods=["POST"])
def agendar():
    nome = request.form["nome"]
    data = request.form["data"]
    hora = request.form["hora"]
    servico = request.form["servico"]

    conn = db()
    c = conn.cursor()

    c.execute("SELECT * FROM agendamentos WHERE data=? AND hora=?", (data, hora))
    if c.fetchone():
        return "<h2>❌ Horário ocupado</h2><a href='/'>Voltar</a>"

    c.execute("INSERT INTO agendamentos (nome,data,hora,servico,status) VALUES (?,?,?,?,?)",
              (nome,data,hora,servico,"Agendado"))

    conn.commit()
    conn.close()

    return "<h2>✅ Agendamento realizado!</h2><a href='/'>Voltar</a>"

# ---------------- LOGIN ----------------
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

# ---------------- PAINEL ----------------
@app.route("/painel")
def painel():
    if not session.get("logado"):
        return redirect("/login")

    conn = db()
    c = conn.cursor()
    dados = c.execute("SELECT * FROM agendamentos").fetchall()
    conn.close()

    # preços reais
    precos = {
        "Corte": 30,
        "Barba": 20,
        "Completo": 45
    }

    total = len(dados)
    faturamento = sum(precos.get(d[4], 0) for d in dados)

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

# ---------------- FINALIZAR ----------------
@app.route("/finalizar/<int:id>")
def finalizar(id):
    conn = db()
    c = conn.cursor()
    c.execute("UPDATE agendamentos SET status='Finalizado' WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/painel")

# ---------------- EXCLUIR ----------------
@app.route("/excluir/<int:id>")
def excluir(id):
    conn = db()
    c = conn.cursor()
    c.execute("DELETE FROM agendamentos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/painel")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
