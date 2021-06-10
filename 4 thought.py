results = {}
ops = [' + ', ' - ', ' * ', ' // ']
for i in ops:
    for j in ops:
        for k in ops:
            expression = "4{:s}4{:s}4{:s}4".format(i, j, k)
            res = eval(expression)
            results[res] = expression.replace('//', '/') + " = {:d}".format(res)
num=int(input())         
for i in range(num):
    val = int(input())
    if val not in results:
        print("no solution")
    else:
        print(results[val])
