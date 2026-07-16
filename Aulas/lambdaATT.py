#soma = lambda a, b: a + b

#print(soma(3, 4))

###############################################################

#par_impar = lambda x: 'Par' if x % 2 == 0 else 'Impar'

#print(par_impar(6))
#print(par_impar(7))

###############################################################

#maior = lambda a, b: a if a > b else b

#print(maior(10, 7))

###############################################################

#numeros = [5, 2, 9, 1, 7]

#numeros_ordenados = sorted(numeros, key=lambda x:x)

#print(numeros_ordenados)

###############################################################

#palavras = ["python", "java", "c", "javascript", "go"]

#tamanho_ordenado = sorted(palavras, key=len)

#print(tamanho_ordenado)

###############################################################

#numeros = [1, 2, 3, 4, 5]

#quadrado = list(map(lambda x:x**2, numeros))

#print(quadrado)

###############################################################

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#pares = list(filter(lambda x:x % 2 == 0, numeros))

#print(pares)

###############################################################

#pessoas = [
#("Ana", 25),
#("Carlos", 18),
#("Pedro", 30),
#("Maria", 22)
#]

#idade = sorted(pessoas, key=lambda x: x[1])

#print(idade)

###############################################################

#from functools import reduce

#numeros = [15, 8, 42, 3, 29]

#maior = reduce(lambda a, b: a if a > b else b, numeros)

#print(maior)

###############################################################

#triplica = lambda a: a * 3

#print(triplica(4))

###############################################################

#positivo_negativo = lambda x: 'Positivo' if x > 0  else ('Negativo' if x < 0 else 'Zero')

#print(positivo_negativo(5))
#print(positivo_negativo(-3))
#print(positivo_negativo(0))

###############################################################

#multiplicacao = lambda a, b: a * b

#print(multiplicacao(5, 6))

###############################################################

#celsius_fahrenheit = lambda c: (c * 9/5) + 32

#print(celsius_fahrenheit(30))

###############################################################

#numeros = [-10, 5, -3, 8, -2]

#ordenacao = sorted(numeros, key=lambda x: abs(x) )

#print(ordenacao)

###############################################################

#numeros = [2, 4, 6, 8]

#dobro = list(map(lambda x:x**2, numeros))

#print(dobro)

###############################################################

#numeros = [3, 12, 7, 18, 5, 20]

#maiores = list(filter(lambda x: x > 10, numeros))

#print(maiores)

###############################################################

#dados = [
#("A", 3),
#("B", 1),
#("C", 2)
#]

#seg_numero = sorted(dados, key=lambda x:x[1])

#print(seg_numero)

###############################################################

#dois_numeros = lambda a, b: a if a > b else b

#print(dois_numeros(-9, -6))

###############################################################

#palavras = ["banana", "uva", "abacaxi", "kiwi"]

#ordenadas = sorted(palavras, key=lambda x:x[-1])

#print(ordenadas)

##############################################################################################################################

#from functools import reduce

#numeros = [1, 2, 3, 4, 5]

#somar = reduce(lambda a, b: a + b, numeros)

#print(somar)

###############################################################

#quadrado = lambda a: a ** 2

#print(quadrado(9))

###############################################################

#maior = lambda a: 'Maior' if a > 10 else 'Menor ou igual'

#print(maior(11))

###############################################################

#tres = lambda a, b, c: a + b + c

#print(tres(1, 2, 3))

###############################################################

#numeros = [10, 7, 4, 9, 6]

#ordenados = sorted(numeros, key=lambda x:x % 3)

#print(ordenados)

###############################################################

#palavras = ["python", "java", "ruby", "c"]

#maiuscula = list(map(lambda x: x.upper(), palavras))

#print(maiuscula)

###############################################################

#numeros = [3, 5, 9, 10, 12, 14]

#divisivel = list(filter(lambda x: x % 3 == 0 , numeros))

#print(divisivel)

###############################################################

#pessoas = [
#("Carlos", 25),
#("Ana", 30),
#("Bruno", 20)
#]

#primeiro = sorted(pessoas, key=lambda x:x[0])

#print(primeiro)

###############################################################

#palavras = ["computador", "sol", "python", "ar"]

#numero = sorted(palavras, key=len)

#print(numero)

###############################################################

#numeros = [5, -3, 7, -1, -8, 2]

#negativos = list(filter(lambda x: x < 0, numeros))

#print(negativos)

###############################################################

from functools import reduce

numeros = [2, 3, 4, 5]

multiplicar = reduce(lambda a, b: a * b, numeros)

print(multiplicar)



