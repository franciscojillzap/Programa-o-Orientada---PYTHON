dicionario = {}
lista = []
tupla = ()

dicionario = {}
lista = []
dicionario.append(lista)

print(.keys())
print(.values())
print(.items())

print([chave])
print(.get(chave))

for k in dicionario.keys():
    print(k)

for v in dicionario.values():
    print(v)

for k, v in dicionario.items():
    print(f"{k}: {v}")


diciolista1 = list(dicionario.keys())[0]
diciolista2 = list(dicionario.values())[1]
dicio, lista = list(dicionario.items())[2]
