'''
O sistema de avaliação de determinada disciplina, é composto por três provas. A
primeira prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5. Faça
um algoritmo para calcular a média final de um aluno desta disciplina.
'''

av1=float(input("Insira o Valor da AV1: "))
av2=float(input("Insira o Valor da AV2: "))
av3=float(input("Insira o Valor da AV3: "))

media=((av1*2)+(av2*3)+(av3*5))/10
print("A media do aluno é: ",media)