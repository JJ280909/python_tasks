bolt1 = int(input())
bolt2 = int(input())
current = int(input())

if abs(bolt1 - current) > abs(bolt2 - current):
    print(abs(bolt2 - current))
else:
    print(abs(bolt1 - current))


