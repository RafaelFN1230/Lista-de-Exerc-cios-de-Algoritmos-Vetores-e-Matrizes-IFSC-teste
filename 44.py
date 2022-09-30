'''
Uma sorveteria vende três tipos de picolés. Sabendo-se que o picolé do tipo 1 é
vendido por R$ 0.50, o do tipo 2 por R$ 0.60 e o do tipo 3 por R$ 0.75, faça um
algoritmo que, para cada tipo de picolé, mostre a quantidade vendida e o total
arrecadado.
'''

um_val=0.5
um=0
dois_val=0.6
dois=0
tres_val=0.75
tres=0

tipo=int(input("Insira aqui qual picole voce gostaria: "))
print("Insira 0 para sair do programa")
while (tipo!=0):
    if (tipo==1):
        quant_um=int(input("Insira a quantidade do tipo um: "))
        um+=quant_um
    elif(tipo==2):
        quant_dois=int(input("Insira a quantidade do tipo dois: "))
        dois+=quant_dois
    elif(tipo==3):
        quant_tres=int(input("Insira a quantidade do tipo tres: "))
        tres+=quant_tres
    tipo=int(input("Insira aqui qual picole voce gostaria: "))

tot=um_val*um+dois_val*dois+tres_val*tres
quant_tot=quant_um+quant_dois+quant_tres

print("Quantidade: ", quant_tot)
print("Total: ",tot)