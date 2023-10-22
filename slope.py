def slope(vertices, edges, n, k):
    p=n//k
    q=n%k

    print("="*25)
    print("p = "+str(p))
    print("q = "+str(q))
    print("="*25)
    
    pages = []
    rot = dict()
        
    for i in range(0,n):
        rot[vertices[i]]=i
        print(str(vertices[i])+" : "+str(i))

    print("="*25)
    for l in range(0,k):
        if l<q:
            s,t = (l*(p+1)) , ((l*(p+1))+p)
        else:
            s,t = (l*p+q) , (l*p+q+(p-1))
        pages.append((s,t))
        print("l="+str(l)+" -> "+"M_"+str(s)+","+str(t))
    print("="*25)

    print("="*25)
    for e in edges:
        i,j = rot[e[0]], rot[e[1]]
        slp = (i+j)%(n)
        for l in range(0,len(pages)):
            x=pages[l]
            if ((slp>=x[0]) and (slp<=x[1])):
                s,t=x[0],x[1]
                break
        print(str(e)+" : "+str((i,j)),end="")
        print(" -> ("+str(i)+"+"+str(j)+") mod "+str(n),end="")
        print(" -> "+"M_"+str(s)+","+str(t)+" -> "+"l = "+str(l))
    print("="*25)
    

def read_graph():
    vertices = set()
    edges = set()
    
    print("Write vertices: ")
    while True:
        s=str(input())
        if s=="":
            break
        vertices.add(s)

    vertices = list(vertices)
    vertices.sort()
    
    print("Write edges how v,w : ")
    while True:
        try:
            s=str(input())
            if s=="":
                break
            t = tuple(s.split(','))
            if len(t) != 2 :
                raise
            elif not((set(t)).issubset(vertices)):
                raise
            edges.add(t)
        except:
            print("Error.....")

    edges = list(edges)
    m=len(edges)
    n=len(vertices)
    
    return vertices, edges, n, m

def read_k():
    while True:
        try:
            k=int(input("k = "))
            if k<2:
                raise
            break
        except:
            print("Error.....")
    return k

def kn():
    vertices = []
    edges = []
    n=int(input("n = "))
    for i in range(0,n):
        vertices.append("v_"+str(i))
    for i in range(0,n):
        for j in range(i+1,n):
            edges.append((vertices[i],vertices[j]))
    m=len(edges)
    return vertices, edges, n, m 

def impr(vertices,edges,n,m):
    print("="*25)
    print("n = "+str(n))
    print("m = "+str(m))
    print("="*25)
    print("="*25)
    print("vertices")
    print(vertices)
    print("="*25)
    print("="*25)
    print("edges")
    print(edges)
    print("="*25)


while True:
    try:
        print("-"*25)
        print("[1] - New Graph")
        print("[2] - Complete Graph")
        print("[3] - Quit")
        print("-"*25)
        op=int(input("Write option: "))
        if op==1:
            vertices, edges, n, m = read_graph()
        elif op==2:
            vertices, edges, n, m = kn()
        elif op==3:
            break
        else:
            raise
        impr(vertices,edges,n,m)
        k = read_k()
        slope(vertices,edges, n, k)
    except:
        print("Error.....")

