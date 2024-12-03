import random
# print(minimo)

def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partion(lista, inicio, fim)
        quicksort(lista, inicio, p-1)
        quicksort(lista, p + 1, fim)

def partion(lista, inicio, fim):
    pivo = lista[fim]
    barra_amarela = inicio
    for barra_roxa in range(inicio, fim):
        if lista[barra_roxa] <= pivo:
            lista[barra_roxa], lista[barra_amarela] = lista[barra_amarela], lista[barra_roxa]
            barra_amarela += 1
    lista[barra_amarela], lista[fim] = lista[fim], lista[barra_amarela]
    return barra_amarela


def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)


def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1
# Complexidade de tempo O(n log n)

def insertion_sort(lista):
    n = len(lista)
    for i in range(1,n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chave
    print(lista)
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print(lista)
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)

def selection_sort(lista):
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
    print(lista)
# 1 + (n-1)*[5 + X] = 1 + 5*(n-1) + X*(n-1)
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)

lista_aleatoria = random.sample(range(1,100), 42)

lista_inverted = [116,
115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73]

repeat = [6,4,4,5,5,9,7,7]

# selection_sort(lista_aleatoria)
# selection_sort(lista_inverted)
# selection_sort(repeat)

# bubble_sort(lista_aleatoria)
# bubble_sort(lista_inverted)
# bubble_sort(repeat)                                                                                             

# insertion_sort(lista_aleatoria)
# insertion_sort(lista_inverted)
# insertion_sort(repeat)

# mergesort(lista_aleatoria)
# mergesort(lista_inverted)
# mergesort(repeat)

quicksort(lista_aleatoria)
quicksort(lista_inverted)
quicksort(repeat)

print(repeat)
print(lista_aleatoria)
print(lista_inverted)