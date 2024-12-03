import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo de execução: {end_time - start_time} segundos")
        return result
    return wrapper

@measure_time
def binary_search(lista, item, beagin=0, end=None):
    if end is None:
        end = len(lista) - 1
    if beagin <= end:
        meio = (beagin + end) // 2
        if lista[meio] == item:
            return meio
        if item < lista[meio]:
            return binary_search(lista, item, beagin, meio - 1)
        else:
            return binary_search(lista, item, meio + 1, end)
    return None

# def binary_search(lista, item, beagin=0, end=None):
#     if end is None:
#         end = len(lista) - 1
#     if beagin <= end:
#         meio = (beagin + end) // 2
#         if lista[meio] == item:
#             return meio
#         if item < lista[meio]:
#             return binary_search(lista, item, beagin, meio - 1)
#         else:
#             return binary_search(lista, item, meio + 1, end)
#     return None

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if binary_search(lista, 11) is not None:
    print('Encontrado')
else:
    print('Não encontrado')