# múltiplos
'''
a = int(input())
b = int(input())

if (a>=b):
    if (a%b==0):
        multi = "Multiplos"
    elif (a%b!=0):
        multi = "Nao multiplos"
else:
    if (b%a==0):
        multi = "Multiplos"
    elif (b%a!=0):
        multi = "Nao multiplos"

print(multi)
'''
# coordenadas de um ponto no plano cartesiano
'''
x, y = map(float, input().split())

if (x==0 and y==0):
    ponto = "Origem"
elif (x==0 and y!=0):
    ponto = "Eixo Y"
elif (x!=0 and y==0):
    ponto = "Eixo X"
elif (x>0 and y>0):
    ponto = "Q1"
elif (x>0 and y<0):
    ponto = "Q4"
elif (x<0 and y>0):
    ponto = "Q2"
else:
    ponto = "Q3"
print(ponto)
'''
# geometria espacial: dimensões de uma esfera e de um cubo
'''
n = int(input())
a, l, p = map(int, input().split())

if (n<=a and n<=l and n<=p):
    print("S")
else:
    print("N")
'''
# Tira-teima

x, y = map(int, input().split())

if (x>=0 and x<=432 and y>=0 and y<=468):
    tirateima = "dentro"
else:
    tirateima = "fora"
print(tirateima)
