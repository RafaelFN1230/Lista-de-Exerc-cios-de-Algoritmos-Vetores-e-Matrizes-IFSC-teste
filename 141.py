'''
Escreva um programa para cadastrar até 30 alunos de uma turma. As
informações necessárias são: nome do aluno, nome da disciplina e média
final.
Deve ser usada uma estrutura de registro para a construção deste cadastro,
usando Type para a declaração do registro.
Ao final do cadastro de cada aluno deverá ser perguntado: "Novo Aluno
(S/N)?".
Deve-se utilizar um vetor do tipo declarado como registro para a solução deste
programa.
Após o término de todos os cadastros, ou seja, quando o usuário digitar "N" na
pergunta para novo aluno ou quando preencher o vetor com 30 alunos, a tela
deverá ser limpa e deverá ser montada uma tela para permitir a consulta aos
alunos por nome. Deverá ser digitada a palavra FIM para o nome para encerrar o
programa. Você poderá fazer uma tela de consulta com o formato que achar
adequado.
'''
cadastro={"nome do aluno":[],"disciplina":[],"media final":[]}
check=["N","S","n","s"]
pergunta=0
cont_perg=0
fim=0

import os

while(pergunta!=check[0] and cont_perg!=3):
    nome=input("Insira o nome do aluno: ")
    disciplina=input("Insira a disciplina: ")
    med=float(input("Insira a media final: "))
    cadastro["nome do aluno"].append(nome)
    cadastro["disciplina"].append(disciplina)
    cadastro["media final"].append(med)
    cont_perg+=1
    if cont_perg!=3:
        pergunta=input("Novo Aluno(S/N)?")

os.system('cls')

print("Consulta pelo nome do aluno")
while fim!="fim":
    cont_search=-1
    search=input("Insira o nome: ")
    for y in cadastro["nome do aluno"]:
        cont_search+=1
        if search==y:
            print("Nome do aluno: ",cadastro["nome do aluno"][cont_search])
            print("Disciplina: ",cadastro["disciplina"][cont_search])
            print("Media final: ",cadastro["media final"][cont_search])
            fim=input("Para finaliza o programa digite 'fim' ou aperte enter para continuar: ")
            cont_search=-1
        elif cont_search+1==cont_perg and search!=y:
            print("Aluno não encontrado.")
            fim=input("Para finaliza o programa digite 'fim' ou aperte enter para continuar: ")
            cont_search=-1
        
