"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
#nome = 'Hugo'
#preco = 1000.95897643
#variavel = ''
#print(variavel)


#import hashlib

#texto = "MinhaSenhaSegura"

# Converter para bytes
#dados = texto.encode('utf-8')

# Gerar hash SHA3-512
#hash_sha3_512 = hashlib.sha3_512(dados).hexdigest()

#print("Hash:", hash_sha3_512)



import hashlib

def calcular_hash_arquivo(caminho):
    sha3 = hashlib.sha3_512()

    with open(caminho, "rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(4096), b""):
            sha3.update(bloco)

    return sha3.hexdigest()

hash_arquivo = calcular_hash_arquivo("documento.pdf")

print("SHA3-512:", hash_arquivo)