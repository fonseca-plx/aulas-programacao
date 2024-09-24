# Questão 1

# n = list(map(int, input().split()))
# n = sorted(n)
# new_list = n[1:5]
# soma = sum(new_list)
# tam = len(new_list)
# media = soma/tam
# print(media)

# Questão 2

# a = int(input())
# b = int(input())
# mult = []

# for i in range(1, b+1):
#     if i%a == 0:
#         mult.append(i)
# print(*mult)

# Questão 3

a1 = int(input())
r = int(input())
n = int(input())
an = a1 + (r*(n-1))
termos = []

for i in range(a1, an+1, r):
    termos.append(i)
print(*termos)

# Questão 4

# lista = list(map(int, input().split()))
# nova_lista = []
# contador = 0

# for i in range(0, len(lista)):
#     if lista[i] == 1:
#         contador += 1
#     else:
#         if contador != 0:
#             for i in range(0, contador):
#                 nova_lista.append(contador)
#             nova_lista.append(0)
#         else:
#             nova_lista.append(0)
#         contador = 0

# if contador != 0:
#     for i in range(0, contador):
#         nova_lista.append(contador)

# print(*nova_lista)