'''
Refaça o algoritmo do exercício 58 usando registro.
exercício 58
Escreva um algoritmo que leia o código de um aluno e suas três notas. Calcule a
média ponderada do aluno, considerando que o peso para a maior nota seja 4 e
para as duas restantes, 3. Mostre o código do aluno, suas três notas, a média
calculada e uma mensagem: "APROVADO" se a média for maior ou igual a 5 e
"REPROVADO" se a média for menor que 5.
'''
registro={"cod":[],"nota1":[],"nota2":[],"nota3":[]}
media=0
cont=0

n_alunos=int(input("Insira o numeros de alunos: "))

for x in range(n_alunos):
    cod=input("Insira o codigo do alunos: ")
    nota1=float(input("Insira nota 1: "))
    nota2=float(input("Insira nota 2: "))
    nota3=float(input("Insira nota 3: "))
    registro["cod"].append(cod)
    registro["nota1"].append(nota1)
    registro["nota2"].append(nota2)
    registro["nota3"].append(nota3)

for y in range (n_alunos):
    if (registro["nota1"][cont]>=registro["nota2"][cont] and registro["nota1"][cont]>=registro["nota3"][cont]):
        media=((registro["nota1"][cont]*4)+(registro["nota2"][cont]*3)+(registro["nota3"][cont]*3))/10
    elif (registro["nota2"][cont]>registro["nota1"][cont] and registro["nota2"][cont]>=registro["nota3"][cont]):
        media=((registro["nota2"][cont]*4)+(registro["nota1"][cont]*3)+(registro["nota3"][cont]*3))/10
    elif (registro["nota3"][cont]>=registro["nota2"][cont] and registro["nota3"][cont]>registro["nota1"][cont]):
        media=((registro["nota3"][cont]*4)+(registro["nota2"][cont]*3)+(registro["nota1"][cont]*3))/10
    if (media>=5):
        print("Código do aluno: ",registro["cod"][cont])
        print("Nota 1: ",registro["nota1"][cont])
        print("Nota 2: ",registro["nota2"][cont])
        print("Nota 3: ",registro["nota3"][cont])
        print("Media: ",media)
        print("APROVADO")
    elif(media<5):
        print("Código do aluno: ",registro["cod"][cont])
        print("Nota 1: ",registro["nota1"][cont])
        print("Nota 2: ",registro["nota2"][cont])
        print("Nota 3: ",registro["nota3"][cont])
        print("Media: ",media)
        print("REPROVADO")
    cont+=1


'''
#outra opção seria usar assim, sem registro nessa etapa
if (nota1>=nota2 and nota1>=nota3):
    media=((nota1*4)+(nota2*3)+(nota3*3))/10
elif (nota2>nota1 and nota2>=nota3):
    media=((nota2*4)+(nota1*3)+(nota3*3))/10
elif (nota3>=nota2 and nota3>nota1):
    media=((nota3*4)+(nota2*3)+(nota1*3))/10
'''