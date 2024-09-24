# Convertendo números inteiros para o formato horas:minutos

inicio, fim = map(int, input().split())
horas = (fim-inicio)//60
minutos = (fim-inicio)%60
print(horas, ":", minutos, sep="")
