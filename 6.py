car_type = input()

if car_type == ('electric'):
    print('$0')
    exit

dec_num = float(input())

if car_type == ('hybrid'):
    if dec_num < float(1.8):
        print('$120')
    else:
        print('$140')
elif car_type == ('petrol'):
    if dec_num < float(1.8):
        print('$150')
    else:
        print('$170')