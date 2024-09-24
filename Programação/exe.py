a, b, c, d = map(int, input().split())

menor_par = a

if b%2==0 and (b<menor_par or menor_par%2!=0):
    menor_par = b
if c%2==0 and (c<menor_par or menor_par%2!=0):
    menor_par = c
if d%2==0 and (d<menor_par or menor_par%2!=0):
    menor_par = d
if menor_par%2!=0:
    menor_par = 0
print(menor_par)
