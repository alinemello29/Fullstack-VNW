# Importa as bibliotecas necessárias do Flask para criar o servidor e manipular requisições e respostas.
from flask import Flask, request, jsonify, render_template
# Importa o módulo sqlite3 para interagir com o banco de dados SQLite.
import sqlite3

# Cria uma instância da aplicação Flask.
app = Flask(__name__)

# Função para inicializar o banco de dados SQLite.


def init_db():
    # Abre uma conexão com o banco de dados (ou cria o arquivo 'database.db' se não existir).
    with sqlite3.connect('database.db') as conn:
        # Cria a tabela 'livros' caso ela não exista, contendo os campos: id, titulo, categoria, autor e imagem_url.
        conn.execute("""CREATE TABLE IF NOT EXISTS livros(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     titulo TEXT NOT NULL,
                     categoria TEXT NOT NULL,
                     autor TEXT NOT NULL,
                     imagem_url TEXT NOT NULL
                     )
                     """)
        # Imprime uma mensagem no console indicando que o banco foi inicializado com sucesso.
        print("Banco de dados inicializado com sucesso!!")


# Chama a função para garantir que o banco de dados esteja pronto antes de iniciar o servidor.
init_db()

# Rota principal da aplicação que retorna uma página HTML.


@app.route('/')
def homepage():
    # Renderiza um template HTML chamado 'index.html'.
    return render_template('index.html')

# Rota para cadastrar um novo livro (doação), que aceita apenas requisições POST.


@app.route("/doar", methods=['POST'])
def doar():
    # Obtém os dados enviados na requisição no formato JSON.
    dados = request.get_json()

    # Extrai os campos necessários do JSON recebido.
    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    imagem_url = dados.get("imagem_url")

    # Verifica se todos os campos foram preenchidos.
    if not all([titulo, categoria, autor, imagem_url]):
        # Retorna um erro 400 (Bad Request) com uma mensagem de erro.
        return jsonify({'erro': 'Todos os campos são obrigatórios'}), 400

    # Conecta ao banco de dados e insere as informações do livro.
    with sqlite3.connect('database.db') as conn:
        conn.execute(""" INSERT INTO livros (titulo, categoria, autor, imagem_url)
                         VALUES(?,?,?,?)
                         """, (titulo, categoria, autor, imagem_url))
        # Confirma a transação para salvar as mudanças.
        conn.commit()

        # Retorna uma mensagem de sucesso com o código 201 (Created).
        return jsonify({'mensagem': 'Livros cadastrados com sucesso'}), 201

# Rota para listar todos os livros cadastrados, que aceita apenas requisições GET.


@app.route('/livros', methods=['GET'])
def listar_livros():
    # Conecta ao banco de dados e recupera todos os registros da tabela 'livros'.
    with sqlite3.connect('database.db') as conn:
        livros = conn.execute("SELECT * FROM livros").fetchall()

    # Lista para armazenar os livros formatados.
    livros_formatados = []

    # Formata cada livro como um dicionário e adiciona à lista.
    for livro in livros:
        dicionario_livros = {
            "id": livro[0],
            "titulo": livro[1],
            "categoria": livro[2],
            "autor": livro[3],
            "imagem_url": livro[4]
        }
        livros_formatados.append(dicionario_livros)

    # Retorna a lista de livros no formato JSON.
    return jsonify(livros_formatados)

# Rota para deletar um livro pelo ID, que aceita apenas requisições DELETE.


@app.route('/livros/<int:livro_id>', methods=['DELETE'])
def deletar_livro(livro_id):
    # Conecta ao banco de dados e cria um cursor para executar comandos SQL.
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        # Executa a exclusão do livro com o ID especificado.
        cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
        # Confirma a transação para salvar as mudanças.
        conn.commit()

    # Verifica se algum registro foi afetado (se o livro foi encontrado e excluído).
    if cursor.rowcount == 0:
        # Retorna um erro 400 (Bad Request) se o livro não foi encontrado.
        return jsonify({"erro": "Livro não encontrado"}), 400

    # Retorna uma mensagem de sucesso com o código 200 (OK).
    return jsonify({"menssagem": "Livro excluído com sucesso"}), 200


# Ponto de entrada da aplicação: inicia o servidor Flask em modo debug.
if __name__ == "__main__":
    app.run(debug=True)
