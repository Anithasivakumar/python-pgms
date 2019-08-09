k=int(input())
for i in range(1<<k):
    s=bin(i)[2:]
    s="0"*(k-len(s))+s
    print(s)
