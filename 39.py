'''
Suponha que um caixa disponha apenas de notas de 1, 10 e 100 reais.
Considerando que alguém está pagando uma compra, escreva um algoritmo que
mostre o número mínimo de notas que o caixa deve fornecer como troco. Mostre
também: o valor da compra, o valor do troco e a quantidade de cada tipo de nota
do troco. Suponha que o sistema monetário não utilize moedas.
'''

valor_comp=int(input("Insira aqui o valor de compra:"))
valor_pago=int(input("Insira aqui o valor pago:"))
valor_troco=valor_pago-valor_comp
uni=0
dez=0
cem=0


if (valor_troco>100):
    cem=valor_troco//100

if (valor_troco>10):
    dez=(valor_troco-(cem*100))//10

if (valor_troco>1):
    uni=(valor_troco-((cem*100)+(dez*10)))//1




print("Quantidades de cedulas de cem:",cem)
print("Quantidades de cedulas de dez:",dez)
print("Quantidades de cedulas de um:",uni)