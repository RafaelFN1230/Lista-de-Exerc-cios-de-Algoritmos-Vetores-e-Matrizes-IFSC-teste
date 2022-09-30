'''
Escreva um algoritmo que leia o código de um aluno e suas três notas. Calcule a
média ponderada do aluno, considerando que o peso para a maior nota seja 4 e
para as duas restantes, 3. Mostre o código do aluno, suas três notas, a média
calculada e uma mensagem: "APROVADO" se a média for maior ou igual a 5 e
"REPROVADO" se a média for menor que 5.
'''

cod=input("Insira o cod. do aluno: ")
nota1=float(input("Insira a nota 1: "))
nota2=float(input("Insira a nota 2: "))
nota3=float(input("Insira a nota 3: "))
media=0

if (nota1>=nota2 and nota1>=nota3):
    media=((nota1*4)+(nota2*3)+(nota3*3))/10
elif (nota2>nota1 and nota2>=nota3):
    media=((nota2*4)+(nota1*3)+(nota3*3))/10
elif (nota3>=nota2 and nota3>nota1):
    media=((nota3*4)+(nota2*3)+(nota1*3))/10

if (media>=5):
    print("Código do aluno: ",cod)
    print("Nota 1: ",nota1)
    print("Nota 2: ",nota2)
    print("Nota 3: ",nota3)
    print("Media: ",media)
    print("APROVADO")
elif (media<5):
    print("Código do aluno: ",cod)
    print("Nota 1: ",nota1)
    print("Nota 2: ",nota2)
    print("Nota 3: ",nota3)
    print("Media: ",media)
    print("REPROVADO")