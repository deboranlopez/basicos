def bubblesort(lista):
    cantidad = len(lista) - 1
    for i in range(0,cantidad):
        hubo_swap = False
        for j in range(0, cantidad):
            if lista[j]>lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                hubo_swap = True
        if hubo_swap is False:
            return lista
    return lista

una_lista = [2, 1, 3, 5, 8, 3, 9]
print(una_lista)

print(bubblesort(una_lista))