'''
def soma(a,b):
    c = a+b
    return c
'''
'''
def media(a,b):
    c = (a+b)//2
    return c
'''
'''
def maior5(a,b,c,d,e):
    l = [a,b,c,d,e]
    maxnum = max(l)
    return maxnum
'''

def dia(dia):
    d = dia.sort()
    return d

lista = list(map(int, input().split()))
teste = dia(lista)
print(teste)
