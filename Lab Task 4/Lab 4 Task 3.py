import heapq

G = {
    'A':[('B',2),('C',4)],
    'B':[('D',3),('E',1)],
    'C':[('E',2)],
    'D':[('G',4)],
    'E':[('G',3)],
    'G':[]
}

H = {'A':6,'B':4,'C':4,'D':2,'E':2,'G':0}

def astar(start,goal,h):
    q=[(h[start],0,start,[])]
    while q:
        f,g,n,p=heapq.heappop(q)
        p=p+[n]
        if n==goal:
            return p,g
        for x,w in G[n]:
            heapq.heappush(q,(g+w+h[x],g+w,x,p))

print("Original:", H)
print("Before:", astar('A','G',H))

H['B']=10

print("Modified:", H)
print("After :", astar('A','G',H))