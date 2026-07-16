# Atividade 1
#numero_inteiro = input('Digite um número inteiro: ')

#try:
#    int_numero = int(numero_inteiro)

#    if int_numero % 2 == 0:
#        print(f'O {numero_inteiro} é par!')
#    else:
#        print(f'O {numero_inteiro} é ímpar!')

#except ValueError:
#    print('O valor digitado não é um número inteiro!')

# Atividade 2

#horario = input('Quantas horas são? ')


#try:
#    horario_atual = float(horario)

#    if 0 <= horario_atual < 11:
#       print('Bom dia!')
#    elif 12 <= horario_atual < 17:
#       print('Boa tarde!')
#    else:
#        print('Boa noite!')
#except:
#    ...

# Atividade 3

nome = input('Qual é o seu primeiro nome? ')

if 0 <= len(nome) <= 4:
    print('Seu nome é curto!')

elif 5 <= len(nome) <= 6:
    print('Seu nome é normal!')

else:
    print('Seu nome é muito grande!')
    