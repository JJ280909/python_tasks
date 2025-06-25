

coin = 0
lst = []
def coinchange():
    while True:
        coin = int(input("Coins?"))
        lst.append(coin)
        if coin == -1:
            add = sum(lst)
            hours = int((add/60) * 30)
            print(hours)
            exit()

coinchange()