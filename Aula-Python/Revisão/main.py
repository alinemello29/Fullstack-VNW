
# Definição de variáveis
nome = 'vini'  # string (texto)
idade = 20  # int (número inteiro)
cfp = 236.666  # float (número decimal)
aluno = True  # boolean (valor lógico, verdadeiro ou falso)
dia = None  # NoneType (ausência de valor)
print(dia)  # Imprime "None" no console

# Operadores de comparação:
# =   -> Atribuição de valor
# ==  -> Comparação de igualdade
# !=  -> Diferente
# >   -> Maior que
# <   -> Menor que
# >=  -> Maior ou igual
# <=  -> Menor ou igual

# Operadores lógicos:
# and -> Retorna True se ambas as condições forem verdadeiras (&& em outras linguagens)
# or  -> Retorna True se pelo menos uma condição for verdadeira (|| em outras linguagens)
# not -> Inverte o valor lógico (! em outras linguagens)

# Estrutura condicional para login
login = input('Digite seu nome:')  # Solicita ao usuário o nome
senha = input('Digite a senha:')  # Solicita ao usuário a senha

if login == 'vini' and senha == '40028922':  # Verifica se login e senha correspondem
    print('Parabéns!!!!!!!!!')  # Mensagem de sucesso para Vini
elif login == 'marina' and senha == '35912973':  # Outra combinação válida
    print('Bom dia Querida Marina!')  # Mensagem específica para Marina
else:
    print('Senha incorreta!')  # Qualquer outra entrada gera erro de senha


cadastro = input('Digite seu nome:')

if cadastro == 'vini' or cadastro == 'Carol':
    print('Parabéns!!!')
else:
    print('Acesso Negado!')


# Estruturas de dados

# Lista (list) - Estrutura mutável que armazena vários valores ordenados
frutas = ['uva', 'laranja', 'banana']
print(type(frutas))  # Verifica que 'frutas' é uma lista

# Tupla (tuple) - Estrutura imutável que pode armazenar diferentes tipos de dados
filmes = ("x-men", 'Carros', True, 22, 2.2)
print(type(filmes))  # Verifica que 'filmes' é uma tupla
print(len(filmes))  # Retorna o número de elementos na tupla

# Operações com tuplas numéricas
numeros = (10, 50, 66, 90, 2, 30)
print(max(numeros))  # Retorna o maior número da tupla
print(min(numeros))  # Retorna o menor número da tupla
print(sum(numeros))  # Retorna a soma de todos os elementos da tupla

# Conversão entre lista e tupla
frutas = ['uva', 'laranja', 'banana']
nova_tupla = tuple(frutas)  # Converte lista para tupla
print(type(nova_tupla))  # Verifica que virou uma tupla

nova_lista = list(nova_tupla)  # Converte tupla de volta para lista
print(type(nova_lista))  # Verifica que virou uma lista

# Dicionário (dict) - Estrutura chave-valor
cadastro = {
    'nome': 'vini',
    'idade': 20,
    'altura': 1.75
}
print(cadastro['nome'])  # Acessa e imprime o valor associado à chave 'nome'

# Estrutura de repetição (loop)
resposta = input('Deseja continuar? [S/N]')  # Pergunta ao usuário

while resposta == 'S':  # Enquanto o usuário digitar 'S', continua executando
    print('Executei!')  # Mensagem exibida a cada iteração
    resposta = input('Deseja continuar? [S/N]')  # Pergunta novamente

# Loop 'for' iterando sobre uma string
for item in 'boa tarde!':  # A string é percorrida caractere por caractere
    print(item)  # Cada caractere da string será impresso separadamente


# Lista de filmes
filmes = ['Carros', 'Rei Leão', 'Toy Story', 'Mulan']

# Loop 'for' iterando sobre uma lista
for item in filmes:  # Percorre a lista, atribuindo cada elemento à variável 'item'
    print(item)  # Imprime o nome de cada filme

# ---------------------------------------------------------------------


def soma(numero1, numero2, numero3=5):
    return f'{numero1 * numero2}'(numero1 * numero2) / numero3


n1 = int(input('Digite um numero:'))
n2 = int(input('Digite um numero:'))
n3 = int(input('Digite um numero:'))

resultado = soma(n1, n2, n3)
print(resultado)

# ---------------------------------------------------

pratos = ['PIZZA', 'Churrasco', 'Macarão', 33, 1.9, True]

dia = 'vini'

print(f"olá {dia}")
