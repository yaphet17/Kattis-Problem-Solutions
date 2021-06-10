n=int(input())
tp=0
prices=[]
pt=[]
totalP=0
for i in range(n):
    price=int(input())
    prices.append(price)
if(len(prices)%3!=0):
    prices.append(0)
    prices.append(0)
for i in range(int(n)):
    if(len(prices)!=0):
        pt.append(list((prices.pop(prices.index(max(prices))),prices.pop(prices.index(max(prices))),prices.pop(prices.index(max(prices))))))
for i in range(len(pt)):
   totalP+=pt[i].pop(pt[i].index(max(pt[i])))+pt[i].pop(pt[i].index(max(pt[i])))
print(totalP)
