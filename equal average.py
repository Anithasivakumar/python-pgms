n=int(input())
a=(input().split())[0:n]
s=n//2
if n>3:
  if(s%2==0):
    print("yes")
  else:
    print("no")
else:
  if(n==3):
    print("yes")
  else:
    print("no")
