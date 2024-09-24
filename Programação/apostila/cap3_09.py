# Convertendo dados fornecidos pelo usuário no tipo inteiro para o formato semanas e dias (desde o início do ano)

num_dias = int(input("Informe quantos dias já se passaram desde o início do ano: "))
semanas = num_dias//7
dias = num_dias%7
print(semanas, " semana(s) e\n", dias, " dia(s)", sep="")
