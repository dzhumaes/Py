from abc import ABC
from typing import List, Dict


class OfficeEquip(ABC):

    def __init__(self, model: str = 'Unnamed'):
        self.model = model


class Printer(OfficeEquip):

    def __init__(self, model: str = 'Unnamed', is_color: bool = False):
        super(Printer, self).__init__(model)
        self.is_color = is_color

    def printing(self):
        if self.is_color:
            print(f'печать на принтере {self.model} в цвете')
        else:
            print(f'печать на принтере {self.model} в ч/б')


class Scanner(OfficeEquip):

    def scanning(self):
        print(f'сканирование на {self.model}')


class Xerox(OfficeEquip):

    def copying(self):
        print(f'копирование на {self.model}')


class Storage:

    def __init__(self):
        self._storage_printers: Dict = {}
        self._storage_scanners: Dict = {}
        self._storage_xeroxs: Dict = {}

    def add(self, device: OfficeEquip):

        if not isinstance(device, OfficeEquip):
            raise ValueError(f'Недопустимый класс - {device.__class__.__name__}')

        elif isinstance(device, Printer):
            if device.model in self._storage_printers:
                self._storage_printers[device.model] += 1
            else:
                self._storage_printers[device.model] = 1

        elif isinstance(device, Scanner):
            if device.model in self._storage_printers:
                self._storage_scanners[device.model] += 1
            else:
                self._storage_scanners[device.model] = 1

        elif isinstance(device, Xerox):
            if device.model in self._storage_printers:
                self._storage_xeroxs[device.model] += 1
            else:
                self._storage_xeroxs[device.model] = 1

    def move_to_office(self, device: OfficeEquip):

        if not isinstance(device, OfficeEquip):
            raise ValueError(f'Недопустимый класс - {device.__class__.__name__}')

        elif isinstance(device, Printer):
            if device.model in self._storage_printers:
                if self._storage_printers[device.model] > 1:
                    self._storage_printers[device.model] -= 1
                else:
                    self._storage_printers.pop(device.model)

        elif isinstance(device, Scanner):
            if device.model in self._storage_scanners:
                if self._storage_scanners[device.model] > 1:
                    self._storage_scanners[device.model] -= 1
                else:
                    self._storage_scanners.pop(device.model)

        elif isinstance(device, Xerox):
            if device.model in self._storage_xeroxs:
                if self._storage_xeroxs[device.model] > 1:
                    self._storage_xeroxs[device.model] -= 1
                else:
                    self._storage_xeroxs.pop(device.model)

    def __str__(self):
        return f'На складе в наличии: \n Принтеры: {self._storage_printers}\n Сканеры: {self._storage_scanners}\n' \
               f' Ксероксы: {self._storage_xeroxs}\n'


if __name__ == '__main__':

    printer = Printer('Toshiba', True)
    printer_2 = Printer('Hp', True)
    printer.printing()
    printer.is_color = False
    printer.printing()
    scanner = Scanner('Samsung')
    scanner.scanning()
    xerox = Xerox()
    storage = Storage()
    storage.add(xerox)
    storage.add(printer)
    storage.add(printer_2)
    print(storage)
    storage.move_to_office(printer)
    print(storage)