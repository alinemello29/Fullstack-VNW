# 📚 Lista e Tuplas em Python

## 📋 Introdução

Neste documento, vamos explorar duas das estruturas de dados mais importantes em Python: **Listas** e **Tuplas**. Ambas têm suas particularidades e são amplamente utilizadas para armazenar coleções de itens.

## 📝 Listas

As listas são coleções ordenadas e mutáveis de itens. Você pode adicionar, remover e modificar elementos.

### 🔍 Características das Listas:

- **Mutáveis**: Podem ser alteradas após a criação.
- **Ordenadas**: Mantêm a ordem dos elementos.
- **Podem conter diferentes tipos de dados**: Números, strings, listas, etc.

### 📌 Exemplo de Lista:

```python
# Criando uma lista
minha_lista = [1, 2, 3, 'Python', True]

# Adicionando um elemento
minha_lista.append('Novo Item')

# Removendo um elemento
minha_lista.remove(2)

print(minha_lista)  # Saída: [1, 3, 'Python', True, 'Novo Item']