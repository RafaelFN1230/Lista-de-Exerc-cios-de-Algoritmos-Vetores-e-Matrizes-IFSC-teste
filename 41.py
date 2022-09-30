'''
A revendedora de carros Pica-Pau Ltda. paga aos seus funcionários vendedores
dois salários mínimos fixos, mais uma comissão fixa de R$ 50,00 por carro
vendido e mais 5% do valor das vendas. Faça um algoritmo que determine o
salário total de um vendedor.
'''

venda=float(input("Insira o valor vendido pelo vendedor:"))
n_carro=int(input("Insira o numero de carros vendidos:"))
salario=(1212*2)+(50*n_carro)+(venda*0.05)

print(salario)