def print_text(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("finished")

        return result

    return wrapper


@print_text
def example(text):
    print(text)


example("print me")
