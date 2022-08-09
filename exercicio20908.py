a = ['B', 'A', 'R'. 'R', 'A']

b = [a[k] for k in range(len(a)) if a.count(a[k]) > 1 and k == a.index(a[k])]

print(b)
