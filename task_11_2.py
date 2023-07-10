class ZeroExcept(Exception):

    @staticmethod
    def divide_by_zero(args: str):
        try:
            dividend, divide = map(float, args.split())
            if not divide:
                if not dividend == 0:
                    raise ZeroExcept('Деление на ноль')

            return True

        except ZeroExcept as error:
            print(error)
            return False


def protected_division(arg: str) -> float:
    main_err = ZeroExcept.divide_by_zero(arg)

    if main_err:
        dividend, divide = map(float, arg.split())
        return dividend / divide
    else:
        pass


if __name__ == '__main__':
    inp = input('Введите делимое и делитель через пробел: ')

    print(protected_division(inp))