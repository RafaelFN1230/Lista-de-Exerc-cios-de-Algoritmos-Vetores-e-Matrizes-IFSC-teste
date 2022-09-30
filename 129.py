'''
Escrever um algoritmo que lê um vetor N(20) e o escreve. Troque, a seguir, o 1º
elemento com o último, o 2º com o penúltimo etc. até o 10º com o 11º e escreva
o vetor N assim modificado.
'''

x=[]
for y in range (20):
    a=int(input("Insira o valor: "))
    x.append(a)

x.sort(reverse=True)
print(x)