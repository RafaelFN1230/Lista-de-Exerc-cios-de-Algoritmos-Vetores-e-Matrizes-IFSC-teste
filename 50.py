'''
Suponha que o conceito de um aluno seja determinado em função da sua nota.
Suponha, também, que esta nota seja um valor inteiro na faixa de 0 a 100,
conforme a seguinte faixa:
Nota Conceito
0 a 49 Insuficiente
50 a 64 Regular
65 a 84 Bom
85 a 100 Ótimo
Crie um algoritmo que apresente o conceito e a nota do aluno.
'''
nota=int(input("Insira aqui o valor da nota do aluno (0 a 100): "))

print("Nota Conceito:")
print("0 a 49 Insuficiente")
print("50 a 64 Regular")
print("65 a 84 Bom")
print("85 a 100 Ótimo")
print(" ")

if (nota<50):
    print("Insuficiente")
elif (nota>40 and nota<65):
    print("Regular")
elif (nota>64 and nota<85):
    print("Bom")
elif (nota>84 and nota<=100):
    print("Ótimo")
