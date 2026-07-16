#x = 5

#print(isinstance(x, int))  # True

###################################################

#nome = 'Hugo'

#print(isinstance(nome, str))

###################################################

#dados = [1, 2, 3]

#print(isinstance(dados, list))

###################################################

#x = 10

#if isinstance(x, int):
#    print('Inteiro')

###################################################

#x = 3.14

#if isinstance(x, float):
#    print('É decimal')

###################################################

#x = 5

#print(isinstance(x, (int, float)))

###################################################

#lista = [1, "a", 2, "b", 3]

#solucao = [x for x in lista if isinstance(x, (int, float))]
#print(solucao)

###################################################

#lista = [1, "a", 2, "b", 3]

#soma = sum(x for x in lista if isinstance(x, int))
#print(soma)

###################################################

#lista = [1, "a", 2.5, "b", True]

#numeros = [x for x in lista if isinstance(x, (int, float)) and not isinstance(x, bool)]
#strings = [x for x in lista if isinstance(x, str)]
#print(numeros, strings)

###################################################

#lista = [1, "a", 2.5, [], {}, 10]

#inteiros = sum(1 for x in lista if isinstance(x, int))
#strings = sum(1 for x in lista if isinstance(x, str))
#lista2 = sum(1 for x in lista if isinstance(x, list))

#print(inteiros)
#print(strings)
#print(lista2)

###################################################

#lista = [1, "a", 2, "b"]

#transformacao = [str(x) if isinstance(x, int) else x for x in lista]

#print(transformacao)

###################################################

#lista = [1, "2", 3.0, "texto", 4]

#numeros = [x for x in lista if isinstance(x, (int, float)) and not isinstance(x, (bool, str))]
#print(numeros)

###################################################

#lista = [1, "2", 3.0, "4", 5]

#numeros = [int(x) if isinstance(x, str) else x for x in lista]
#print(numeros)

###################################################0000000000000000000000000000000000000000000000000000000000000000000000000000000

#n1 = int(input('Digite um numero: '))
#n2 = int(input('Digite outro numero: '))
#n3 = int(input('Digite mais um numero: '))

#if n1 > n2 > n3:
#    print(f'{n1} é maior!')

#elif n1 < n2 > n3:
#    print(f'{n2} é maior!')

#else:
#    print(f'{n3} é maior!')

###################################################

#numeros = []

#for i in range(5):
#    numero = int(input('Digite algum numero: '))
#    if numero % 2 == 0:
#        numeros.append(numero)
#    print(len(numeros))

###################################################
#soma = 0
#numeros = 1

#while numeros != 0:
#    numeros = int(input('Digite qualquer numero (0 para parar): '))
#    soma += numeros
#print('Soma total', soma)

###################################################

#numero_secreto = 5

#while True:
#    palpite = int(input('Digite um número:'))
    
#    if palpite == numero_secreto:
#        print('Você acertou!')

#    else:
#        print('Você errou, tente novamente.')

###################################################

#palavra = 'Phyton'
#vogais = 'aeiou'
#contador = 0

#for letra in palavra:
#    if letra in vogais:
#        contador += 1
#print(contador)

###################################################

#soma = 0
#quantidade = 0

#while True:
#    nota = float(input('Digite a nota (-1 para parar): '))

#    if nota == -1:
#        break

#    soma += nota
#    quantidade += 1

#media = soma / quantidade

#print('Media', media)
#print('Quantidade de alunos', quantidade)

###################################################

#numero = 0
#while numero <= 9:
#    numero += 1
#    print(numero)

###################################################

#numero = 10
#while numero >= 1:
#    print(numero)
#    numero -= 1

###################################################
    
#contador = 5 

#while contador >= 1:
#    print(contador)
#    contador -= 1

###################################################

#while True:
#    numero = int(input('Digite um numero (0 para parar): '))
#    if numero == 0:
#        break

###################################################

contador = 0
numero = 1 

while numero <= 10:
    if numero % 2 == 0:
        contador += 1
    numero += 1
print('Quantidade de numeros pares', contador)