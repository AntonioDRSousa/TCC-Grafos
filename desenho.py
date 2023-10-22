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

def t_count(omega,x1,x2,y1,y2):
    v1=x1//omega
    v2=x2//omega
    v3=y1//omega
    v4=y2//omega
    v=[v1,v2,v3,v4]
    s = set(v)
    size = len(s)

    if (size==4):
        return 1
    elif (size==1):
        return 2
    elif (size==3):
        return 5
    elif (v.count(v1)==2):
        return 4
    else:
        return 3

def count_cruz(edges,s,k,omega):
    ncruz=0
    cruz = [0,0,0,0,0]
    for i in range(0,len(edges)):
        for j in range(i+1,len(edges)):
            if s[i]==s[j]:
                e1 , e2 = edges[i] , edges[j]
                x1 , y1 , x2 , y2 = e1[0] , e1[1] , e2[0] , e2[1]
                b1=((x2 < x1) and (x1 < y2) and (y2 < y1))
                b2=((x1 < x2) and (x2 < y1) and (y1 < y2))
                if (b1 or b2):
                    ncruz += 1
                    cruz[t_count(omega,x1,x2,y1,y2)-1]+=1

    return ncruz, cruz
            
        


def main():
    ntuple = ""
    
    n=int(input("n = "))

    k=2
    h = hamiltoniano(bergeParImpar(n))

    omega = n//2
    theta = (n-1)+(n%2)
    p = theta//2
    q = theta % 2

    kn_edges = [None]*theta
    for i in range(0,theta):
        kn_edges[i] = [None]*theta
    kn_vertices = []

    for i in range(0,theta):
        ud = 0
        for j in range(i+1,theta):
            slp = (i+j) % theta
            if slp<=(p-1+q):
                kn_edges[i][j]=0
                ud-=1
            else:
                kn_edges[i][j]=1
                ud+=1
        if ud<=0:
            kn_vertices.append(0)
        else:
            kn_vertices.append(1)

    edges = []
    pos_edges = []
    cliques = []
    for i in range(0,len(h)):
        for j in range(i+1,len(h)):
            a , b = set(h[i]) , set(h[j])
            if a.intersection(b) == set():
                edges.append((a,b))
                pos_edges.append((i,j))
                v1=i//omega
                v2=j//omega
                cliques.append((v1,v2))
                
                if (v1==v2):
                    if (kn_vertices[v1]==0):
                        ntuple+="1"
                    else:
                        ntuple+="0"
                else:
                    ntuple+=str(kn_edges[v1][v2])


    ncruz,cruz = count_cruz(pos_edges,ntuple,k,omega)

    """
    print("-"*25)
    print(h)
    print("-"*25)
    print("-"*25)
    for i in range(0,len(edges)):
        print("edge = "+str(edges[i])+" | ",end="")
        print("position = "+str(pos_edges[i])+" | ",end="")
        print("cliques = "+str(cliques[i])+" | ",end="")
        print("up/down = "+str(ntuple[i]))
    print("-"*25)
    print("-"*25)
    print(ntuple)
    print("-"*25)
    """
    print("-"*25)
    print("cr1(n) = "+str(cruz[0]))
    print("cr2(n) = "+str(cruz[1]))
    print("cr3(n) = "+str(cruz[2]))
    print("cr4(n) = "+str(cruz[3]))
    print("cr5(n) = "+str(cruz[4]))
    print("crossing number = "+str(ncruz))
    print("-"*25)

main()
