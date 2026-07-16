#import copy
#from dados import produtos

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

#novos_produtos = copy.deepcopy(produtos)

#for produto in novos_produtos:
#    produto['preco'] = produto['preco'] * 1.10

#    produtos_ordenados_por_nome = sorted(
#        copy.deepcopy(produtos),
#        key=lambda produto: produto['nome'],
#        reverse= True
#    )

#    produtos_ordenados_por_preco = sorted(
#        copy.deepcopy(produtos),
#        key=lambda produto: produto['preco']
#    )

#for produto in novos_produtos:
#    print(f'Nome: {produto['nome']} | Preço: R$ {produto['preco']:.2f}')
#print()
#for produto in produtos_ordenados_por_nome:
#    print(f'Nome: {produto['nome']} | Preço: R$ {produto['preco']:.2f}')
#print()
#for produto in produtos_ordenados_por_preco:
#    print(f'Nome: {produto['nome']} | Preço: R$ {produto['preco']:.2f}')

###################################################################################

# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(3))