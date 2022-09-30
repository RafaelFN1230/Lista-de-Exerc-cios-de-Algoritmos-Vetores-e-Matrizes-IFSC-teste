'''
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
n_hoteis=int(input("Insira o numero de hóteis fazenda: "))
cont_dist=0
Cont_tipo=0
media_parc=0
media_final=0

for x in range (n_hoteis):
    nome=input("Insira o nome do hotel: ")
    dist=float(input("Insira a distancia (em Km) do hotel ate o centro: "))
    n_visit=int(input("Insira o numero medio de visitantes: "))
    tipo=int(input("tipo de acesso ao hotel (0 – acesso não asfaltado;1 – acesso asfaltado): "))
    if (dist>15):
        cont_dist+=1
    if (tipo==0):
        Cont_tipo+=1
        media_parc+=n_visit
    if (n_visit<1000 and tipo==1):
        print(nome,"=",dist)
media_final=media_parc/Cont_tipo
print("Hoteis que distam mais de 15km do centro: ",cont_dist)
print("Média de visitantes no último feriado, nos hoteis com acesso não asfaltado: ",media_final)


    
