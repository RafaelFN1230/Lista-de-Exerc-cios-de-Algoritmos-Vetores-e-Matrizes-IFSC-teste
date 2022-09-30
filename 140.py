'''
Fazer um programa que tenha um registro com os campos nome, endereco,
telefone, email, salário, leia os dados de entrada e processe o total dos salários e
imprima o valor do maior salário, e a quem pertence (nome).
Observação: ler o maximo de registros ou até que o nome seja "fim".
'''
registro={"nome":[],"endereco":[],"telefone":[],"email":[],"salário":[]}
pergunta=0
maior_salario=0
total_salarios=0
cont=0
dono=0

while (pergunta!="fim"):
    nome=input("Insira nome: ")
    endereco=input("Insira endereço: ")
    telefone=input("Insira telefone: ")#Telefone deve ser em forma de str pois pode começar com "0"
    email=input("Insira email: ")
    salário=float(input("Insira salário: "))

    registro["nome"].append(nome)
    registro["endereco"].append(endereco)
    registro["telefone"].append(telefone)
    registro["email"].append(email)
    registro["salário"].append(salário)
    pergunta=input("Se deseja para com o registro digite 'fim'")

for x in registro["salário"]:
    total_salarios+=x
    cont+=1
    if (maior_salario<x):
        maior_salario=x
        dono=cont-1

print(maior_salario, registro["nome"][dono])
    