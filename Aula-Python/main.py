

nome = 'vini'  # string

# -------- camelCase(javaScript)--
# let nomeSobrenome = "Fulano da Silva"
# ----snake_case(python)------
nome_sobrenome = "vini bispo"

# ------ Inteiros (int)
idade = 18
frio = -273

# Ponto flutuante, decimais (float)
temperatura = -2.2
preco = 9.99

# Strings (str)
frase = "A maior heroína de Arcane"

# Booleanos (bool)
maior_de_idade = True
tem_saldo = False

# Nulos (None)
resultado = None

# Exibir na tela
idade = 18
print(idade)

# Exibir soma
Primeiro_valor = 2.2
Segundo_valor = 2.1

print(Primeiro_valor + Segundo_valor)

# Exibir frase
nome = 'Vini'
frase = 'Lindo dia!!'

print(nome, frase)

# Exibir o tipo da variavel
idade = 2.2
nome = "vini"

print(type(nome))
print(type(idade), type(nome))

# Função de Entrada
nome = input("Qual o seu nome ?")

print("Olá, " + nome)

# Solicitando o email e a senha do usuário
Email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

print(f"Seu email é: {Email}")
print(f"Sua senha é: {senha}")

# Calculando a soma de dois números
Primeiro_valor = input("Digite o primeiro numero: ")
Segundo_valor = input("Digite o segundo numero: ")

soma = Primeiro_valor + Segundo_valor
# soma = int(Primeiro_valor) + int(Segundo_valor)

print('A soma dos valores é: ' + soma)
# print('A soma dos valores é: ' + str(soma))


# Também pode ser convertido no momento da captura

primeiro_valor = int(input("Digite o primeiro número: "))
segundo_valor = int(input("Digite o segundo número: "))

# Decimal(float) para String(str)

altura = 1.80
print(type(altura))  # Exibirá float

# Conversão do tipo de float para str
altura = str(altura)

print(type(altura))

# Inteiro(int) para Decimal(float)

idade = 18
print(type(idade))  # Exibirá int

# Conversão do tipo de int para float
idade = float(idade)

print(type(idade))