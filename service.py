def my_input(msg_welcome: str, msg_TypeError: str, msg_ValueError: str):
    # валидация ввода
    successful_input = False
    while not successful_input:
        try:
            buffer = (input(msg_welcome))
            value = float(buffer)
            if my_range(value, 0, 255):
                successful_input = True
            else:
                raise ValueError
        except TypeError:
            print(msg_TypeError)
        except ValueError:
            print(msg_ValueError)
    return value


def my_range(value: float, left: float, right: float):
    # проверка попадания в интервал
    return left <= value <= right
