season = input()
jump = int(input())

year = ['spring', 'summer', 'autumn', 'winter']

for i,item  in enumerate(year):
    if season == item:
        if(i + jump < len(year)):
            new_season = year[i + jump]
        else:
            new_season = year[(i+jump)%len(year)]
        break

print(new_season)
# while True:
#     for item in year:
#         if season == item:


#         current_item = year[year.index(item)]
#         try:
#             next_item = year[year.index(item) + 1]
#         except IndexError:
#             next_item = year[0]
        