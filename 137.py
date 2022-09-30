'''
Escreva um programa para cadastrar dois clientes de uma loja. As informações
necessárias são: nome, endereço e telefone. Deve ser usada uma estrutura de
registro para a construção deste cadastro, usando Type para a declaração do
registro.
'''

cadastro={"nome":[],"endereço":[],"telefone":[]}
for x in range (2):
    nome=input("Insira nome: ")
    endereço=input("Insira endereço: ")
    telefone=input("Insira telefone: ")
    cadastro["nome"].append(nome)
    cadastro["endereço"].append(endereço)
    cadastro["telefone"].append(telefone)


print(type(cadastro))
print(cadastro)