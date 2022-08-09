a = []

print('digite 3 números')
n1 = a.append(int(input()))
n2=  a.append(int(input()))
n3 = a.append(int(input()))



menor = min(a)
maior = max(a)
do_meio = sum(a) - min(a) - max(a)


print('menor = {}, do meio = {}, maior = {} '.format(menor, do_meio, maior))