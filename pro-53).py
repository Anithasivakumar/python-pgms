from string import ascii_lowercase as asc_lower
def check(word):
    return set(asc_lower)-set(word.lower())==set([])
w1=str(input(""))
if(check(w1)==True):
    print("yes")
else:
    print("no")
