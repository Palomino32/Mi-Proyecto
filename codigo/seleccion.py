lista = [4,7,9,5,2]
n = len(lista)
for a in range(n):
    for b in range(a+1,n):
        if(lista[a]>lista[b]):
            aux = lista[a]
            lista[a] = lista[b]
            lista[b] = aux
print(lista)