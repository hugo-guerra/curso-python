#numeros = [1, 2, 3, 4]

#dc = {n : n ** 2 for n in numeros}
#print(dc)

######################################

#numeros = [1, 2, 3, 4]

#dc = {n : n * 2 for n in numeros}
#print(dc)

######################################

#palavras = ["python", "java", "c"]

#dc = {p: len(p) for p in palavras}
#print(dc)

######################################

#numeros = [1, 2, 3, 4, 5]

#dc = {n for n in numeros if n % 2 == 0}
#print(dc)

######################################

#palavras = ["python", "go", "javascript"]

#dc = {p: len(p) for p in palavras if len(p) > 4}
#print(dc)

######################################

#numeros = [1, 2, 3, 4]

#dc = {n : 'par' if n % 2 == 0 else 'impar' for n in numeros}
#print(dc)

######################################

#d = {"a": 1, "b": 2, "c": 3}

#dc = {valor : chave for chave, valor in d.items()}
#print(dc)

##   SET    ####################################

#numeros = [1, 2, 2, 3, 3, 4]

#s1 = {n for n in numeros}
#print(s1)

######################################

#numeros = [1, 2, 2, 3, 3, 4]

#s1 = {n ** 2 for n in numeros}
#print(s1)

######################################

#numeros = [1, 2, 3, 4, 5, 6]

#s1 = {n for n in numeros if n % 2 == 0}
#print(s1)

######################################

#palavras = ["python", "java", "c", "go"]

#s1 = {p: len(p) for p in palavras}
#print(s1)

######################################

#palavra = "programacao"

#s1 = {p for p in palavra}
#print(s1)

######################################

numeros = [1, 2, 3, 4, 5, 6]

s1 = {n : n ** 2 for n in numeros if n % 2 == 0}
print(s1)