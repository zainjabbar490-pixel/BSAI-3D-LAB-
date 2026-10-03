import heapq

G={'A':[('B',2),('C',4)],'B':[('D',3),('E',1)],
'C':[('E',2)],'D':[('G',4)],'E':[('G',3)],'G':[]}

H={'A':6,'B':4,'C':4,'D':2,'E':2,'G':0}

def search(s,t,h):
    q=[(h[s],0,s)]
    seen=[]
    while q:
        f,g,n=heapq.heappop(q)
        if n in seen: continue
        seen.append(n)
        if n==t: return seen,g
        for x,w in G[n]:
            heapq.heappush(q,(g+w+h[x],g+w,x))
        
print("A* :",search('A','G',H))
print("UCS:",search('A','G',{x:0 for x in G}))