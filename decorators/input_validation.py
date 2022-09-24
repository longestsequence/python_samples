class InvalidInputError(BaseException):
    pass


def validate(function):
    def new_function(*args, **kwargs):
        for i in args:
            if not isinstance(i, int):
                raise InvalidInputError
        return function(*args, **kwargs)
    return new_function


@validate
def add_numbers(a, b):
    return a+b


if __name__ == "__main__":
    add_numbers(2, 'k')
