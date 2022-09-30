'''
Escreva um algoritmo que, para uma conta bancária, leia o seu número, o saldo,
o tipo de operação a ser realizada (depósito ou retirada) e o valor da operação.
Após, determine e mostre o novo saldo. Se o novo saldo ficar negativo, deve ser
mostrada, também, a mensagem “conta estourada”.
'''

saldo=0
n=int(input("Insira aqui o seu numero: "))
print("Insira 'PARE' para encerrar o programa.")
op=input("Insira o tipo da operação: ")

while (op!="PARE"):
    if(op=="DEPÓSITO"):
        val=float(input("Insira aqui o valor do deposito: "))
        saldo+=val
    elif(op=="RETIRADA"):
        val=float(input("Insira aqui o valor da retirada: "))
        saldo-=val
    if(saldo>=0):
        print("O seu saldo é: ",saldo)
    elif(saldo<0):
        print("Conta estourada.", saldo)
    op=input("Insira o tipo da operação: ")
if (op=="PARE"):
    print("Seu numero é: ",n)
    print("O seu saldo é: ",saldo)
    quit()

