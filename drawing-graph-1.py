import cairo
import math

width = 600  # width of image
height = 600 # height of image
cv = (0,0,0) # color of vertices
cs = (0,1,0) # color of spine
cu = (0,0,1) # color of up edges
cd = (1,0,0) # color of down edges
cb = (1,1,1) # color of background
o = True     # orientation
ew = 1       # edge width
fw = 1       # foreground width
cf = (0,0,0) # foreground color
cq = 0       # orientation of clique in case equal
name = True  # automatically or manually naming

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

def draw(n):
    global width, height, cv, cs, cu, cd, cb, o, ew, fw, cf, ecc, cq, name
            
    ntuple = ""

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
        if ud<0:
            kn_vertices.append(0)
        elif ud>0:
            kn_vertices.append(1)
        else:
            kn_vertices.append(cq)

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

    return (n,ntuple,pos_edges,omega,theta)

def oposite(ntuple):
    nt=""
    for i in range(0,len(ntuple)):
        if ntuple[i]=="0":
            nt+="1"
        else:
            nt+="0"
    return nt

def plot(t):
    global width, height, cv, cs, cu, cd, cb, o, ew, fw, cf, ecc, cq, name

    n,ntuple,pos_edges,omega,theta = (t[0],t[1],t[2],t[3],t[4])

    if (not o):
        ntuple=oposite(ntuple)

    nvertices = (n*(n-1))//2
    cut_x = width//(2*nvertices + theta)
    radius = cut_x//2

    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    ctx = cairo.Context(surface)

    ctx.rectangle(0, 0, width, height)
    ctx.set_source_rgb(cb[0],cb[1],cb[2])
    ctx.fill()

    pos_vertices = []
    for i in range(0,2*nvertices):
        if (i%2==0):
            clique = ((i//2)//omega)+1
            pos_vertices.append(((i+clique)*cut_x+radius))

            ctx.arc(pos_vertices[i//2],height//2, radius, 0, 2*math.pi)
            ctx.set_source_rgb(cv[0],cv[1],cv[2])
            ctx.fill()
            ctx.stroke()

            ctx.arc(pos_vertices[i//2],height//2, radius, 0, 2*math.pi)
            ctx.set_source_rgb(cf[0],cf[1],cf[2])
            ctx.set_line_width(fw)
            ctx.stroke()
    
    for i in range(0,len(pos_edges)):
        e = pos_edges[i]
        x , y = e[0] , e[1]
        ctx.set_line_width(ew)
        if ((abs(x-y))==1):
            ctx.set_source_rgb(cs[0],cs[1],cs[2])
            ctx.move_to(pos_vertices[max(x,y)] - radius, height//2)
            ctx.line_to(pos_vertices[min(x,y)] + radius, height//2)    
        else:
            v1=x//omega
            v2=y//omega
            r  = (abs(pos_vertices[x]-pos_vertices[y]))//2
            center = pos_vertices[min(x,y)] + r
            
            if (ntuple[i]=="0"):
                ctx.set_source_rgb(cd[0],cd[1],cd[2])
                ctx.arc(center, (height//2)+radius, r , 0, math.pi)
            else:
                ctx.set_source_rgb(cu[0],cu[1],cu[2])
                ctx.arc_negative(center, (height//2)-radius, r , 0, math.pi)
        ctx.stroke()

    if(name):
        surface.write_to_png('k'+str(n)+'2'+'.png')
    else:
        surface.write_to_png(str(input("name = "))+'.png')

def dsettings():
    global width, height, cv, cs, cu, cd, cb, o, ew, fw, cf, ecc, cq, name
    width = 600
    height = 600
    cv = (0,0,0)
    cs = (0,1,0)
    cu = (0,0,1)
    cd = (1,0,0)
    cb = (1,1,1)
    orientation = True
    ew = 1
    fw = 1
    cf = (0,0,0)
    cq = 0     
    name = True

def set_color(s):
    c=str(input("color of "+s+" = "))
    v = c.split(',')
    v = (float(v[0]),float(v[1]),float(v[2]))
    return tuple(v)

def settings():
    global width, height, cv, cs, cu, cd, cb, o, ew, fw, cf, ecc, cq, name
    while True:
        print("-"*25)
        print("[  1 ] - width")
        print("[  2 ] - height")
        print("[  3 ] - color of vertices")
        print("[  4 ] - color of spine")
        print("[  5 ] - color of up edges")
        print("[  6 ] - color of down edges")
        print("[  7 ] - color of background")
        print("[  8 ] - orientation of tuple")
        print("[  9 ] - edge width")
        print("[ 10 ] - foreground width")
        print("[ 11 ] - foreground color")
        print("[ 12 ] - clique orientation in case equal")
        print("[ 13 ] - automatically/manually naming")
        print("[0] - Quit")
        print("-"*25)
        op=int(input(""))
        if op==0:
            break
        elif op==1:
            print("width = "+str(width))
            width = int(input("width = "))
        elif op==2:
            print("height = "+str(height))
            height = int(input("height = "))
        elif op==3:
            print("color of vertices = "+str(cv))
            cv = set_color("vertices")
        elif op==4:
            print("color of spine = "+str(cs))
            cs = set_color("spine")
        elif op==5:
            print("color of up edges = "+str(cu))
            cu = set_color("up edges")
        elif op==6:
            print("color of down edges = "+str(cd))
            cd = set_color("down edges")
        elif op==7:
            print("color of background = "+str(cb))
            cb = set_color("background")
        elif op==8:
            print("orientation of tuple = "+str(orientation))
            orientation = bool(int(input("orientation = ")))
        elif op==9:
            print("edge width = "+str(ew))
            ew = float(str(input("edge width = ")))
        elif op==10:
            print("foreground width = "+str(fw))
            fw = float(str(input("foreground width = ")))
        elif op==11:
            print("foreground color = "+str(cf))
            fw = set_color("foreground")
        elif op==12:
            print("clique orientation in case equal = "+str(cq))
            cq = bool(str(input("clique orientation = ")))
        elif op==13:
            print("automatically/manually naming = "+str(name))
            name = bool(str(input("auto/man = ")))
        else:
            raise

def read_settings():
    global width, height, cv, cs, cu, cd, cb, o, ew, fw, cf, ecc, cq, name
    print("-"*25)
    print("width = "+str(width))
    print("height = "+str(height))
    print("color of vertices = "+str(cv))
    print("color of spine = "+str(cs))
    print("color of up edges = "+str(cu))
    print("color of down edges = "+str(cd))
    print("color of background = "+str(cb))
    print("orientation of tuple = "+str(orientation))
    print("edge width = "+str(ew))
    print("foreground width = "+str(fw))
    print("foreground color = "+str(cf))
    print("clique orientation in case equal = "+str(cq))     
    print("automatically/manually naming = "+str(name))
    print("-"*25)

def main():
    while True:
        try:
            print("-"*25)
            print("[  1 ] - Draw K(n,2)")
            print("[  2 ] - Draw List of K(n,2)")
            print("[  3 ] - Settings")
            print("[  4 ] - Default Settings")
            print("[  5 ] - Read Settings")
            print("[  0 ] - Quit")
            print("-"*25)
            op = int(input(""))
            if op==0:
                break
            elif op==1:
                n=int(input("n = "))
                t=draw(n)
                plot(t)
            elif op==2:
                i=int(input("i = "))
                f=int(input("f = "))
                for j in range(i,f):
                   t=draw(j)
                   plot(t) 
            elif op==3:
                settings()
            elif op==4:
                dsettings()
            elif op==5:
                read_settings()
            else:
                raise
        except:
            print("Error.....")

    

main()
