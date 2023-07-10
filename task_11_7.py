class ComplexNum:
    def __init__(self, num: complex):
        if isinstance(num, complex):
            self.num = num
        else:
            raise ValueError('Некорректный формат числа')

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num


if __name__ == '__main__':
    a = ComplexNum(5+1j)
    b = ComplexNum(6+3j)
    print(a + b)
    print(a * b)