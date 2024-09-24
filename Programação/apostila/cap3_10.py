# Simulando um sistema de comercialização

valor_item, qtd, pgto = map(int, input().split())
valor_total = valor_item*qtd
troco = pgto-valor_total
print("A pagar: ", valor_total, "\n", "Troco: ", troco, sep="")
