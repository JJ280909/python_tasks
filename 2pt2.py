import math

speed = int(input())

distance = (384400 * 2 + 10921 ) * 1000
print(math.ceil(float(distance / (speed))/3600))