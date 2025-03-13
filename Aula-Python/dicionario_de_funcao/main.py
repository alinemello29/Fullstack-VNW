# Criando um dicionário simples com uma chave e um valor
nome_do_dicionario = {'chave': 'valor'}

# Imprime o dicionário inteiro
print(nome_do_dicionario)

# Imprime o tipo do objeto (neste caso, um dicionário)
print(type(nome_do_dicionario))

# ---------------------------------------------

# Criando um dicionário chamado "comida" com chaves "nome" e "idade" inicializadas como strings vazias
comida = {
    'nome': '',
    'idade': '',
}

# Modificando o valor da chave "nome" no dicionário
comida['nome'] = 'vini'

# Exibe o dicionário atualizado
print(comida)

# -------------------------

# Criando um dicionário chamado "cadastro" com informações de uma pessoa
cadastro = {
    'nome': 'vini',
    'altura': '1.75',
    'idade': '20'
}

# Exibe apenas o valor associado à chave "nome"
print(cadastro['nome'])

# Adiciona uma nova chave "cidade" ao dicionário
cadastro['cidade'] = 'salvador'

# Modifica o valor da chave "idade"
cadastro['idade'] = 18

# Exibe o dicionário atualizado
print(cadastro)

# Remove a chave "altura" do dicionário
del cadastro['altura']

# Exibe o dicionário após a remoção da chave "altura"
print(cadastro)

# -------------------

# Remove todos os itens do dicionário, tornando-o vazio
cadastro.clear()

# Exibe o dicionário agora vazio
print(cadastro)

# ------------------------------------------

# Criando um dicionário com informações sobre um livro
livros = {
    'nome': 'A arte da guerra',
    'autor': 'sun tzu'
}

# Remove e retorna o último item do dicionário
ultimo_item = livros.popitem()
print(f"Item removido: {ultimo_item}")
print(livros)  # Exibe o dicionário após a remoção do item

# Adiciona novos pares chave-valor ao dicionário
livros.update({'ano': 1520, 'editora': 'xingling'})

# Exibe o dicionário atualizado
print(livros)

# ---------------------------------------------------

# Definição de uma função simples que exibe uma mensagem


def frase():
    print('Olá, sejam bem-vindos!!')


# Chamada da função
frase()

# ---------------------------------------

# Função que verifica se um número é par ou ímpar


def verifica_numero(numero):
    if numero % 2 == 0:
        return f'O número {numero} é par'
    else:
        return f'O número {numero} é ímpar'


# Chamada da função e impressão do resultado
print(verifica_numero(9))

# print(resultado)  # Comentado porque a variável "resultado" não foi definida
