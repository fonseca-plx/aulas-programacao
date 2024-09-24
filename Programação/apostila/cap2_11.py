x = int(input('Digite um número inteiro: '))
x_invertido = (x%10*1000) + ((x-x%10)%100)*10 + ((x-x%10)-(x-x%10)%100)%1000//10 + (((x-x%10)-(x-x%10)%100)-(((x-x%10)-(x-x%10)%100)%1000))//1000
print('O número digitado é {} e seu valor invertido é {}'.format(x, x_invertido))
