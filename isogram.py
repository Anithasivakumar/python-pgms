txt=str(input(""))
txt = txt.lower()
if len(list(txt)) == len(set(txt)):
    print("yes")
else:
    print("no")
