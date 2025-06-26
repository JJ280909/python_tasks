contacts = {
    'number' : 4,
    'students': 
        [
            {'Name':'Sarah Holdings', 'email': 'ssh@gmail.com'},
            {'Name': 'Harry Potter', 'email': 'hp@fmail.xom'},
            {'Name': 'Ron Weasly', 'email': 'rw@gmail.com'},
            {'Name': 'Hermoine Granger', 'email': 'hg@gmail.com'}


        ]

}

print('Student Email:')
for student in contacts['students']:
    print(student['email'])
