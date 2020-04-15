dollar_amount = 8.69

piggy_bank = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0
}

coin_values = {
    "quarters": .25,
    "dimes": .1,
    "nickels": .05,
    "pennies": .01
}

def convert_to_coins(amount, bank, coin_values):
    for key in bank:
        while amount + 0.01 > coin_values[key]:
            bank[key] += 1
            amount -= coin_values[key]

convert_to_coins(dollar_amount, piggy_bank, coin_values)
print(piggy_bank)
