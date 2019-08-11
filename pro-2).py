from itertools import combinations
s,a=map(int,input().split())
t=len(str(s))
l=list(combinations(str(s),t-a))
l=sorted(l)
print(*l[0],sep='')
