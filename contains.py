a = str(input("Type here the text : "))
b = str(input("Type here letter to be found in previous input :"))
if b in a:
    print( b, "- is present in typed text ")
elif b not in a:
    print( b, "-  is not present in typed text ")
