def calc_dollars(**coins):
    penny_price = coins['pennies']/100
    nickel_price = coins['nickels']/20
    dime_price = coins['dimes']/10
    quarter_price = coins['quarters']/4

    dollar_amount = penny_price + nickel_price + dime_price + quarter_price
    print(dollar_amount)

calc_dollars(pennies=342, nickels=9, dimes=32, quarters=4)