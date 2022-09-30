'''
Com base em seu conhecimento defina os registros abaixo. Crie um algoritmo
que solicite ao usuário informar os dados do registro e imprima os mesmos na
tela:
a) cheque bancário;
b) livro;
c) aluno;
d) endereço;
e) cadastro de pessoa;
'''
cheque_bancario=input("Insira chque bancario: ")
livro=input("Insira livro: ")
aluno=input("Insira aluno: ")
endereço=input("Insira endereço: ")
cadastro_de_pessoa=input("Insira cadastro de pessoa: ")
registro={"cheque bancário":cheque_bancario,"livro":livro,"aluno":aluno,
"endereço":endereço,"cadastro de pessoa":cadastro_de_pessoa}
print(registro["cheque bancário"])
print(registro["livro"])
print(registro["aluno"])
print(registro["endereço"])
print(registro["cadastro de pessoa"])
