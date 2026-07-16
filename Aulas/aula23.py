# Operador lógico "not"
# Usado para inverter expressões
senha = '123456'
if not senha:
    print('Você não digitou nada')

not True = False
not False = True
senha = input('Senha: ')
print(not True)  # False
print(not False)  # True