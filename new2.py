d1 = int(input())
d2 = int(input())
d3 = int(input())

tot = d1 + d2 + d3
ans = 180 - tot

if tot < 180:
    print(ans)
else:
    print('this number is impossible to achieve')

    
