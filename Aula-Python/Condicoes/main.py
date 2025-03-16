saldo = False  # Define a variável saldo como False (sem dinheiro)

if saldo == False:  # Verifica se saldo é False
    print("Tamo lascado!")  # Se saldo for False, exibe a mensagem

# ---------------------------------------------------------

idade = 18  # Define a idade como 18 anos

if idade >= 18:  # Se a idade for maior ou igual a 18
    print('Você pode dirigir')  # Permite dirigir
else:  # Se for menor de 18 anos
    print('Você ainda não pode dirigir!')  # Não pode dirigir

# ---------------------------------------------------------

saldo = False  # Define saldo como False
idade = 18  # Define idade como 18 anos

# Se a idade for maior ou igual a 18 e saldo for True (ou seja, tem dinheiro)
if idade >= 18 and saldo == True:
    # Pode dirigir e fazer um pagamento
    print('Você pode dirigir e mandar o pix')
# Se a idade for menor de 18 e saldo for False
elif idade < 18 and saldo == False:
    print('Você ainda não pode dirigir')  # Não pode dirigir
# Se nenhuma das condições acima for atendida
else:
    print('Não precisa de carteira aqui no Vai na Web')  # Mensagem alternativa

# ---------------------------------------------------------

# Operadores de Comparação
# =   (atribuição, não é uma comparação)
# ==  (igualdade)
# !== (diferente - errado em Python, o correto é !=)
# >   (maior que)
# <   (menor que)
# >=  (maior ou igual)
# <=  (menor ou igual)

# Operadores Lógicos
# and (e)  -> Ambas as condições precisam ser verdadeiras
# or  (ou) -> Basta uma das condições ser verdadeira
# not (não) -> Inverte o valor da condição (True vira False e vice-versa)

# ---------------------------------------------------------

cargo = input("Digite seu cargo: ")  # Solicita que o usuário digite seu cargo

# Se o cargo for "Admin" ou "gerente", acesso é liberado
if cargo == 'Admin' or cargo == 'gerente':
    print('Acesso Liberado!')
else:  # Se não for Admin ou gerente, acesso é negado
    print('Acesso Negado!')

# ---------------------------------------------------------

for caractere in 'Python':  # Para cada caractere na string "Python"
    print(caractere)  # Exibe o caractere atual

# ---------------------------------------------------------

lista_de_sonhos = ['Iate', 'avião', 'Ferrari', 'Resort']  # Lista de sonhos

print(lista_de_sonhos)  # Exibe a lista completa

for item in lista_de_sonhos:  # Percorre a lista
    print(item)  # Exibe cada item individualmente

# ---------------------------------------------------------

contador = 0  # Inicializa um contador

while contador < 10:  # Enquanto o contador for menor que 10
    print(contador)  # Exibe o valor atual do contador
    contador += 1  # Incrementa o contador em 1

# ---------------------------------------------------------
lanche = 'Pizza'  # Define a string "Pizza"

print(lanche[0])  # Exibe o primeiro caractere da string ('P')
print(lanche[0:2])  # Exibe os dois primeiros caracteres ('Pi')

print(lanche.upper())  # Converte a string para maiúsculas ('PIZZA')
print(lanche.lower())  # Converte a string para minúsculas ('pizza')