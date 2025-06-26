current_movies = {'The grinch': '11:00am',
                  'Rudolph' : '12:00am',
                   'Frosty the Snowman' : '1:00pm',
                    'Christmas Vacation' : '5:00pm' }


print('We are currently showing the following movies:')
for key in current_movies:
    print(key)
ques = input('What movie do you want to recieve the showtime for?\n')

showtime = current_movies.get(ques)

if showtime == None:
    print('That movie is not on the list, make sure you are spelling it right.')
else:
    print(ques, 'is playing at', showtime)