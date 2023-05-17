import random


def licensePlate(abbrev, digits):
    plate = abbrev + "-"
    for i in range(digits):
        plate = plate + random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')


    return plate


print('Ask user to enter state abbreviation')
abbrev = input()

print('Ask user to enter the number of digits the plate has')
digits = int(input())

plate = licensePlate(abbrev, digits)
print(plate)

ans = 'y'
while ans == 'y':
    print('Ask user to enter state abbreviation')
    abbrev = input()

    print('Ask user to enter the number of digits the plate has')
    digits = int(input())

    plate = licensePlate(abbrev, digits)
    print(plate)

    print('again? (y/n):')
    ans = input()



