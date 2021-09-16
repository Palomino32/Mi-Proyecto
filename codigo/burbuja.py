lista = [3,4,2,1]
n = len(lista)
for i in range(n):
    for j in range(n-1):  
        if(lista[j] < lista[j+1]):
            aux = lista[j+1]
            lista[j+1] = lista[j]
            lista[j] = aux
print(lista)           