# Acumulador
'''
n = int(input())
soma = 0
for i in range(1, n+1):
    soma = soma+i
print(soma)
'''

# Tabuada
'''
n = int(input())
for i in range(1,11):
    print("{} x {} = {}".format(i, n, i*n))
'''

# Somatório
'''
n = int(input())
somatorio = 0
for i in range(1, n+1):
    somatorio = somatorio + (1/i)
print("{:.4f}".format(somatorio))
'''

# Múltiplos
'''
a, b = map(int, input().split())
multiplos = 0
for i in range(1, (b//a)+1):
    multiplos = a*i
    print(multiplos, end=" ")
'''

# Divisores
'''
n = int(input())
divisores = 0
for i in range(1, n+1):
    if n%i==0:
        divisores = i
        print(divisores, end=" ")
'''

# Media
'''
n = int(input())
valores = list(map(int, input().split()))
soma = sum(valores)
media = soma/n
menor = 0
maior_igual = 0

for i in range(len(valores)):
    if valores[i] < media:
        menor = menor + 1
    else:
        maior_igual = maior_igual + 1

print("{:.1f}".format(media))
print(menor)
print(maior_igual)
'''

# Game Show
'''
c = int(input())
valor_inicial = 100
maior_p = 100
    
for i in range(1, c+1):
    v = int(input())
    valor_inicial += v
    
    if valor_inicial > maior_p:
        maior_p = valor_inicial
    
print(maior_p)
'''

# Desvendando Monty Hall
'''
n = int(input())
w = 0

for i in range(1, n+1):
    porta = int(input())

    if porta == 2 or porta == 3:
        w += 1

print(w)
'''

