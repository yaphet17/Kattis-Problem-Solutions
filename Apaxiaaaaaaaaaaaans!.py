string=[i for i in input()]
output=[]
for i in range(len(string)):
    if(i==len(string)-1):
        output.append(string[i])
        break
    if(string[i]!=string[i+1]):
        output.append(string[i]) 
for i in output:
    print(i,end="")
