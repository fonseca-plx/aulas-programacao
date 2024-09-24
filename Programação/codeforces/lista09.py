# Jogo da estratégia
'''
j,r = map(int, input().split())
pv = list(map(int, input().split()))
somador = 0
vencedor = 1
lista_pontos = []

for c in range(0, j):
    for i in range(c, len(pv), j):
        somador += pv[i]
    lista_pontos.append(somador)
    somador = 0

maior = max(lista_pontos)

for x in range(len(lista_pontos) -1, 0, -1):
    if lista_pontos[x] == maior:
        vencedor = x + 1
        break

print(vencedor)
'''
# Holter
'''
n = int(input())
q = 0
batimentos = []
    
for i in range(1, n+1):
    b = int(input())
    batimentos.append(b)
    
media = sum(batimentos)//len(batimentos)
print(media)
    
for x in range(0, n):
    if batimentos[x] < int(media-(media/10)) or batimentos[x] > int(media+(media/10)):
        q += 1
    
print(q)
'''
# Lampadas
'''
n = int(input())
interruptores = list(map(int, input().split()))
a = 0
b = 0

for i in range(0, n):
    if interruptores[i] == 1:
        if a == 0:
            a = 1
        else:
            a = 0
    else:
        if a == 0 and b == 0:
            a = 1
            b = 1
        elif a == 0 and b == 1:
            a = 1
            b = 0
        elif a == 1 and b == 0:
            a = 0
            b = 1
        else:
            a = 0
            b = 0

print(a)
print(b)
'''
# Enigma
'''
msg = input().upper()
crib = input().upper()
subst = 0
posicoes = 0
    
while len(crib) <= len(msg):
    for i in range(len(crib)):
        if msg[i] == crib[i]:
            subst = 0
            break
        else:
            subst = 1
    
    if subst == 1:
        posicoes += 1
    
    crib = " " + crib
    
print(posicoes)
'''
# Monótonos não triviais maximais
'''
n = int(input())
seq = input()
qtd = 0

lista = seq.split("b")

for i in lista:
    if len(i) >= 2:
        qtd += len(i)
print(qtd)
'''
# Maior número de um algarismo
'''
def soma_algarismos(meio):
    soma_alg = 0
    while meio>=10:
        soma_alg += meio%10
        meio = meio//10
    soma_alg += meio
    return soma_alg
    
n, m = map(int, input().split())
    
while n != 0 or m != 0:
    n1 = soma_algarismos(n)
    n2 = soma_algarismos(m)
    
    while n1>=10:
        n1 = soma_algarismos(n1)
    while n2>=10:
        n2 = soma_algarismos(n2)
    
    if n1 > n2:
        print(1)
    elif n2 > n1:
        print(2)
    else:
        print(0)
    
    n, m = map(int, input().split())
'''
# Flores Florecem da França
'''
frase = input().lower()

while frase != "*":
    tautograma = True
    lista = frase.split()
    primeira_letra = lista[0][0]

    for i in lista:
        if i[0] != primeira_letra:
            tautograma = False
            break

    if tautograma:
        print("Y")
    else:
        print("N")
    
    frase = input().lower()
'''
# Fase
'''
n = int(input())
k = int(input())
empates = 0
lista_pontos = []

for i in range(n):
    pontos = int(input())
    lista_pontos.append(pontos)

lista_pontos.sort()
lista_pontos.reverse()

for i in range(k, n):
    if lista_pontos[i] == lista_pontos[k-1]:
        empates += 1

classificados = k + empates
print(classificados)
'''
