def operation_result(*args):
    for arg in args:
        number = int(arg.split(":")[-1].strip())
        result = number + 10
        print(result)


operation_result(
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 22"
)
