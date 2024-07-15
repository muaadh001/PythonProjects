
amount_due = 50


while amount_due > 0:

    print("Amount Due: ", amount_due, sep="")

    coin = int(input("Insert Coin: "))

    if coin in [25, 10, 5]:

        amount_due -= coin


change_owed = abs(amount_due)

print("Change Owed: ", change_owed, sep="")
