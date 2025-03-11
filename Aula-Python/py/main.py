# Lista de alunos
alunos = ['Vini', 'Marina', 'João', 'Fernanda']
#            0      1        2        3

# Acessando elementos da lista por índice
print(alunos[0])   # Exibe 'Vini' (primeiro elemento)
print(alunos[-1])  # Exibe 'Fernanda' (último elemento)

# Exibindo o tipo da variável 'alunos'
print(type(alunos))  # Saída: <class 'list'>

# ----------------

# Adicionando um novo aluno à lista
alunos = ['Vini', 'Marina', 'João', 'Fernanda', 'Joy']
print(len(alunos))  # Exibe o tamanho da lista: 5

# -----------------------------

# Lista de frutas com elementos duplicados
frutas = ['maçã', 'banana', 'uva', 'laranja', 'banana']

# Inserindo 'manga' na posição 2 da lista
frutas.insert(2, 'manga')
print(frutas)  # Saída: ['maçã', 'banana', 'manga', 'uva', 'laranja', 'banana']

# ------------------------------------------------------

# Adicionando 'abacaxi' ao final da lista
frutas.append('abacaxi')
# Saída: ['maçã', 'banana', 'manga', 'uva', 'laranja', 'banana', 'abacaxi']
print(frutas)

# ---------------------------------------------------------

# Ordenando a lista de frutas em ordem alfabética
frutas.sort()
# Saída: ['abacaxi', 'banana', 'banana', 'laranja', 'maçã', 'manga', 'uva']
print(frutas)

# Lista de números
numeros = [10, 12, 20, 60, 3, 5, 9]

# Ordenando a lista de números em ordem crescente
numeros.sort()
print(numeros)  # Saída: [3, 5, 9, 10, 12, 20, 60]

# -------------------------------------------

# Criando uma nova lista de frutas
frutas = ['maçã', 'banana', 'uva', 'laranja', 'banana']

# Removendo a primeira ocorrência de 'banana'
frutas.remove('banana')
print(frutas)  # Saída: ['maçã', 'uva', 'laranja', 'banana']

# ------------------------------------------

# Removendo o último elemento da lista
frutas.pop()
print(frutas)  # Último elemento removido

# ------------------------------------------

# Criando uma nova lista de frutas
frutas = ['maçã', 'banana', 'uva', 'laranja', 'banana']

# Contando quantas vezes 'banana' aparece na lista
quantidade = frutas.count('banana')
print('Quantidade de banana:', quantidade)  # Saída: Quantidade de banana: 2

# ---------------------------------------------------------

# Tuplas (imutáveis)

# Tupla contendo diferentes tipos de dados
minha_tupla = ['vini', '1234', ('cpf', 'rg'), True, 22]
# Saída: <class 'list'> (essa variável na verdade é uma lista, não uma tupla!)
print(type(minha_tupla))

# Tupla correta de filmes
filmes = ('Interestelar', 'Senhor dos Aneis', 'Harry Potter', 'X-Men')

# Verificando se 'Matrix' está na tupla
print('Matrix' in filmes)  # Saída: False (não está na tupla)

# -------------------------------------

# Duas tuplas de pratos
pratos1 = ("lasanha", "strogonoff")
pratos2 = ("Churrasco", "Sushi")

# Multiplicando uma tupla (repete os elementos)
print(pratos2 * 2)  # Saída: ('Churrasco', 'Sushi', 'Churrasco', 'Sushi')

# Concatenando tuplas
nova_tupla = pratos1 + pratos2
print(nova_tupla)  # Saída: ('lasanha', 'strogonoff', 'Churrasco', 'Sushi')