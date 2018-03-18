import random
# ERRO: conversão de string em lista não produz o resultado desejado.
#dado = list(input("Digite alguma coisa: "))

# Solução 1: pedir valor por valor da lista repetidamente
tamanho = int(input("Digite o tamanho da lista"))
lista = []
for i in range(tamanho):
    num = int(input("Digite o {}° número: ".format(i+1)))
    lista.append(num)

# Solução 2: pedir a lista completa com seus elementos separados com um mesmo
# padrão
conteudo = input("Digite a lista de números (separe com ', ' ): ")
numeros = conteudo.split(", ")
print(numeros)
print(type(numeros[0]))

# Não esquecer de converter cada elemento da lista para o tipo de dado desejado
for i in range(len(numeros)):
    numeros[i] = int(numeros[i])

print(numeros)
print(type(numeros[0]))
