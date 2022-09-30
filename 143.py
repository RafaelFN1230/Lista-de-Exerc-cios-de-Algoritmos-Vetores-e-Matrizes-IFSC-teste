'''
Refaça o algoritmo do exercício 42 usando registro.
exercício 42
Uma pessoa comprou quatro artigos em uma loja. Para cada artigo, tem-se
nome, preço e percentual de desconto. Faça um algoritmo que imprima nome,
preço e preço com desconto de cada artigo e o total a pagar.
'''

registro={"nome":[],"preço":[],"percentual":[]}
total=0
preço_desc=0

for x in range (4):
    nome=input("Insira o nome do artigo: ")
    preço=float(input("Insira o valor do arquivo: "))
    percent=float(input("Insira o percentual de desconto: "))
    registro["nome"].append(nome)
    registro["preço"].append(preço)
    registro["percentual"].append(percent)

for y in range(4):
    preço_desc=registro["preço"][y]-(registro["preço"][y]*(registro["percentual"][y]/100))
    print("Nome: ",registro["nome"][y])
    print("Preço: ",registro["preço"][y])
    print("Percentual: ",registro["percentual"][y])
    print("Preço com desconto: ",preço_desc)
    total+= preço_desc

print("Total: ",total)