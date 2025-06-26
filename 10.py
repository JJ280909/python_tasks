stam = int(input())
stren = int(input())
track = input().split('_')[1:-1]

count = 0

for hurdle in track:
    if len(hurdle) > stren:
        break
    count =+ 1
    if len(hurdle) > stam:
        break
    print(count)

