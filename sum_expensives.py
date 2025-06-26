total = 0
expenses = []

for i in range(7):
    expenses.append(float(input('Please put down your cost')))

total = sum(expenses)

print('you spent', total, sep='')