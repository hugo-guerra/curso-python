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
#lista = [n for n in range(10) if n < 5]
#print(lista)

#import pprint

#def p(v):
    #pprint.pprint(v, sort_dicts=False, width=40)


#produtos = [
#    {'nome': 'p1', 'preco': 20, },
#    {'nome': 'p2', 'preco': 10, },
#    {'nome': 'p3', 'preco': 30, },
#]

#novos_produtos= [
#    {**produto, 'preco': produto['preco'] * 1.05}
#    if produto['preco'] > 20 else {**produto}
#    for produto in produtos
#    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
#]
#p(novos_produtos)
#print(novos_produtos)

###########################################################################


#idade = int(input('Qual é a sua idade? '))
#lista = []
#if idade > 18:
#    lista.append(idade) 
#    print(lista)

###########################################################################

#numero = int(input("Digite um numero: "))

#if numero % 2 == 0:
#    print("Par")
#else:
#    print("Impar")

###########################################################################

#numeros = []

#while True:
#    n = int(input("Digite um numero (0 para parar): "))

#    if n == 0:
#        break

#    numeros.append(n)

#print("Maior: ", max(numeros))
#print("Menor: ", min(numeros))

#pares = 0

#for numero in numeros:
#    if numero % 2 == 0:
#        pares += 1

#print("Quantidade de pares: ", pares)

###########################################################################

#while True:
#    print("1 - Somar")
#    print("2 - Sair")

#    opcao = input("Escolha: ")

#    if opcao == "1":
#        print("Somando... ")
#    elif opcao == "2":
#        break

###########################################################################

#while True:
#    n = int(input('Digite um numero: '))

#    if n % 2 == 0:
#        print('Par')
#    else:
#        print('Impar')
#        break

###########################################################################
#numeros = ()
#for numeros in range(1, 11):
#    print(numeros)

###########################################################################

#for numeros in range(0, 22, 2):
#    print(numeros)

###########################################################################

#soma = 0

#for i in range(1, 6):
#    numero = int(input('Digite um numero: '))
#    soma = soma + numero
#print('Soma: ', soma)

###########################################################################

#for i in range(5):
#    numero = int(input('Digite um numero: '))
#    if numero >= 10:
#        pass

#print('São maiores que 10: ', numero)

###########################################################################

#pessoa = {
#    "nome": "João",
#    "idade": 20,
#    "cidade": "São Paulo"
#}

#for chave, valor in pessoa.items():
#    print(chave, ":",valor)

###########################################################################

#idades = (15, 20, 17, 25, 30)

#contador = 0

#for idade in idades:
#    if idade > 18:
#        contador += 1

#print("Maiores de idade:", contador)

###########################################################################

#numeros = [5, 12, 3, 20, 8, 100]

#maior = numeros[0]

#for numero in numeros:
#    if numero > maior:
#        maior = numero

#print("Maior número:", maior)

###########################################################################

#pessoas = {
#    "Ana": 17,
#    "João": 22,
#    "Carlos": 15,
#    "Maria": 30
#}

#for nome, idade in pessoas.items():
#    if idade >= 18:
#        print(nome, "é maior de idade")

###########################################################################

#for i in range(1, 6):
#    for j in range(1, 11):
#        print(i, "x", j, "=", i * j)

#    print()

###########################################################################

#palavra = "pneumoultramicroscopicossilicovulcanoconiótico"

#contador = 0

#for letra in palavra:
#    contador = contador + 1

#print("Quantidade de letras:", contador)

###########################################################################

#senha_correta = "1234"

#for tentativa in range(3):
#    senha = input("Digite a senha: ")

#    if senha == senha_correta:
#        print("Acesso permitido")
#        break
#    else:
#        print("Senha errada")

#else:
#    print("Conta bloqueada")

###########################################################################

#soma = 0
#numero = 1

#while numero != 0:
#    numero = int(input("Digite um número: "))

#    soma += numero

#print("Soma:", soma)

###########################################################################

#senha = ""

#while senha != "1234":
#    senha = input("Digite a senha: ")

#print("Acesso permitido")

###########################################################################

#while True:
#    numero = int(input("Digite um número: "))

#    if numero == 0:
#        break

#    print("Você digitou:", numero)

###########################################################################

#numero = -1

#while numero < 0:
#    numero = int(input("Digite um número positivo: "))

###########################################################################

#contador = 0

#while contador < 5:
#    print("Executando...")
#    contador = contador + 1

###########################################################################

#soma = 0
#numero = 1

#while numero <= 5:
#    soma = soma + numero
#    numero = numero + 1

#print(soma)

###########################################################################


#numero = -1

#while numero < 0:
#    numero = int(input("Digite um número positivo: "))

###########################################################################

#i = 1

#while i <= 3:

#    j = 1

#    while j <= 2:
#        print(i, j)
#        j = j + 1

#    i = i + 1

###########################################################################

#tentativas = 0

#while tentativas < 3:

#    senha = input("Digite a senha: ")

#    if senha == "1234":
#        print("Acesso permitido")
#        break

#    tentativas = tentativas + 1

#if tentativas == 3:
#    print("Conta bloqueada")

###########################################################################

#idade = 0

#while idade < 18 or idade > 100:
#    idade = int(input("Digite uma idade válida: "))

###########################################################################

#numero = int(input("Digite um número: "))

#if numero > 0:
#    print("Positivo")

#elif numero < 0:
#    print("Negativo")

#else:
#    print("Zero")

###########################################################################

#idade = int(input('Qual é a sua idade? '))
#tem_carteira = str(input('Tem carteira? [S/N] '))

#if idade >= 18:

#    if tem_carteira == 'S':
#        print("Pode dirigir")

#    else:
#        print("Não pode dirigir")

#else:
#    print("Menor de idade")

###########################################################################

#while True:

#    numero = int(input("Digite um número: "))

#    if numero == 0:
#        print("Saindo... ")
#        break

#    print("Número digitado:", numero)

###########################################################################

#ano = int(input("Digite um ano: "))

#if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#    print("Ano bissexto")
#else:
#    print("Ano normal")

###########################################################################

#numero = int(input("Digite um número: "))

#if 10 <= numero <= 20:
#    print("Está no intervalo")

#else:
#    print("Fora do intervalo")

###########################################################################

#pessoa = {
#    'nome': 'Hugo',
#    'sobrenome': 'Guerra',
#    'idade': 22,
#    'altura': 1.8,
#    'endereços': [
#        {'rua': 'tal tal', 'número': 123},
#        {'rua': 'outra rua', 'número': 321},
#    ],
#}
# print(pessoa, type(pessoa))
#print(pessoa['nome'])

###########################################################################

#try:
#    numero = int(input("Digite um número: "))
#    print(numero)

#except:
#    print("Você digitou algo inválido")

###########################################################################

#try:
#    resultado = 10 / 0
#    print(resultado)

#except ZeroDivisionError:
#    print("Não pode dividir por zero")

###########################################################################

#try:
#    numero = int(input("Digite um número: "))

#except ValueError:
#    print("Digite apenas números")

###########################################################################

#try:
#    numero = int(input("Digite um número: "))

#except ValueError:
#    print("Erro")

#else:
#    print("Número digitado:", numero)

###########################################################################

#while True:

#    try:
#        numero = int(input("Digite um número: "))
#        break

#    except ValueError:
#        print("Digite apenas números")

###########################################################################

#try:
#    a = int(input("Digite o primeiro número: "))
#    b = int(input("Digite o segundo número: "))

#    resultado = a / b

#except ValueError:
#    print("Digite apenas números")

#except ZeroDivisionError:
#    print("Não pode dividir por zero")

#else:
#    print("Resultado:", resultado)

#finally:
#    print("Fim do programa")

###########################################################################

#import json

#pessoa = {
#    "nome": "Hugo",
#    "idade": 25
#}

#json_texto = json.dumps(pessoa)

#print(json_texto)

###########################################################################

#def mostrar_nome(nome):
#    print("Seu nome é:", nome)

#mostrar_nome(input("Digite o seu nome: "))

###########################################################################

#def somar(a, b):
#    print(a + b)

#somar(5, 3)

###########################################################################

#def somar(a, b):
#    resultado = a + b
#    return resultado

#resposta = somar(5, 3)

#print(resposta)

###########################################################################

#def pedir_numero():

#    while True:

#        try:
#            numero = int(input("Digite um número: "))
#            return numero

#        except ValueError:
#            print("Digite apenas números")

#pedir_numero()

###########################################################################

#def somar_lista(lista):

#    soma = 0

#    for numero in lista:
#        soma = soma + numero

#    return soma

#numeros = [1, 2, 3, 4]

#resultado = somar_lista(numeros)

#print(resultado)

###########################################################################

#def calcular(a, b):

#    soma = a + b
#    multiplicacao = a * b

#    return soma, multiplicacao

#s, m = calcular(5, 3)

#print(s)
#print(m)

###########################################################################

#def externo():

#    def interno():
#        print("Função interna")

#    interno()
#externo()

###########################################################################

#def calcular_media(n1, n2):

#    media = (n1 + n2) / 2

#    if media >= 7:
#        return "Aprovado"

#    else:
#        return "Reprovado"
    
#resultado = calcular_media(8, 6)

#print(resultado)

###########################################################################

#def pedir_idade():

#    while True:

#        try:
#            idade = int(input("Digite a idade: "))

#            if idade >= 0:
#                return idade

#            else:
#                print("Idade inválida")

#        except ValueError:
#            print("Digite um número")
#pedir_idade()

###########################################################################

#def menu():

#    print("1 - Somar")
#    print("2 - Sair")

#    opcao = input("Escolha: ")

#    return opcao


#def somar():

#    try:
#        a = int(input("Digite o primeiro número: "))
#        b = int(input("Digite o segundo número: "))

#        return a + b

#    except ValueError:
#        print("Digite apenas números")
#        return None


#while True:

#    escolha = menu()

#    if escolha == "1":

#        resultado = somar()

#        if resultado is not None:
#            print("Resultado:", resultado)

#    elif escolha == "2":
#        break

#    else:
#        print("Opção inválida")

###########################################################################

#def validar_email(email):

#    email = email.strip()

#    if "@" in email and "." in email:
#        return True
#    else:
#        return False
    
#if validar_email("teste@gmail.com"):
#    print("Email válido")
#else:
#    print("Email inválido")

###########################################################################

#def calcular_media(notas):

#    if len(notas) == 0:
#        return 0

#    soma = sum(notas)

#    media = soma / len(notas)

#    return media

#notas = [7, 8, 9]

#print(calcular_media(notas))

###########################################################################

#def remover_repetidos(lista):

#    nova_lista = []

#    for item in lista:

#        if item not in nova_lista:
#            nova_lista.append(item)

#    return nova_lista

#numeros = [1, 2, 2, 3, 4, 4, 5]

#print(remover_repetidos(numeros))

###########################################################################

#email = input("Digite o email: ")

#if email.lower() == "admin@gmail.com":
#    print("Acesso permitido")

###########################################################################

#frase = "Python é muito bom"

#palavras = frase.split()

#print(palavras)

###########################################################################

#numeros = [1, 2, 3]

#numeros.remove(2)

#print(numeros)

###########################################################################

#pessoa = {
#    "nome": "João",
#    "idade": 25
#}
#print(pessoa.keys())

###########################################################################

#a, b, c = map(int, input().split())

#print(a, b, c)

###########################################################################

#a = [11, 22, 33, 44, 55, 66]
#for i in a:
#    a.remove(i)
#print(i)

###########################################################################

#matriz = []

#for i in range(5):

#    linha = []

#    for j in range(5):

#        linha.append(0)

#    matriz.append(linha)

#print(matriz)

###########################################################################

#class Conta:

#    def __init__(self, saldo):
#        self.__saldo = saldo

#    def ver_saldo(self):
#        return self.__saldo
    
###########################################################################

#class Pessoa:

#    def __init__(self, nome):
#        self.nome = nome

#    def falar(self):
#        print(self.nome, "está falando")

#print(Pessoa.__init__)

###########################################################################

#class Conta:

#    def __init__(self, saldo):
#        self.__saldo = saldo

#    def get_saldo(self):
#        return self.__saldo

#    def set_saldo(self, valor):
#        self.__saldo = valor

#conta = Conta(100)

#conta.set_saldo(500)

#print(conta.get_saldo()) 

###########################################################################

#numero_secreto = 8

#while True:

#    valor_chutado = int(input('Digite um valor: '))

#    if valor_chutado > numero_secreto:
#        print('Tente novamente, o valor chutado é maior!')

#    if valor_chutado < numero_secreto:
#        print('Tente outra vez, o valor é muito baixo!')

#    if valor_chutado == numero_secreto:
#        print('Parabens, você acertou em cheio!')
#        break
    
###########################################################################

#numero = int(input('Digite um número: '))

#fatorial = 1

#if numero <= 0:
#    print('Digite somente numeros inteiros positivos!')

#while numero > 0:
#    fatorial *= numero
#    numero -= 1
#print(f'Fatorial é {fatorial}')

###########################################################################

#idades = [15, 46, 75, 34, 23]
#total = 0

#for idade in idades:
#    total += idade
#print(total)

###########################################################################

#salario_mensal = float(input('Qual é o seu salario? R$'))
#horas_trabalhadas = float(input('Quantas horas você trabalha? '))

#valor_hora = salario_mensal / horas_trabalhadas

#print(valor_hora)

###########################################################################

#p1 = int(input('Qual é o primeiro valor: '))
#p2 = int(input('Qual é o segundo valor: '))

#if p1 > p2:
#    print(f'O primeiro valor {p1} é maior que o segundo valor {p2}.')
#elif p1 < p2:
#    print(f'O segundo valor {p2} é maior que o primeiro valor {p1}.')
#else:
#    print('Os dois valores são iguais.')

###########################################################################

#idades = [13, 15, 18, 30, 50, 75]

#for idade in idades:
#    if idade >= 18:
#        print(f'{idade} é maior de idade.')
#    else:
#        print(f'{idade} é menor de idade.')

###########################################################################

#senhas = ['abc', 'segura123', '12345', 'python123', 'oi']

#for senha in senhas:
#    if len(senha) >= 6:
#        print(f'{senha} é maior que 6')
#    else:
#        print(f'{senha} é menor que 6')

###########################################################################

#tentativas = 0

#while tentativas < 3:
#    print('Tente novamente')
#    tentativas += 1

###########################################################################

#senha = ''

#while senha != '123456':
#    senha = input('Digite a senha correta: ')

#print('Bem-vindo ao sistema')

###########################################################################

#nome = ''
#while nome == '':
#    nome = input('Digite seu nome: ')

#print(f'Bem-vindo {nome}')

###########################################################################

#horario = 0
#while horario <= 17:
#    print(horario)
#    horario += 1
#print('Hora de ver o por do sol!')

###########################################################################

#usuario = ''
#senha = ''
#tentativas = 0

#while (usuario != 'Hugo' or senha != 'senha123') and tentativas < 3:
#    usuario = input('Digite seu usuario: ')
#    senha = input('Digite a sua senha: ')
#    tentativas += 1

#if usuario == 'Hugo' and senha == 'senha123':
#    print('Login feito com sucesso.')
#else:
#    print('Favor aguardar 30 min, para tentar novamente.')

###########################################################################

#precos = [20, 50, 100]
#print(precos[0]) #acessando por indice

#nomes = ['Brasil', 'EUA', 'Mexico']
#print(nomes[1]) #acessando por indice

#Encontrar indice automaticamnete
#print(nomes.index('EUA'))

# Manipulando - add novos itens 
#salarios = [2500, 5000, 7000]
#salario_usuario = float(input('Qual é o seu salario? R$'))
#salarios.append(salario_usuario)
#print(salarios)

#salarios = [2500, 900, 5000, 7500]
#total = 0
#for salario in salarios:
    # 2500 -> 2500 + 900 -> 3400 + 5000 -> 8400 + 7500 -> 15900
#    total += salario 
#print(total)

###########################################################################

#numero = int(input('Digite um número: '))

#if numero > 0 and type(numero) == int:
#    fatorial = 1

#    for item in range(1, numero + 1):
#        print(f'{fatorial} * {item}')
#        fatorial *= item
#        print(f'{fatorial}')
#    print(f'O fatorial de {numero} é {fatorial}')
#else:
#    print('Favor informar apenas números inteiros positivos!')

###########################################################################

#import random

#valor_aleatorio = random.randint(1, 10)
#acertou = False

#while acertou == False:
#    chute = int(input('Chute um numero: '))

#    if chute > valor_aleatorio:
#        print('Tente novamente, o chute foi muito alto!')
#    elif chute < valor_aleatorio:
#        print('Tente novamente, o chute foi muito baixo!')
#    else:
#        print('Parabens, você acertou em cheio!')
#        acertou = True

###########################################################################

# Medidor de velocidade

#velocidade = float(input('Digite a velocidade: '))
#velocidade_maxima = 80

#if velocidade <= velocidade_maxima:
#    print('Não houve multa!')
#elif velocidade <= velocidade_maxima + 10:
#    print('Leveou multa leve!')
#elif velocidade <= velocidade_maxima + 20:
#    print('Levou multa grave!')
#else:
#    print('Levou multa gravíssima!')

###########################################################################

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()