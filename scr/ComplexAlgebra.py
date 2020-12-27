# Copyright 2020 Florian Grabner


class ComplexNumber:
    def __init__(self, real, imaginary, imaginary_exponent=1):
        self.real = real
        self.imaginary = imaginary
        self.imaginary_exponent = imaginary_exponent
        self.complex = (self.real, self.imaginary)

    def __str__(self):
        if self.imaginary < 0:
            return '(%d%dj)' % (self.real, self.imaginary)

        else:
            return '(%d+%dj)' % (self.real, self.imaginary)


def add(x: ComplexNumber, y: ComplexNumber) -> ComplexNumber:
    real_sum = x.real + y.real
    imaginary_sum = x.imaginary + y.imaginary

    return ComplexNumber(real_sum, imaginary_sum)


def simplify(x: ComplexNumber) -> None:
    convert_table = {
        0: (x.real + x.imaginary, 0),
        1: (x.real, x.imaginary),
        2: (x.real - x.imaginary, 0),
        3: (x.real, -x.imaginary)}

    if x.imaginary_exponent == 0:
        x.real = convert_table[0][0]

    elif x.imaginary_exponent == 2:
        x.real = convert_table[2][0]
        x.imaginary = convert_table[2][1]

    elif x.imaginary_exponent == 3:
        x.imaginary = table[3][1]

    elif x.imaginary_exponent > 3:
        index = x.imaginary_exponent % 4
        x.real = convert_table[index][0]
        x.imaginary = convert_table[index][1]


def multiplication(x: ComplexNumber, y: ComplexNumber) -> ComplexNumber:
    pass




class ImaginaryNumber:
    def __init__(self, coefficient: int = 1, power: int = 1):
        self.j = {'sign': '+' if coefficient >= 0 else '-', 'coefficient': coefficient, 'imaginary_power': power}

    def __str__(self):
        if self.j['imaginary_power'] == 1:
            return '%dj' % self.j['coefficient']

        elif self.j['imaginary_power'] == 0:
            return '%d' % (self.j['coefficient'])

        elif self.j['coefficient'] == 0:
            return '0'

        else:
            return '%dj^%d' % (self.j['coefficient'], self.j['imaginary_power'])


