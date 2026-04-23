#Aprendendo sobre listas, funcionamento e funções

frutas = ['maçã', 'uva', 'laranja']

#numa lista os elementos presentes nela tem suas posições definidas pelo indice, começando pelo [0]
print(frutas[0])
#é possivel começar pelo fim da lista com indice [-1]
print(frutas[-1])

#a função append, é responsavel por adicionar um elemento a lista na ultima posição
frutas.append('caju')
print(frutas)

#a função insert, é responsavel por adicionar um elemento a lista em uma determinada posição
frutas.insert(1,'banana')
print(frutas)

#a função remove, é responsavel por remover um elemento da lista
frutas.remove('banana')
print(frutas)

#a função pop remove e retorna um elemento em sua posição especifica da lista
fruta_removida = frutas.pop(3)
print(fruta_removida)
print(frutas)

#a função sort organiza a lista em ordem ascendente, se for uma lista de numero ficaria na ordem crescente
frutas.sort()
print(frutas)

#a função reverse organiza a lista em ordem decrescente
frutas.reverse()
print(frutas)

#lista de compreensão, nesse caso a lista quadrados terá apenas o quadrado dos numeros pares da lista numeros,
#isso ocorre por meio da função for que passa pela lista numeros,
#e a condicional if que verifica se a sobra da divisão de x na lista numeros por 2 é igual a 0
numeros = [1, 2, 3, 4, 5, 6]
quadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(quadrados)