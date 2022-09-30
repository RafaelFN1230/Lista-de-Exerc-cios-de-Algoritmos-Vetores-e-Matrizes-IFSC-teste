'''
Uma empresa de vendas tem três corretores. A empresa paga ao corretor uma
comissão calculada de acordo com o valor de suas vendas. Se o valor da venda
de um corretor for maior que R$ 50.000.00 a comissão será de 12% do valor
vendido. Se o valor da venda do corretor estiver entre R$ 30.000.00 e R$
50.000.00 (incluindo extremos) a comissão será de 9.5%. Em qualquer outro
caso, a comissão será de 7%. Escreva um algoritmo que gere um relatório
contendo nome, valor da venda e comissão de cada um dos corretores. O
relatório deve mostrar também o total de vendas da empresa.
'''

c1=float(input("Vendas do corretor 1: "))
c2=float(input("Vendas do corretor 1: "))
c3=float(input("Vendas do corretor 1: "))

if c1>50000:
    c1=c1*0.12
    print("A comissão do primeiro corretor é de: R$",c1)
elif c1>=30000 and c1<=50000:
    c1=c1*0.095
    print("A comissão do primeiro corretor é de: R$",c1)
else:
    c1=c2*0.07
    print("A comissão do primeiro corretor é de: R$",c1)

if c2>50000:
    c2=c2*0.12
    print("A comissão do primeiro corretor é de: R$",c2)
elif c2>=30000 and c2<=50000:
    c2=c2*0.095
    print("A comissão do primeiro corretor é de: R$",c2)
else:
    c2=c2*0.07
    print("A comissão do primeiro corretor é de: R$",c2)

if c3>50000:
    c3=c3*0.12
    print("A comissão do primeiro corretor é de: R$",c3)
elif c3>=30000 and c3<=50000:
    c3=c3*0.095
    print("A comissão do primeiro corretor é de: R$",c3)
else:
    c3=c3*0.07
    print("A comissão do primeiro corretor é de: R$",c3)

