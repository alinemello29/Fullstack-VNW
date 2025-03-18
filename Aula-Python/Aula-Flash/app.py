# Importando a classe Flask
from flask import Flask
# A variável app recebe a instancia da classe Flask
app = Flask(__name__)


# Criando a primeira rota
@app.route('/')
# Função que será acionada ao acessar a rota
def index():
    # Retorno impresso no navegador quando a rota for acessada
    return "<h1>Olá, mundo!</h1>"


# Função que roda o servidor local
app.run()
