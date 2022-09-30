'''
O mesmo exercício 138, mas após o término de todos os cadastros, ou seja,
quando o usuário digitar "N" na pergunta para novo cliente ou quando preencher
o vetor com 50 clientes, a tela deverá ser limpa e deverá ser montada uma tela
para permitir a consulta aos clientes por código (que é o índice do vetor). Deverá
ser digitado o código 999 para encerrar o programa.
A tela de consulta deverá ter o seguinte formato:
Digite o código do cliente: _
Nome:
Endereço:
Telefone:
<Digite 999 para sair...>
'''
import os

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

os.system('cls')

cod=0
while (cod!=999):
    cod=int(input("Digite o codigo do cliente: "))
    print("Nome: ",cadastro["nome"][cod])
    print("Endereço:",cadastro["endereço"][cod])
    print("Telefone: ",cadastro["telefone"][cod])
    print("Digite 999 para sair...")