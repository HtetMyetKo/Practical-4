import random

MINIMUM_PICK = 1
MAXIMUM_PICK = 45

NUMBERS = 6

def main():
    """"Quick Pick" Lottery Ticket Generator"""
    
    quick_picks = int(input("How many quick picks ? "))

    while quick_picks < 0:
        print("Invalid. Please retry")

        quick_picks = int(input("How many quick picks? "))

    for i in range(quick_picks):
        data = []
        for j in range(NUMBERS):
            number = random.randint(MINIMUM_PICK, MAXIMUM_PICK)

            while number in data:
                number = random.randint(MINIMUM_PICK, MAXIMUM_PICK)
            data.append(number)

        data.sort()
        print(" " .join("{:2}".format(number) for number in data))



main()