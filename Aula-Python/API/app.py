from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS livros(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   categoria TEXT NOT NULL,
                   autor TEXT NOT NULL,
                   imagem_url TEXT NOT NULL
                   )""")
        print("Banco de dados criado!!")


init_db()


@app.route('/')
def home_page():
    return '<h2>Minha pagina com Flask</h2>'


@app.route('/doar', methods=['POST'])
def doar():

    dados = request.get_json()

    titulo = dados.get('titulo')
    categoria = dados.get('categoria')
    autor = dados.get('autor')
    imagem_url = dados.get('imagem_url')

    if not all([titulo, categoria, autor, imagem_url]):
        return jsonify({'erro': 'Todos os campos são obrigatórios'}), 400

    with sqlite3.connect('database.db') as conn:
        conn.execute(f""" INSERT INTO livros (titulo, categoria, autor, imagem_url)
                     VALUES (?,?,?,?) 
                     """, (titulo, categoria, autor, imagem_url))

        conn.commit()

        return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201

# Rota para listar todos os livros cadastrados


# Agora vamos criar a rota que irá listar os livros cadastrados, ou seja a rota que irá receber o GET (requisição)
@app.route("/livros", methods=["GET"])
def listar_livros():
    """
    Retorna todos os livros cadastrados no banco de dados.
    """

    # Como vamos puxar os livros que foram cadastrados no banco de dados, devemos refazer mais uma vez a conexão com o banco de dados
    with sqlite3.connect("database.db") as conn:
        # Esse comando é responsável por buscar todos os livros armazenados no banco de dados
        livros = conn.execute("SELECT * FROM livros").fetchall()

        # Vamos decompor e entender esses comandos
        # conn.execute --> Como sabemos todo e qualquer comando que executamos no banco de dados precisamos do conn, ele é a ponte entre o banco de dados e o código Python
        # SELECT * FROM LIVROS --> Consulte todas as informações da tabela Livros
        # fetchall() --> É utilizado para buscar todos os dados retornados por uma consulta SQL e retorna-lós em formato de tupla

        # Por mais que utilizamos o SELECT * FROM LIVROS, esse comando fará somente a consulta dos dados, para que realmente consigamos pegar esses dados formatados precisamos do fetchall() que os pegará e transformará eles em formato de tupla

    # Criamos esse array, pois ele será responsável por armazenar todos os valores que puxarmos do nosso banco de dados
    livros_formatados = []

    # Esse loop for in junto com o dicionário_livros, será o responsável por passar por cada um dos valores das tuplas e com essas duas estruturas conseguiremos organizar os dados para que possamos retornar ao usuário cada um desses valores formatados corretamente
    for livro in livros:
        dicionario_livros = {
            "id": livro[0],
            "titulo": livro[1],
            "categoria": livro[2],
            "autor": livro[3],
            "imagem_url": livro[4]
        }
        livros_formatados.append(dicionario_livros)

    return jsonify(livros_formatados)


if __name__ == '__main__':
    app.run(debug=True)
