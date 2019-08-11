p=int(input())
q=list(map(int,input().split()))[0:p]
q.sort(reverse=True)
i=0
while i<p:
    print(q[i],end="\n")
    i+=1
