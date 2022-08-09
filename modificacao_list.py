numeros = [5, 10]

numeros.append(20) # insere 20 no final: [5, 10, 20]
numeros.append(10) # insere 10 no final: [5, 10, 20, 10]
numeros.insert(2,15) # insere 15 na posição 2: [5, 10, 15, 20, 10]
numeros.insert(0,10) # insere 10 na posição 0: [10, 5, 10, 15, 20, 10]

numeros.pop() # remove o último elemento: [10, 5, 10, 15, 20]
numeros.pop(3) # remove o quarto elemento: [10, 5, 10, 20]
numeros.remove(10) # remove o primeiro 10: [5, 10, 20]
numeros.extend([40, 50]) # estende a lista: [5, 10, 20, 40, 50]

print(numeros)

del numeros[1:3] # com del posso apagar 1 ou mais elementos: [5, 40, 50]
numeros.clear() # esvazia a lista: [ ]
