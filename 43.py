'''
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

cat=input("Insira aqui a categoria do funcionario: ")
nome=input("Insira aqui o nome do funcionario: ")
sal=float(input("Insira aqui o salario do funcionario: "))
sal_fin=0
if (cat=="A" or cat=="c" or cat=="F" or cat=="H" or cat=="a" or cat=="c" or cat=="f" or cat=="h"):
    sal_fin=sal*1.1
    print("Nome:",nome,"Categoria:",cat,"Salario:",sal_fin)
elif (cat=="B" or cat=="D" or cat=="E" or cat=="I" or cat=="J" or cat=="T" or cat=="b" or cat=="d" or cat=="e" or cat=="i" or cat=="j" or cat=="t"):
    sal_fin=sal*1.15
    print("Nome:",nome,"Categoria:",cat,"Salario:",sal_fin)
elif (cat=="K" or cat=="R" or cat=="k" or cat=="r"):
    sal_fin=sal*1.25
    print("Nome:",nome,"Categoria:",cat,"Salario:",sal_fin)
elif (cat=="L" or cat=="M" or cat=="N" or cat=="O" or cat=="P" or cat=="Q" or cat=="S" or cat=="k" or cat=="m" or cat=="n" or cat=="o" or cat=="p" or cat=="q" or cat=="s"):
    sal_fin=sal*1.35
    print("Nome:",nome,"Categoria:",cat,"Salario:",sal_fin)
elif (cat=="U" or cat=="V" or cat=="W" or cat=="X" or cat=="Y" or cat=="Z" or cat=="u" or cat=="v" or cat=="w" or cat=="x" or cat=="y" or cat=="z"):
    sal_fin=sal*1.50
    print("Nome:",nome,"Categoria:",cat,"Salario:",sal_fin)
else:
    print("Categoria incorreta")