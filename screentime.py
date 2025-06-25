arrival = int(input())
bed = int(input())
homework = int(input())
dinner = int(input())

minarrival = arrival * 60 
minbed = bed * 60

screentime = minbed - ((minarrival + (homework * 35) + dinner)) - 60

print(screentime)
