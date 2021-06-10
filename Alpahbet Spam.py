string=input()
n=len(string)
whitespace=0
lowercase=0
uppercase=0
symbols=0
for i in string:
    if(i=='_'):
        whitespace+=1
        continue
    if(i.isalpha()):
        if(ord(i)>=65 and ord(i)<=90):
            uppercase+=1
            continue
        if(ord(i)>=97 and ord(i)<=122):
            lowercase+=1
            continue
       
    if(ord(i)>=33 and ord(i)<=126):
        symbols+=1
print(round(whitespace/n,13))
print(round(lowercase/n,13))
print(round(uppercase/n,13))
print(round(symbols/n,13))
