G={'A':[('B',2),('C',4)],'B':[('D',3),('E',1)],
'C':[('E',2)],'D':[('G',4)],'E':[('G',3)],'G':[]}

h={'A':6,'B':4,'C':4,'D':2,'E':2,'G':0}

def astar(s,t):
    q=[(h[s],0,s,[s])]
    while q:
        f,g,n,p=q.pop(0)
        if n==t:return p,g
        for x,w in G[n]:
            q.append((g+w+h[x],g+w,x,p+[x]))
        q.sort()

print("A* =",astar('A','G'))