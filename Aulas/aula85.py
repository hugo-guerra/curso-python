#lista = [
#    (x, y)
#    for x in range(3)
#    for y in range(3)
#]

#print(lista)

######Em vez de fazer isso######

#numeros = [1, 2, 3, 4, 5]
#novos_numeros = []
#for numero in numeros:
#    novos_numeros.append(numero)

#print(novos_numeros)

############Faça isso###########

#numeros = [1, 2, 3, 4, 5]
#novos_numeros = [numero for numero in numeros]

#print(novos_numeros)

#######################################################

#def divisionHg(x, y):
#    return x / y

#def multiplicationHg(x, y):
#    return x * y

#def quadradoHg(x, y):
#    return x ** y

#numeros = [1, 2, 3, 4, 5]

#division = [divisionHg(numero, 2) for numero in numeros]
#multiplication = [multiplicationHg(numero, 2) for numero in numeros]
#quadrado = [quadradoHg(numero, 2) for numero in numeros]

#print(numeros)
#print(division)
#print(multiplication)
#print(quadrado)

#########################################################################

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#novos_numeros = [numero for numero in numeros if numero > 5]
#impares = [numero for numero in numeros if numero % 2 != 0]
#pares = [numero for numero in numeros if numero % 2 == 0]
#outro_if = [numero if numero != 6 else 600 for numero in pares]

#print(numeros)
#print(novos_numeros)
#print(impares)
#print(pares)
#print(outro_if)

#########################################################################
#for x in range(10):
#    for y in range(5):
#        print(x, y)

#########################################################################

#linha_e_colunas = [ 
#    (x, y)
#    if y != 2 else (x, y * 1000)
#    for x in range(1, 11) 
#    for y in range(1, 6) 
#    if x != 2
#]

#print(linha_e_colunas)

#########################################################################

#string = 'Hugo'
#numero_de_letra = 2
#nova_string = '.'.join([
#    string[indice:indice + numero_de_letra]
#    for indice in range(0, len(string), numero_de_letra)
#])
#print(nova_string)

#########################################################################

nomes = ['Hugo', 'Marilia', 'Rosa']
novos_nomes = [nome[:-1].lower() + nome[-1].upper() for nome in nomes]
print(novos_nomes)