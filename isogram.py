txt=str(input(""))
txt = txt.lower()
if len(list(txt)) == len(set(txt)):
    print("Yes")
else:
    print("No")
