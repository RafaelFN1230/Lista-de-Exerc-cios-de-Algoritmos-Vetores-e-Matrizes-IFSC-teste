'''
Uma pessoa comprou quatro artigos em uma loja. Para cada artigo, tem-se
nome, preço e percentual de desconto. Faça um algoritmo que imprima nome,
preço e preço com desconto de cada artigo e o total a pagar.
'''

nome1=input("Insira o nome do produto: ")
nome2=input("Insira o nome do produto: ")
nome3=input("Insira o nome do produto: ")
nome4=input("Insira o nome do produto: ")
quant1=int(input("Insira aqui a quantidade do produto: "))
quant2=int(input("Insira aqui a quantidade do produto: "))
quant3=int(input("Insira aqui a quantidade do produto: "))
quant4=int(input("Insira aqui a quantidade do produto: "))
preco1=float(input("Insira aqui o preço do produto: "))
preco2=float(input("Insira aqui o preço do produto: "))
preco3=float(input("Insira aqui o preço do produto: "))
preco4=float(input("Insira aqui o preço do produto: "))
percent1=float(input("Insira aqui o perccentual de desconto do produto: "))
percent2=float(input("Insira aqui o perccentual de desconto do produto: "))
percent3=float(input("Insira aqui o perccentual de desconto do produto: "))
percent4=float(input("Insira aqui o perccentual de desconto do produto: "))

total=(((quant1*preco1)*percent1)/100)+(((quant2*preco2)*percent2)/100)+(((quant3*preco3)*percent3)/100)+(((quant4*preco4)*percent4)/100)

valor_prod1=preco1*quant1*(percent1-100)/100
valor_prod2=preco2*quant2*(percent2-100)/100
valor_prod3=preco3*quant3*(percent3-100)/100
valor_prod4=preco4*quant4*(percent4-100)/100


print(nome1,"",valor_prod1)
print(nome2,"",valor_prod2)
print(nome3,"",valor_prod3)
print(nome4,"",valor_prod4)
print("Total:",total)
