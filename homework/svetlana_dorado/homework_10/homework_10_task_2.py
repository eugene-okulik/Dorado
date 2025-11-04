def function_launches(func):

    def wrapper(*args, **kwargs):
        count = kwargs.pop("count", 1)

        for i in range(count):
            result = func(*args, **kwargs)

        return result

    return wrapper


@function_launches
def example(text):
    print(text)


example("print me", count=2)
