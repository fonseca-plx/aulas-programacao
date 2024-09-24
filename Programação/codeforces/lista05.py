# Corrida
'''
n1, d1, v1 = map(int, input().split())
n2, d2, v2 = map(int, input().split())

t1 = (d1*(10**-3))/v1
t2 = (d2*(10**-3))/v2

if t1 > t2:
    vencedor = n2
elif t1 < t2:
    vencedor = n1

print(vencedor)
'''
# Interceptando Informações
'''
n1, n2, n3, n4, n5, n6, n7, n8 = map(int, input().split())

if n1==9 or n2==9 or n3==9 or n4==9 or n5==9 or n6==9 or n7==9 or n8==9:
    print("F")
else:
    print("S")
'''
# Piloto Automático
'''
a = int(input())
b = int(input())
c = int(input())

if (b-a)<(c-b):
    print(1)
elif (b-a)>(c-b):
    print(-1)
elif (b-a)==(c-b):
    print(0)
'''
# A idade da Dona Monica
'''
m = int(input())
a = int(input())
b = int(input())
c = m-(a+b)

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
'''
# Conta de água
'''
n = int(input())
valor = 7

if n>=0 and n<=10:
    valor = valor
elif n>=11 and n<=30:
    valor += n-10
elif n>=31 and n<=100:
    valor += 20 + 2*(n-30)
elif n>=101:
    valor += 20 + 140 + 5*(n-100)

print(valor)
'''
# Escolha difícil
'''
a, b, c = map(int, input().split())
d, e, f = map(int, input().split())

passageiros_n_atendidos = 0

if a>=d and b>=e and c>=f:
    passageiros_n_atendidos = 0
if a<d:
    passageiros_n_atendidos = d-a
if b<e:
    passageiros_n_atendidos += e-b
if c<f:
    passageiros_n_atendidos += f-c

print(passageiros_n_atendidos)
'''
# Andando no tempo
'''
a, b, c = map(int, input().split())

if a==b or a==c or b==c:
    print("S")
elif a+b==c or a+c==b or b+c==a:
    print("S")
else:
    print("N")
'''
# Dupla de tênis
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

nivel_jogadores = [a, b, c, d]
ordem = sorted(nivel_jogadores)

menor_dif = (ordem[3]+ordem[0])-(ordem[2]+ordem[1])
print(menor_dif)
'''