def fibonacci_numbers():
    f1 = 0
    f2 = 1
    while True:
        yield f1
        sum_numbers = f1 + f2
        f1 = f2
        f2 = sum_numbers


def generator(n):
    number_generator = fibonacci_numbers()
    for i in range(n):
        result = next(number_generator)
    return result


print(f"Number 5 is: {generator(5)}")
print(f"Number 200 is: {generator(200)}")
print(f"Number 1000 is: {generator(1000)}")
print(f"Number 100000 is: {generator(100000)}")
