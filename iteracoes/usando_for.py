

lista = [43, 100, 3]
# Implementação com erro, duas ideias misturadas
for i in lista: #elemento?
    if lista[i]%2 == 1: #índice?
        print("é ímpar")

# Solução 1: decidir que a variável assumirá os valores dos elementos da lista
for n in lista:
    if n%2 == 1:
        print("é ímpar")

# Solução 2: decidir que a variável assumirá os possíveis índices da lista
for i in range(len(lista)):
    if lista[i]%2 == 1:
        print("é ímpar")
