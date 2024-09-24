# Calculando tempo de viagem

'''
d//v retorna o tempo em horas (sem contar a porção decimal que seriam os minutos)
d%v vai retornar os quilometros restantes que vão ser percorridos em menos de 1 hora
d%v/v divide os quilometros que ainda faltam percorrer pela velocidade retornando um valor entre 0 e 1, ou seja, o que vai ser percorrido em menos de 1 hora
d%v/v*60 transforma a porção decimal de horas para minutos
'''

d = int(input("Digite a distância em km: "))
v = int(input("Digite a velocidade em km/h: "))
horas = d//v
minutos = ((d%v)*60)//v
print("O tempo de viagem é {}:{} horas".format(horas, minutos))
