# Pula Sapo

p, n = map(int, input().split())
alturas = list(map(int, input().split()))
caiu = False

for i in range(len(alturas) -1):
    if alturas[i+1] - alturas[i] > p or alturas[i+1] - alturas[i] < -p:
        caiu = True
        break

if caiu:
    print("GAME OVER")
else:
    print("YOU WIN")

