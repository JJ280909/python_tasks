#get details
money_owed = float(input('How much money do you owe?\n'))   #50,000
apr = float(input('what is the annual percentage rate of the loan?\n')) # 3%
payment = float(input('how much will you pay of each month?\n')) #1,000
months = int(input('how many months do you want to see results in?\n')) #24

monthly_rate = apr/100/12

#calc interest to pay
interest_paid = money_owed * monthly_rate

for i in range(months):
    #add interest
    money_owed = money_owed + interest_paid
    if (money_owed - payment < 0):
        print('the last payment is', money_owed)
        print('you payed off the loan in', i + 1, 'months')
        break
    #make payment
    money_owed = money_owed - payment

    print('payed', payment, 'of which', interest_paid, 'was interest')
    print('now i owe', money_owed)