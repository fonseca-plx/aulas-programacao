lista = list(map(int,input().split()))

tam = len(lista)
lista_crescente = sorted(lista)

if tam%2==1:
    mid = (tam+1)//2
    print(lista_crescente[mid-1])
else:
    mid = tam//2
    print((lista_crescente[mid]+lista_crescente[mid-1])/2)
