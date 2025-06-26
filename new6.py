lemons = int(input())
sugar = int(input())

if lemons >= 20 and sugar >= 3:
    print('A')
elif lemons >= 20 and sugar <= 3:
    print('C')
elif lemons <= 20 and sugar >= 3:
    print('B')
else:
    print('D')

    