lista = [7,3,4,1,8,5]

def bubble_sort(lista):
    n = len(lista)
    menor_num = 1
    for j in range (n-1):
     for i in range (n-1):
        if lista[i]> lista[i+1]:
    


           lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

mostrar_lista = bubble_sort(lista)
print(mostrar_lista)            