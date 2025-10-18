saved_number = 13

while True:
    user_input = int(input("Введите цифру: "))
    if user_input == saved_number:
        print("Поздравляю! Вы угадали!")
        break
    elif user_input > saved_number or user_input < saved_number:
        print("Попробуйте снова: ")
        continue
