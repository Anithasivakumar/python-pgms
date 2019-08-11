def minl(s,n):
    min=len(s[0])
    for i in range(1,n):
        if len(s[i])<min:
           min=len(s[i])
    return(min)
def commonprefix(s,n):
    minlen=minl(s,n)
    result=""
    for i in range(minlen):
        crn=s[0][i]
        for j in range(1,n):
            if(s[j][i]!=crn):
                return result
        result=result+crn
    return(result)
if __name__=="__main__":
    no=int(input())
    s=[]
    for x in range(0,no):
        ss=str(input())
        s.append(ss)
    n=len(s)
    final=commonprefix(s,n)
    if(len(final)):
        print(final)
    else:
        print("")
