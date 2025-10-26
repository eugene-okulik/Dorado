import random


def your_bonus():
    salary = int(input("Enter your salary: "))
    bonus = random.choice([True, False])

    if bonus:
        salary += random.randint(1, 10000)
    return f"'${salary}'"

print(your_bonus())
