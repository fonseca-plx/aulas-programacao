# Quantidade de divisores de um número natural
'''
def conta_divisores_rec(n, d):
    if d==1:
        return 1
    else:
        div = 0
        if n%d==0:
            div = 1
        return div + conta_divisores_rec(n, d-1)

def conta_divisores(n):
    return conta_divisores_rec(n, n)

num = int(input())
divisores = conta_divisores(num)
print(divisores)
'''
# Maior divisor par
'''
def maior_divisor_par(num):
    return maior_divisor_par_rec(num, num//2)

def maior_divisor_par_rec(n, d):
    if n%2!=0:
        return 0
    elif n%d==0 and d%2==0:
        return d
    else:
        return maior_divisor_par_rec(n, d-1)

        
n = int(input())
teste = maior_divisor_par(n)
print(teste)
'''
# Quantidade de algarismos

def conta_algarismos(n):
    if n<10:
        return 1
    else:
        cont_alg = 1
        return cont_alg + conta_algarismos(n//10)

num = int(input())
alg = conta_algarismos(num)
print(alg)

# Lista de divisores de um número natural
'''
def divisores_rec(n, d):
    if d==1:
        return [1]
    else:
        divs = divisores_rec(n, d-1)
        if n%d==0:
            divs.append(d)
        return divs

def divisores(n):
    return divisores_rec(n, n)

num = int(input())
teste = divisores(num)
print(teste)
'''
