def operations(func):

    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        elif first < second:
            operation = "/"

        return func(first, second, operation)

    return wrapper


@operations
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/":
        return first / second


first_number = float(input("Enter first number: "))

second_number = float(input("Enter second number: "))

result = (calc(first_number, second_number))

print(f"Result is: {result}")
