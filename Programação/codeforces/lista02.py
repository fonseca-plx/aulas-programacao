'''
nome = input()
horas = int(input())
valor = float(input())
print(nome)
print("R$ {:.2f}".format(horas*valor))
'''
'''
n1, n2 = map(float, input().split())
print(int(n2/n1*100))
'''
'''
nome = input()
salario = float(input())
vendas = float(input())
print(nome)
print("R$ {:.2f}".format(salario+(vendas*0.15)))
'''
'''
valor_item = int(input())
quantidade = int(input())
pgto = int(input())
print("A pagar: {}".format(valor_item*quantidade))
print("Troco  : {}".format(pgto-valor_item*quantidade))
'''
'''
t = int(input())
print(t*4)
'''
'''
d = int(input())
v = int(input())
horas = d//v
minutos = ((d%v)*60)//v
print("{:02}:{:02}".format(horas, minutos))
'''
'''
t1, t2, t3, t4 = map(int, input().split())
print(t1+t2+t3+t4-3)
'''
'''
c, n = map(int, input().split())
print(c%n)
'''
l, d = map(int, input().split())
k, p = map(int, input().split())