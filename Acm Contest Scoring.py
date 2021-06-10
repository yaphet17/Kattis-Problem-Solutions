data=[]
minute=0
solved=0

def check(i,c):
    count=0
    for j in range(i):
        if(data[j][1]!=c):
            continue
        if(data[j][2].lower()=="wrong"):
            count+=1
    return count
while True:
    line=input()
    if(int(list(line.split())[0])==-1):
        break
    data.append(tuple(line.split()))
for i in range(len(data)):
   if(data[i][2].lower()=="right"):
       minute+=int(data[i][0])
       solved+=1
       minute+=(check(i,data[i][1])*20)
print(solved," ",minute)
    
