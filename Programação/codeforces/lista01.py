# Decomposição de um número inteiro

valor = int(input())
print(valor)
print(valor//100, "nota(s) de R$ 100,00")
print((valor%100)//50, "nota(s) de R$ 50,00")
print((valor%100%50)//20, "nota(s) de R$ 20,00")
print((valor%100%50%20)//10, "nota(s) de R$ 10,00")
print((valor%100%50%20%10)//5, "nota(s) de R$ 5,00")
print((valor%100%50%20%10%5)//2, "nota(s) de R$ 2,00")
print((valor%100%50%20%10%5%2)//1, "nota(s) de R$ 1,00")
