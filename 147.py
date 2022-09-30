'''
Refaça o algoritmo do exercício 114 usando registro.
exercício 114
Considere que, para cada um dos hotéis fazenda da região, se tenha registrado
o nome do hotel, a sua distância do centro da cidade, o número médio de
visitantes no último feriado e o tipo de acesso ao hotel (0 – acesso não asfaltado;
1 – acesso asfaltado). Construa um algoritmo que forneça:
a) O número de hoteis que distam mais de 15km do centro;
b) A quantidade média de visitantes no último feriado, nos hoteis com acesso
não asfaltado;
c) O nome e a distância do centro em Km, de todos os hoteis de acesso
asfaltado que tiveram menos de 1.000 visitantes.
'''

registro={"nome":[],"distancia":[],"numero de visitantes":[],"acesso":[]}

b=[]
c=[]

cont_dist=0
Cont_tipo=0
cont_acesso=0
cont_c=0
media_parc=0
media_final=0

n_hoteis=int(input("Insira o numero de hóteis fazenda: "))
for x in range (n_hoteis):
    nome=input("Insira o nome do hotel: ")
    dist=float(input("Insira a distancia (em Km) do hotel ate o centro: "))
    n_visit=int(input("Insira o numero medio de visitantes: "))
    acesso=int(input("tipo de acesso ao hotel (0 – acesso não asfaltado;1 – acesso asfaltado): "))
    registro["nome"].append(nome)
    registro["distancia"].append(dist)
    registro["numero de visitantes"].append(n_visit)
    registro["acesso"].append(dist)

#A
for y in registro["distancia"]:
    if (y<15):
        cont_dist+=1
print("Hoteis que distam mais de 15km do centro: ",cont_dist)

#B e C
for z in registro["acesso"]:
    if (z==0):
        b.append(cont_acesso)
    elif (z==1):
        for B in registro["numero de visitantes"]:
            if (B<=1000):
                c.append(cont_c)
            cont_c+=1      
    cont_acesso+=1

for A in b:
    media_parc+=registro["numero de visitantes"][A]
media_final=media_parc/cont_acesso
print("Média de visitantes no último feriado, nos hoteis com acesso não asfaltado: ",media_final)

#C
for C in c:
    print("Hoteis que distam mais de 15km do centro: ", registro["nome"][C],"=",registro["distancia"][C]) 