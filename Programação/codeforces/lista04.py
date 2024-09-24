# Frota de taxi
'''
a, g, ra, rg = map(float, input().split())

if (a/ra < g/rg):
    print("A")
else:
    print("G")
'''
# Triangulo
'''
a, b, c, d = map(int, input().split())

if (a+b>c and a+c>b and b+c>a):
    print("S")
elif (a+b>d and a+d>b and b+d>a):
    print("S")
elif (a+c>d and a+d>c and c+d>a):
    print("S")
elif (b+c>d and b+d>c and c+d>b):
    print("S")
else:
    print("N")
'''
# Maior de 5 numeros
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
maior = a

if (b>=maior):
    maior = b
if (c>=maior):
    maior = c
if (d>=maior):
    maior = d
if (e>=maior):
    maior = e
print(maior)
'''
# Maior média ponderada
'''
a11, a21 = map(int, input().split())
a12, a22 = map(int, input().split())
p1, p2 = map(int, input().split())

m1 = (a11*p1+a21*p2)//(p1+p2)
m2 = (a12*p1+a22*p2)//(p1+p2)

if (m1>=m2):
    a = 1
else:
    a = 2
print(a)
'''
# Idade de Camila
'''
a = int(input())
b = int(input())
c = int(input())

if (a>=b and b>=c):
    idade = b
elif (b>=a and a>=c):
    idade = a
elif (a>=c and c>=b):
    idade = c
elif (b>=c and c>=a):
    idade = c
elif (c>=a and a>=b):
    idade = a
elif (c>=b and b>=a):
    idade = b
print(idade)
'''
# Teleférico
'''
c = int(input())
a = int(input())
v = 0
m = 0

if (c>a):
    v = 1
elif (c==a):
    v = 2
elif (c<a):
    if (a%c==0):
        v = a//c+1
    elif (a%c!=0):
        v = a//c+1
        m = v
        if(a+m>c*v):
            v = v+1
        else:
            v = a//c+1
print(v)
'''
# Triangulos
'''
a, b, c = map(int, input().split())

if a+b>c and a+c>b and b+c>a:
    if (a**2)==(b**2)+(c**2) or (b**2)==(a**2)+(c**2) or (c**2)==(a**2)+(b**2):
        print("r")
    elif (a**2)>(b**2)+(c**2) or (b**2)>(a**2)+(c**2) or (c**2)>(a**2)+(b**2):
        print("o")
    else:
        print("a")
else:
    print("n")
'''
# Nota Cortada

b = int(input())
t = int(input())
valor = 0

if ((b+t)*70)/2 == (160*70)/2:
    valor = 0
elif ((b+t)*70)/2 > (160*70)/2:
    valor = 1
elif ((b+t)*70)/2 < (160*70)/2:
    valor = 2

print(valor)