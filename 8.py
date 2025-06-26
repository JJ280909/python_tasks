exdate = int(input())
num = 0

while True:
    fruit = int(input())
    if fruit == -1:
        break 
    if fruit >= exdate:
        num =+ 1
print(num)

          