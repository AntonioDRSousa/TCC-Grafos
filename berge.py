def berge(n):
    q=n//2
    brg=[[None for x in range(q)] for y in range(n-1)]
    for i in range(0,n-1):
        brg[i][0]=(1,i+2)
        for j in range(1,q):
           l= ( ((i+2)-(j+2)) % (n-1) ) + 2
           r= ( ((i+2)+(j-2)) % (n-1) ) + 2
           brg[i][j]=(l,r)
    return brg

def hamiltoniano(b):
    p=[]
    for i in b:
        p+=i
    return p

def bergeParImpar(n):
    if n%2==0:    
        b=berge(n)
    else:
        brg=berge(n+1)
        b=[]
        for i in brg:
            b+=[list(filter(lambda x: x[0]!=(n+1) and x[1]!=(n+1), i))]
    return b
    
def impr(b,p):
    print("-------------------------------------------")
    print("Algoritmo de Berge\n\n")
    for j in range(0,len(b[0])):
        for i in range(0,len(b)):
            print(str(b[i][j]),end=" ")
        print()
    print("\n\nCaminho Hamiltoniano")
    print("P = ( ",end="")
    print(*p, sep=" , ",end=" )\n\n")
    print("-------------------------------------------")

while True:
    n = int(input("n = "))

    t=bergeParImpar(n)
    h=hamiltoniano(t)
    impr(t,h)

    ch=input("\nDigite 'c' para continuar: ")
    if ch!='c':
        break
    print()
