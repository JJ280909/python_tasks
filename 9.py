cookies = int(input())
guests = int(input())

remain = cookies

while remain > (cookies // 2) and guests > 0 and remain >= 2:
    remain -= 2
    guests -= 1
    
while remain > 0 and guests > 0:
    remain -= 1
    guests -= 1

print(remain)



    

