'''
Refaça o algoritmo do exercício 113 usando registro.
exercício 113
Crie um algoritmo que peça o nome, a altura e o peso de duas pessoas e
apresente o nome e peso da mais pesada e o nome e altura da mais alta.
'''
registro={"nome":[],"peso":[],"altura":[]}

for x in range (2):
    nome=input("Insira o nome: ")
    peso=float(input("Insira o peso: "))
    altura=float(input("Insira a altura: "))
    registro["nome"].append(nome)
    registro["peso"].append(peso)
    registro["altura"].append(altura)

if (registro["peso"][0]>registro["peso"][1]):
    print("Pessoa mais pessada.")
    print("Nome: ",registro["nome"][0])
    print("Peso: ",registro["peso"][0])
elif(registro["peso"][1]>registro["peso"][0]):
    print("Pessoa mais pessada.")
    print("Nome: ",registro["nome"][1])
    print("Peso: ",registro["peso"][1])

if(registro["altura"][0]>registro["altura"][1]):
    print("Pessoa mais pessada.")
    print("Nome: ",registro["nome"][0])
    print("Altura: ",registro["altura"][0])
if(registro["altura"][1]>registro["altura"][0]):
    print("Pessoa mais pessada.")
    print("Nome: ",registro["nome"][1])
    print("Altura: ",registro["altura"][1])