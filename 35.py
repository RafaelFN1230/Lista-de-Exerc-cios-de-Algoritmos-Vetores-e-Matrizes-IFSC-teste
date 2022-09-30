'''
Considere que o último concurso vestibular apresentou três provas: Português,
Matemática e Conhecimentos Gerais. Considerando que para cada candidato
tem-se um registro contendo o seu nome e as notas obtidas em cada uma das
provas, construa um algoritmo que forneça:
a) o nome e as notas em cada prova do candidato
b) a média do candidato
c) uma informação dizendo se o candidato foi aprovado ou não. Considere que
um candidato é aprovado se sua média for maior que 7.0 e se não apresentou
nenhuma nota abaixo de 5.0
'''

nome=input("Insira o nome do canditato: ")
port=float(input("Insira a pontuação de português: "))
mat=float(input("Insira a pontuação de matemática: "))
con=float(input("Insira a pontuação de conecimentos gerais: "))

media=(port+mat+con)/3
print(nome,", ","nota de portugues: ",port,", nota de matematica: ",mat,", nota de conhecimentos gerais: ",con)
print("Media: ",media)
if media>=7 and port>=5 and mat>=5 and con>=5:
    print("Aprovado")
else:
    print("Reprovado")
