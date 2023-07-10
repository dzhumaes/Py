import re


class CheckList(Exception):
    def __init__(self, value):
        self.value = value
        self.result = CheckList.__check_value(value)

    @staticmethod
    def __check_value(value):
        return re.match(r'^[+-]?\d+([,.]?\d+)*\d*$', value)

    def __str__(self):
        if self.result:
            return f'Введено число {self.value}'
        else:
            return f'Введенное значение "{self.value}" не является числом'


if __name__ == '__main__':
    list_out = []
    while True:
        resp = input('Введите число (для выхода введите stop): ')
        try:
            if resp != 'stop':
                raise CheckList(resp)
        except CheckList as check:
            if check.result:
                list_out.append(resp)
            else:
                print(check)
        else:
            print(list_out)
            break