import random
from aula1 import BinarySearchTree


random.seed(77)

def random_tree(size=42):
    values = random.sample(range(1, 1000), size)
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def exemple_tree():
    values = [45, 23, 89, 12, 67, 34, 78, 56, 90, 11, 38, 72]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def extend_tree():
    values = [45, 23, 89, 12, 67, 34, 78, 56, 90, 11, 38, 72, 100, 90]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

bst = exemple_tree()
bst.inorder_traversal()

# Testar remoção da Arvore
print("\n", "_"* 40)
v = 67
bst.remove(v)
print(f"Apos remover o valor {v}")
bst.inorder_traversal()
print('\n')

# Testar Percuso por nivel na Arvore
# print('')
bst.levelorder_traversal()
print('\n')
print('_'*40)
# Testar Maximo e minimo da Arvore
print(f'Máximo: ', bst.max())
print(f'Minimo: ', bst.min())
# items = [1,3,981,510,1000]
# for item in items:
#     r = bst.search(item)
#     if r is None:
#         print(f"{item} não encontrado")
#     else:
#         print(f"{r.root.data} Encontrado")