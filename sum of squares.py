j=int(input())
sum=0
while(j>0):
    r=j%10
    sum=sum+r*r
    j=j//10
print(sum)
