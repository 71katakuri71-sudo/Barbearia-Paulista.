from flask import Flask, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "123"

USER = "admin"
PASS = "123"

def init_db():
    conn = sqlite3.connect("agendamentos.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        data TEXT,
        horario TEXT,
        status TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return """
    <html>
    <head>
    <title>Barbearia Paulista</title>

    <style>
    body { margin:0; font-family:'Segoe UI'; background:#0d0d0d; color:white; }
    .container { max-width:420px; margin:auto; padding:20px; }
    h1 { text-align:center; color:gold; }

    .card {
        background:#1c1c1c;
        padding:20px;
        border-radius:20px;
        margin-top:20px;
    }

    input {
        width:100%;
        padding:14px;
        margin-top:10px;
        border-radius:12px;
        border:none;
        background:#2a2a2a;
        color:white;
    }

    button {
        width:100%;
        padding:14px;
        margin-top:15px;
        border:none;
        border-radius:12px;
        background:gold;
        font-weight:bold;
        cursor:pointer;
    }

    .servico {
        display:flex;
        justify-content:space-between;
        padding:10px 0;
        border-bottom:1px solid #333;
    }

    a { display:block; text-align:center; margin-top:20px; color:gold; }

    .whatsapp {
        position:fixed;
        bottom:20px;
        right:20px;
        background:#25D366;
        padding:15px;
        border-radius:50%;
        text-decoration:none;
        color:white;
    }

    </style>
    </head>

    <body>

    <div class="container">

    <h1>💈 Barbearia Paulista</h1>

    <div class="card">
        <h3>Agendar</h3>
        <form action="/agendar" method="POST">
            <input name="nome" placeholder="Nome" required>
            <input type="date" name="data" required>
            <input type="time" name="horario" required>
            <button>Agendar</button>
        </form>
    </div>

    <div class="card">
        <h3>Serviços</h3>
        <div class="servico"><span>Corte</span><span>R$30</span></div>
        <div class="servico"><span>Barba</span><span>R$20</span></div>
        <div class="servico"><span>Completo</span><span>R$45</span></div>
    </div>

    <a href="/login">🔐 Área do barbeiro</a>

    </div>

    <a class="whatsapp" href="#">💬</a>

    </body>
    </html>
    """

@app.route("/agendar", methods=["POST"])
def agendar():
    nome = request.form["nome"]
    data = request.form["data"]
    horario = request.form["horario"]

    conn = sqlite3.connect("agendamentos.db")
    c = conn.cursor()

    c.execute("SELECT * FROM agendamentos WHERE data=? AND horario=?", (data, horario))
    if c.fetchone():
        return "<h2>Horário ocupado</h2><a href='/'>Voltar</a>"

    c.execute("INSERT INTO agendamentos (nome,data,horario,status) VALUES (?,?,?,?)",
              (nome, data, horario, "Agendado"))

    conn.commit()
    conn.close()

    return redirect("/")

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

@app.route("/painel")
def painel():
    if not session.get("logado"):
        return redirect("/login")

    conn = sqlite3.connect("agendamentos.db")
    c = conn.cursor()
    c.execute("SELECT * FROM agendamentos")
    dados = c.fetchall()

    total = len(dados)
    faturamento = total * 30

    conn.close()

    linhas = ""
    for ag in dados:
        linhas += f"""
        <tr>
        <td>{ag[1]}</td>
        <td>{ag[2]}</td>
        <td>{ag[3]}</td>
        <td>{ag[4]}</td>
        <td>
            <a href='/finalizar/{ag[0]}'>✔</a>
            <a href='/excluir/{ag[0]}'>❌</a>
        </td>
        </tr>
        """

    return f"""
    <html>
    <head>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>
    body {{ background:#0d0d0d; color:white; font-family:'Segoe UI'; }}
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

    <h1>Painel</h1>

    <div class="stats">
        <div class="box">Clientes: {total}</div>
        <div class="box">R$: {faturamento}</div>
    </div>

    <canvas id="grafico"></canvas>

    <table>
    <tr>
    <th>Nome</th><th>Data</th><th>Hora</th><th>Status</th><th>Ação</th>
    </tr>
    {linhas}
    </table>

    <br><a href="/logout">Sair</a>

    </div>

    <script>
    new Chart(document.getElementById('grafico'), {{
        type: 'bar',
        data: {{
            labels: ['Clientes'],
            datasets: [{{
                label: 'Total',
                data: [{total}]
            }}]
        }}
    }});
    </script>

    </body>
    </html>
    """

@app.route("/finalizar/<int:id>")
def finalizar(id):
    conn = sqlite3.connect("agendamentos.db")
    c = conn.cursor()
    c.execute("UPDATE agendamentos SET status='Finalizado' WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/painel")

@app.route("/excluir/<int:id>")
def excluir(id):
    conn = sqlite3.connect("agendamentos.db")
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