# Complexidade e uma medida de recursos demanddos por um algoritmo
# Sendo ela de espaço ou tempo


def inverter_lista(lista):
    tamanho = len(lista)
    limite = tamanho // 2
    for i in range(limite):
        aux = lista[i]
        lista[i] = lista[i - 1]
        lista[tamanho - i] =  aux

# 4 + N memoria - Complexidade de espaço
# 4 variaveis + 1 lista com N valores de memorias

# Operções elementares
# 2 + 4*limite(N/2) - complexidade de tempo = O(N)
# 2 termo irrelevante
# 4* termo irrelevante
# limite(N/2) = N/2 termo dominante

def inverter_lista2(lista):
    nova_lista = []
    tamnho = len(lista)
    for i in range(tamnho):
        nova_lista.append(lista[tamnho - i])
    return nova_lista

# 2 + N memoria - Complexidade de espaço
# 3 + 2*N - complexidade de tempo

def tem_duplicados(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(i + 1, tamanho):
            if lista[i] == lista[j]:
                return True
    return False

# complexidade de tempo: N - 1 + N-2 + N-3 + ... + 1 = N*(N-1)/2
# (N^2 - N)/2 + 1 = O(N^2)
# 	                                                                                                             