n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

s1 = n2 - n1
s2 = n3 - n2
s3 = n4 - n3

if s1 == s2 == s3:
    print(s1)
else:
    print('NO')
