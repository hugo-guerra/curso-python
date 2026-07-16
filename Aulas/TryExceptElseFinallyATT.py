#try:
#    p1 = int(input('Digite um numero: '))
#    p2 = int(input('Digite outro numero: '))
#    print(p1 / p2)
#except ZeroDivisionError:
#    print('Foi dividido por 0')

#2###################################################

#try:
#    valor = input("Digite um número: ")
#    numero = int(valor)
#    print(numero)

#except ValueError:
#    print('Valor invalido')

#3###################################################

#lista = [10, 20, 30]
#try:
#    print(lista[4])

#except IndexError:
#    print('IndexError')

#4###################################################

#try:
#    a = int(input('Digite um numero: '))
#    b = int(input('Digite outro numero: '))
#    resultado = a / b
#    print(resultado)
#except ZeroDivisionError:
#    print('ZeroDivisionError')
#except ValueError:
#    print('ValueError')

#5###################################################

#try:
#    x = int(input("Digite um número: "))
#    print(x)
#except Exception as e:
#    print('Nome: ',e.__class__.__name__)

#6###################################################

#try:
#    valor = input('Digite um valor: ')
#    numero = int(valor)
#    print('Conversão realizada com sucesso')
#except ValueError:
#    print('Valor invalido')
#else:
#    print('Converção feita com sucesso')

#7###################################################

#try:
#    arquivo = open('arquivo.txt')
#except FileNotFoundError:
#    print('Arquivo não encontrado')
#finally:
#    print('Programa finalizado')

#8###################################################

#arquivo = None

#try:
#    arquivo = open('Arquivo.txt')
#except FileNotFoundError:
#    print('Arquivo não encontrado')
#finally:
#    if arquivo:
#        arquivo.close()
#        print('Arquivo fechado com sucesso')

#9###################################################

#try:
#    valor = input('Digite um numero: ')
#    numro = int(valor)
#    print('Aqui está o numeor', valor)
#except ValueError:
#    print('Erro')
#finally:
#    print('Fim da tentativa')

#10###################################################

#def dividir(a, b):
#    try:
#       resultado = a / b
#       return resultado
#    except ZeroDivisionError:
#        print('Erro, divisão por zero!!')
#    finally:
#        print('Operação finalizada')
#print(dividir(10, 2))

#11###################################################

#def acessar_indice(lista, indice):
#    try:
#        return lista[indice]
#    except IndexError:
#        print('Deu erro')

#lista = [1, 2, 3]
#print(acessar_indice(lista, 0))

#12###################################################

#valores = ["10", "20", "abc", "30"]
#for i in valores:
#    try:
#        resultado = int(i)
#        print(i)
#    except ValueError:
#        print('Valor Invalido')

#Desafio final###################################################

def processar_dados(lista): #recebe a lista
    soma = 0 

    try:
        for item in lista: # Vai percorrer a lista
            try:
                numero = int(item)
                soma += numero
            except ValueError:
                pass
        return soma
    finally:
        print('Processamento concluido')

dados = ["10", "abc", "20", "x", "30"]
print(processar_dados(dados))
        

