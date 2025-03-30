from flask import Flask, request, jsonify, render_template
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


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
    return render_template('index.html')


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
        conn.execute(""" INSERT INTO livros (titulo, categoria, autor, imagem_url)
                     VALUES (?,?,?,?) 
                     """, (titulo, categoria, autor, imagem_url))

        conn.commit()

        return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201


@app.route('/livros', methods=['GET'])
def listar_livros():
    with sqlite3.connect('database.db') as conn:
        livros = conn.execute("SELECT * FROM livros").fetchall()

    livros_formatados = []

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


@app.route('/livros/<int:livro_id>', methods=['DELETE'])
def deletar_livro(livro_id):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
        conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"erro": "Livro não encontrado"}), 404

    return jsonify({"menssagem": "Livro excluido com sucesso"}), 200


if __name__ == '__main__':
    app.run(debug=True)
