def verifica_numero(numero):
    if numero % 2 == 0:
      return f'o numero {numero} é par'
    else:
       return f'o numero {numero} é impar'
    
print(verifica_numero(9))
