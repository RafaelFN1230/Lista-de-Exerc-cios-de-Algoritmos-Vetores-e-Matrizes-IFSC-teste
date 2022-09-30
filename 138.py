'''
O mesmo exercício 137, mas o programa deverá suportar até 50 clientes. Ao
final do cadastro de cada cliente deverá ser perguntado: "Novo Cliente (S/N)?".
Deve-se utilizar um vetor do tipo declarado como um registro para a solução
deste programa.
'''
cadastro={"nome":[],"endereço":[],"telefone":[]}
novo_cliente=["S","N"]
cont=0
while (cont<51):
    nome=input("Insira nome: ")
    endereço=input("Insira endereço: ")
    telefone=input("Insira telefone: ")
    cadastro["nome"].append(nome)
    cadastro["endereço"].append(endereço)
    cadastro["telefone"].append(telefone)
    cont+=1
    pergunta=input("Novo Cliente (S/N)?")
    if (pergunta==novo_cliente[1]):
        cont+=50


print(type(cadastro))
print(cadastro)
