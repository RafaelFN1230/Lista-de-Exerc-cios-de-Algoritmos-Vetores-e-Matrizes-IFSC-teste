'''
Faça um algoritmo para somar duas matrizes.
'''
a=[1,2,3]
b=[4,5,6,7]
c=[]
soma=0

while a!=[]:
    soma=a[0]+b[0]
    a.pop(0)
    b.pop(0)
    c.append(soma)

print(c+b)
