escritores = ['José Saramago', 'George Orwell', 'Jane Austen', 'Joarge Amado']

seq_fibonacci = [0, 1, 1, 2 , 3, 5, 8, 13, 21, 34, 55]

lista_vazia = []
lista_vazia2 = list()

lista_mista = ['Pen Drive', 25.90, 'Laptop', 2690]

m = [ [1, 2, 3], [4, 5, 6]  ]

print(escritores)
print(seq_fibonacci)
print(lista_vazia)
print(lista_mista)
print(m)

import pprint
pp = pprint.PrettyPrinter(width=15, compact=True)
pp.pprint(m)
