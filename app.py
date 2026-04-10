from flask import Flask, request, redirect, session

app = Flask(__name__)
app.secret_key = "123"

import sqlite3

def conectar():
    return sqlite3.connect("banco.db")

# CRIAR TABELA
conn = conectar()
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS agendamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    data TEXT,
    hora TEXT,
    servico TEXT
)
""")
conn.commit()
conn.close()

@app.route("/")
def home():
    return """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Barbearia Paulista</title>
        <style>
            body {
                background:#0f0f0f;
                color:white;
                font-family:Arial;
                padding:20px;
                margin:0;
            }
            h1 {text-align:center;}
            .box {
                background:#1c1c1c;
                padding:20px;
                border-radius:15px;
                max-width:400px;
                margin:auto;
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
                padding:15px;
                margin-top:15px;
                background:gold;
                border:none;
                border-radius:10px;
                font-weight:bold;
                cursor:pointer;
            }
        </style>
    </head>
    <body>
        <h1>💈 Barbearia Paulista</h1>
        <div class="box">
            <form action="/agendar" method="post">
                <input name="nome" placeholder="Seu nome" required>
                <input type="date" name="data" required>
                <input type="time" name="hora" required>
                
                <select name="servico">
                    <option>Corte</option>
                    <option>Barba</option>
                    <option>Completo</option>
                </select>

                <button>Agendar</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.route("/agendar", methods=["POST"])
def agendar():
    nome = request.form["nome"]
    data = request.form["data"]
    hora = request.form["hora"]
    servico = request.form["servico"]

    conn = conectar()
    c = conn.cursor()

    c.execute("INSERT INTO agendamentos (nome,data,hora,servico) VALUES (?,?,?,?)",
              (nome,data,hora,servico))

    conn.commit()
    conn.close()

    return "<h1>Agendamento realizado!</h1><a href='/'>Voltar</a>"

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        if request.form["user"] == "admin" and request.form["senha"] == "123":
            session["logado"] = True
            return redirect("/painel")

    return """
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="background:black;color:white;text-align:center;">
        <h2>Login</h2>
        <form method="post">
            <input name="user" placeholder="Usuário"><br><br>
            <input name="senha" placeholder="Senha" type="password"><br><br>
            <button>Entrar</button>
        </form>
    </body>
    </html>
    """

@app.route("/painel")
def painel():
    if not session.get("logado"):
        return redirect("/login")

    conn = conectar()
    c = conn.cursor()
    dados = c.execute("SELECT * FROM agendamentos").fetchall()
    conn.close()

    lista = ""
    for d in dados:
        lista += f"<p>{d[1]} - {d[2]} {d[3]} ({d[4]})</p>"

    return f"""
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="background:#111;color:white;padding:20px;">
        <h1>📊 Painel</h1>
        {lista}
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
