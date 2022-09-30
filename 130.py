'''
Escrever um algoritmo que lê um vetor G(13) que é o gabarito de um teste de
loteria esportiva, contendo os valores 1 (coluna 1), 2 (coluna 2) e 3 (coluna do
meio). 
Ler, a seguir, para cada apostador, o número de seu cartão e um vetor Resposta R (13). 
Verificar para cada apostador o número de acertos e escrever o
número do apostador e seu número de acertos. Se tiver 13 acertos, acrescentar
a mensagem: "GANHADOR, PARABENS".
'''
G=[]
R=[]
cont=0

for x in range (13):
    g=int(input("Insira o Gabarito: "))
    G.append(g)

n=int(input("Insira o numero do cartão: "))

for y in range (13):
    r=int(input("Insira sua resposta: "))
    R.append(r)

for a in R:
    for b in G:
        if (a==b):
            cont+=1

if (cont==13):
    print("Bilhete numero",n,"GANHADOR, PARABENS")
elif (cont<13):
    print("Bilhete numero",n,"teve:",cont,"acertos")