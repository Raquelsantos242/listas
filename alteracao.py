lst = ['John', 'Yoko', 'Julian', 'Sean']
print('Lista Original: ', lst)

lst[1] = 'Yoko Ono'
lst[0] = 'John Lennon'
print('Lista alterada: ', lst)

#modificando vários de uma vez
lst[1:4] = ['Paul', 'George', 'Ringo']
print('lista alterada de novo: ', lst)