#for i in range(1, 11):
#    print(i)

###############################################

#for i in range(1, 21):
#    if i % 2 == 0:
#        print(i)

###############################################

#soma = 0

#for i in range(1, 101):
#    soma += i

#print(soma)

###############################################

#palavra = input('Digite uma palavra: ')

#for letra in palavra:
#    print(letra)

###############################################

#palavra = input('Digite uma palavra: ')

#contador = 0

#for i in palavra:
#    contador += 1

#print('Número de letras: ', contador)

###############################################

#numero = int(input('Digite um número: '))

#for i in range(1, 11):
#    print(numero, 'x', i, '=', numero * i)

###############################################

#numeros = [2, 4, 6, 8]
#soma = 0 

#for numero in numeros:
#    soma += numero
    
#print(soma)

###############################################

#numeros = [10, 5, 22, 8, 17]

#maior = numeros[0]

#for numero in numeros:
#    if numero > maior:
#        maior = numero

#print(maior)

###############################################

#palavra = input('Digite uma palavra: ')

#vogais = 'aeiou'
#contador = 0

#for letra in palavra:
#    if letra in vogais:
#        contador += 1

#print('Quantidade de vogais:', contador)

###############################################

#quadrado = []

#for i in range(1, 11):
#    quadrado.append(i ** 2)

#    print(quadrado)

################################################33333333333333333333333333333333333333333333333333333

#def impar_ou_par(numero): 
#    if numero % 2 == 0:
#        print('Par')
#    else:
#        print('Impar')
#num = int(input('Digite um numero qualquer: '))
#impar_ou_par(num)

################################################

#def maior_numero(lista):
#    maior = lista[0]

#    for numero in lista:
#        if numero > maior:
#            maior = numero
#    return maior



#print(maior_numero([10, 5, 30, 2]))

################################################

#def maior_zero(lista):
#    contador = 0

#    for numero in lista:
#        if numero > 0:
#            contador += 1
#    return contador
            
#print(maior_zero([-1, 2, 0, 5, -3])) 

################################################

#def validar_numero(n):
#    tipo_n = type(n)
#    if not isinstance(n,(int, float)):
#        raise TypeError("O valaor não é INT e nem FLOAT!")
#    return True
#print(validar_numero(5))

################################################
#dados = ["10", "abc", "20", "x", "30"]
#def soma(lista):
#    soma = 0

#    for item in lista:
#        try:
#            numero = int(item)
#            soma += numero
#        except ValueError:
#            pass

#    return soma
#print(soma(dados))

################################################

#from datetime import datetime

#dia = datetime.today().strftime('%d/%m')

#if dia == '01/04':
#    print('Nunca deixei de revisar o codigo da IA')

################################################

#def validar_senha(senha):
#    if len(senha) < 6:
#        raise ValueError('A senha deve conter mais de 6 digitos')
    
#    return True

#print(validar_senha('123456'))

################################################

#def sacar(saldo, valor):

#    if valor <=0:
#      raise ValueError('Valor deve ser maior que zero')
    
#    if valor > saldo:
#       raise ValueError('Saldo insuficiente')
    
#    saldo = saldo - valor
#    return saldo
#print(sacar(1000, 200))

################################################8888888888

#def saudacao(nome):
#    print(f'Olá, {nome}')
#saudacao('Hugo Guerra')

################################################

#numero = 1 

#while numero <= 20:
#    if numero % 2 == 0:
#        print(numero)
#    numero += 1

################################################


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print(f'A media do aluno é: {media}, ele está apreovado!')
else:
    print(f'A media do aluno é: {media}, ele esta reprovado!')