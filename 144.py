'''
Refaça o algoritmo do exercício 43 usando registro
exercício 43
Uma empresa irá dar um aumento de salário aos seus funcionários de acordo
com a categoria de cada empregado. O aumento seguirá a seguinte regra:
• Funcionários das categorias A, C, F, e H ganharão 10% de aumento sobre o
salário;
• Funcionários das categorias B, D, E, I, J e T ganharão 15% de aumento sobre
o salário;
• Funcionários das categorias K e R ganharão 25% de aumento sobre o salário;
• Funcionários das categorias L, M, N, O, P, Q e S ganharão 35% de aumento
sobre o salário;
• Funcionários das categorias U, V, X, Y, W e Z ganharão 50% de aumento
sobre o salário.
Faça um algoritmo que escreva nome, categoria e salário reajustado de cada
empregado.
'''

registro={"nome":[],"categoria":[],"salario":[]}
cont=-1
total=0

n_fun=int(input("Insira o numero de funcionários: "))

for y in range(n_fun):
    nome=input("Insira o nome do funcionário: ")
    cat=input("Insira a categoria do funcionário: ")
    salario=float(input("Insira o salário do funcionário: "))
    registro["nome"].append(nome)
    registro["categoria"].append(cat)
    registro["salario"].append(salario)


for x in registro["categoria"]:
    cont+=1
    if (x=="A" or x=="C" or x=="F" or x=="H"):
        total=registro["salario"][cont]*1.1
    elif (x=="B" or x=="D" or x=="E" or x=="I" or x=="J" or x=="T"):
        total=registro["salario"][cont]*1.15
    elif (x=="K" or x=="R"):
        total=registro["salario"][cont]*1.25
    elif (x=="L" or x=="M" or x=="N" or x=="O" or x=="P" or x=="Q" or x=="S"):
        total=registro["salario"][cont]*1.35
    elif (x=="U" or x=="V" or x=="X" or x=="Y" or x=="W" or x=="Z"):
        total=registro["salario"][cont]*1.5
    print("Nome: ",registro["nome"][cont])
    print("Catergoria: ",registro["categoria"][cont])
    print("Salário reajustado: %.2F"%total)
    