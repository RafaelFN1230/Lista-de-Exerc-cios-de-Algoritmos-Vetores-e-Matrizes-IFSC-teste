'''
Refaça o algoritmo do exercício 35 usando registro
exercício 35: 
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
media=0
registro={"provas":{"portugues":[],"matematica":[],"conhecimentos gerais":[]},"nome":[]}

nome=input("Nome do candidato: ")
port=float(input("Nota de Portugues: "))
mat=float(input("Nota de Matematica: "))
con=float(input("Nota de Conhecimentos Gerais: "))

registro["nome"].append(nome)
registro["provas"]["portugues"].append(port)
registro["provas"]["matematica"].append(mat)
registro["provas"]["conhecimentos gerais"].append(con)

print(nome)
print("Nota Portugues: ",registro["provas"]["portugues"][0])
print("Nota Matematica: ",registro["provas"]["matematica"][0])
print("Nota Conhecimentos Gerais: ",registro["provas"]["conhecimentos gerais"][0])

media=(registro["provas"]["portugues"][0]+registro["provas"]["matematica"][0]+registro["provas"]["conhecimentos gerais"][0])/3
print(media)

if (media>=7):
    if (registro["provas"]["portugues"][0] >=5 and registro["provas"]["matematica"][0] >=5 and registro["provas"]["conhecimentos gerais"][0]>=5):
        print("APROVADO")
    else:
        print("REPROVADO")
else:
    print("REPROVADO")