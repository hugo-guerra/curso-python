#1##########################################

#texto = 'Hugo'
#print(dir(texto))

#2##########################################

#lista = ['Eu', 'Tu', 'Nós', 'Vós']
#print(dir(lista))

#3##########################################

#inteiro = 10
#print(dir(inteiro))

#4##########################################

#texto = "python"
#print(hasattr(texto, "upper"))

#5##########################################

#lista = [1, 2, 3]
#print(hasattr(lista, 'remove_item'))

#6##########################################

#texto = "python"
#if hasattr(texto, 'lower'):
#    print('Tem método lower')
#else:
#    print('Não tem')
    
#7##########################################

#texto = "python"
#metodo = getattr(texto, 'upper')
#print(metodo())

#8##########################################

#lista = [1, 2, 3]
#atributo = getattr(lista, 'tamanho', 'Não existe')
#print(atributo)

#9##########################################

#texto = "python"
#metodo = "upper"
#print(getattr(texto, metodo)())

#10##########################################

#texto = "python"
#metodo = "capitalize"
#if hasattr(texto, metodo):
#    funcao = getattr(texto, metodo)
#    print(funcao())
#else: 
#    print('Não existe')

#11##########################################

def chamar_metodo(obj, nome_metodo):
    if hasattr(obj, nome_metodo):
        atributo = getattr(obj, nome_metodo)

        if callable(atributo):
            return atributo()
        else:
            return atributo
    else:
        return 'Não existe'
print(chamar_metodo('python', 'upper'))

#12##########################################

#texto = "python"

#metodo_publico = [ 
#    nome for nome in dir(texto)
#    if not nome.startswith('_')
#]
#print(metodo_publico)

#DESAFIO##########################################

#def executar(obj, nome):
#    if hasattr(obj, nome):
#        atributo = getattr(obj, nome)

#        if callable(atributo):
#            return atributo()
#        else: 
#            return atributo
#    else: 
#        return "Não encontrado"

#print(executar('python', 'upper'))