def my_input():
    # валидация ввода
    successful_input = False
    while not successful_input:
        try:
            buffer = (input('Введите пороговое значение на отрезке [0;255]\n'))
            value = float(buffer)
            if my_range(value, 0, 255):
                successful_input = True
            else:
                raise ValueError
        except TypeError:
            print("Неверный тип. Попробуйте снова")
        except ValueError:
            print("Значение некорректно. Попробуйте снова")
    return value


def my_range(value: float, left: float, right: float):
    # проверка попадания в интервал
    return left <= value <= right
