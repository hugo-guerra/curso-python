#i = 1

#while i <= 10:
#    print(i)
#    i += 1
######################################################

#i = 1

#while i <= 20:
#    if i % 2 == 0:
#        print(i)
#    i += 1

######################################################

#i = 1
#soma = 0

#while i <= 100:
#    soma += i
#    i += 1
#print(soma)

######################################################

#i = 10

#while i >= 1:
#    print(i)
#    i -= 1

######################################################

#senha = input('Digite a senha: ')

#while senha != "1234":
#    print('A senha esta incorreta!')
#else:
#    print('A senha está coreta!')
    
#senha = ""

#while senha != "1234":
#    senha = input("Digite a senha: ")

#print("Senha correta!") 

######################################################

#soma = 0 
#numero = 1

#while numero != 0:
#    numero = int(input('Digite um número (0 para parar): '))
#    soma += numero

#print('Soma total: ', soma)

######################################################

#pessoa = {
#    'nome' : 'Hugo',
#    'altura' : '1.8',
#}

#dados_pessoas = {
#    'idade' : 22,
#    'sobrenome' : 'Guerra',
#}

#pessoa_completa = {**pessoa, **dados_pessoas}
#print(pessoa_completa)

x = (1, 2, [3, 4])
x[2].append(5)
print(x)