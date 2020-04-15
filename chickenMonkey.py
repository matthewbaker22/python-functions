count_to_100 = range(1, 101)

for num in count_to_100:
    if num % 5 == 0 and num % 7 == 0:
        print("ChickenMonkey")
    elif num % 5 == 0:
        print('Chicken')
    elif num % 7 == 0:
        print("Monkey")
    else:
        print(num)