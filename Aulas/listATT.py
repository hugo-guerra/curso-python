#numeros = [1, 2, 3, 4, 5]

#dobro = [n * 2 for n in numeros]
#print(dobro)

##################################################

#numeros = [1, 2, 3, 4, 5]

#quadrado = [n ** 2 for n in numeros]
#print(quadrado)

##################################################

#nomes = ["ana", "joao", "maria"]

#maiusculo = [nome.upper() for nome in nomes]
#print(maiusculo)

##################################################

#numeros = [1, 2, 3, 4, 5, 6]

#pares = [n for n in numeros if n % 2 == 0]
#print(pares)

##################################################

#numeros = [5, 12, 8, 20, 3]

#maiores = [n for n in numeros if n > 10]
#print(maiores)

##################################################

#palavras = ["python", "java", "c", "javascript"]

#maior = [n for n in palavras if len(n) > 4]
#print(maior)

##################################################

#numeros = [1, 2, 3, 4, 5, 6]

#pares = [n * 2 for n in numeros if n % 2 == 0 ** 2]
#print(pares)

##################################################

#numeros = [1, 2, 3, 4, 5, 6]

#impares = [n ** 2 for n in numeros if n % 2 != 0]
#print(impares)

##################################################

#palavras = ["python", "java", "csharp", "go", "javascript"]

#maiusculo = [p.upper() for p in palavras if len(p) > 5]
#print(maiusculo)

##################################################

#numeros = [1, 2, 3, 4]

#numeroo = [(numero, numero ** 2) for numero in range(1, 5)]
#print(numeroo)

##################################################

#numeros = [1, 2, 3]

#string = [f'Números {numero}' for numero in numeros]
#print(string)

##################################################

#nomes = ["  ana", "joao  ", "  maria  "]

#espaco = [n.strip().upper() for n in nomes]
#print(espaco)

##################################################
#errado
cars = ['BMW', 'Tesla', 'Toyota', 'Audi']

for i in range(len(cars)):
    if cars[i].startswith('T'):
        cars.pop(i)

print(cars)

#corrigida\/

cars = ['BMW', 'Tesla', 'Toyota', 'Audi']

cars = [car for car in cars if not car.startswith('T')]

print(cars)