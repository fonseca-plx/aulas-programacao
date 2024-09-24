def dia(dia, mes, ano):
    meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

    data_por_extenso = ""

    if mes-1 == meses.index("janeiro") or mes-1 == meses.index("marco") or mes-1 == meses.index("maio") or mes-1 == meses.index("julho") or mes-1 == meses.index("agosto") or mes-1 == meses.index("outubro") or mes-1 == meses.index("dezembro"):
        if dia >= 1 and dia <= 31:
            data_por_extenso = "{:02d} de {} de {}".format(dia, meses[mes-1], ano)
        else:
            data_por_extenso = "Data Invalida"
    elif mes-1 == meses.index("abril") or mes-1 == meses.index("junho") or mes-1 == meses.index("setembro") or mes-1 == meses.index("novembro"):
        if dia >= 1 and dia <= 30:
            data_por_extenso = "{:02d} de {} de {}".format(dia, meses[mes-1], ano)
        else:
            data_por_extenso = "Data Invalida"
    elif mes-1 == meses.index("fevereiro"):
        if dia >= 1 and dia <= 28:
            data_por_extenso = "{:02d} de {} de {}".format(dia, meses[mes-1], ano)
        else:
            data_por_extenso = "Data Invalida"
    else:
        data_por_extenso = "Data Invalida"
    return data_por_extenso

d, m, a = map(int, input().split())
data = dia(d, m, a)
print(data)
