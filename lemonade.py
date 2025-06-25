lem = int(input())
sug = int(input())

if lem >= 20 and sug >=3:
    print('A')
elif lem < 20 and sug >= 3:
    print('B')
elif lem >= 20 and sug < 3:
    print('C')
else:
    print('D')