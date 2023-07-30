amount_due = 50

while amount_due > 0:
    print("Amount Due:", amount_due)
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        amount_due -= coin
    else:
        continue
change = amount_due * -1
print("Change Owed:", change)
