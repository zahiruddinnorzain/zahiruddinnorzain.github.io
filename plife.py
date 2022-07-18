code = input("What? ")
print ("code: " + code)

temp = ""
out = ""

temp = code.encode("ascii").hex()
# 14 char only
temp = temp[:14]

b1 = 'Za'
b3 = '@912'
out+=str(b1+temp+b3)
print( "length: " + str(len(out)) )
print(out)
