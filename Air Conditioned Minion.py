def rooms(l):
    counter = 0
    while l:
        counter += 1
        a,b = l.pop()
        while l and (a <= l[-1][0] <= b or a <= l[-1][1] <= b):
            A,B = l.pop()
            a = max(a,A)
            b = min(b,B)
    return counter
def do():
    num= int(input())
    ls=sorted((tuple(map(int,input().split())) for _ in range(num)),reverse=True)
    print(rooms(ls))

do()
