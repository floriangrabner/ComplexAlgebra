# Copyright 2020 Florian Grabner


class ComplexNumber:
    def __init__(self, real, imaginary, imaginary_exponent=1):
        self.real = real
        self.imaginary = imaginary
        self.imaginary_exponent = imaginary_exponent
        self.complex = (self.real, self.imaginary)

    def simplify(self):
        convert_table = {
            0: (self.real + self.imaginary, 0),
            1: (self.real, self.imaginary),
            2: (self.real - self.imaginary, 0),
            3: (self.real, - self.imaginary)}

        index = self.imaginary_exponent % 4
        self.real = convert_table[index][0]
        self.imaginary = convert_table[index][1]

    def __str__(self):
        if self.imaginary < 0:
            return '(%d%dj)' % (self.real, self.imaginary)

        else:
            return '(%d+%dj)' % (self.real, self.imaginary)


def addition(x: ComplexNumber, y: ComplexNumber) -> ComplexNumber:
    real_sum = x.real + y.real
    imaginary_sum = x.imaginary + y.imaginary

    return ComplexNumber(real_sum, imaginary_sum)


def subtraction(x: ComplexNumber, y: ComplexNumber) -> ComplexNumber:
    real_sum = x.real - y.real
    imaginary_sum = x.imaginary + y.imaginary

    return ComplexNumber(real_sum, imaginary_sum)


def multiplication(x: ComplexNumber, y: ComplexNumber) -> ComplexNumber:
    z1 = ComplexNumber(x.real * y.real, x.real * y.imaginary)
    z2 = ComplexNumber(0, x.imaginary * y.real)
    z3 = ComplexNumber(0, x.imaginary * y.imaginary, x.imaginary_exponent + y.imaginary_exponent)
    z3.simplify()

    return addition(addition(z1, z2), z3)


def division(x: ComplexNumber, y: ComplexNumber) -> ComplexNumber:
    pass
