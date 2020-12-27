# Copyright 2020 Florian Grabner


class ComplexNumber:
    def __init__(self, real, imaginary, imaginary_exponent=1):
        self.real = real
        self.imaginary = imaginary
        self.imaginary_exponent = imaginary_exponent
        self.complex = (self.real, self.imaginary)

    def simplify(self):
        """
        This method simplifies complex numbers and changes the attributes of the given object
        E.g.: z = ComplexNumber(real=2, imaginary=1, imaginary_exponent=2)
        ... z.simplify() -> (1+0j)

        :return: None
        """

        # dictionary of all possible sates of i
        convert_table = {
            0: (self.real + self.imaginary, 0),
            1: (self.real, self.imaginary),
            2: (self.real - self.imaginary, 0),
            3: (self.real, - self.imaginary)}

        # The value of the modulo operation specifies the exponent of the imaginary number
        index = self.imaginary_exponent % 4
        self.real = convert_table[index][0]
        self.imaginary = convert_table[index][1]

    def conjugate(self):
        """
        This method returns the conjugation of the specified complex number
        :return: <class 'ComplexAlgebra.ComplexNumber'>
        """
        return ComplexNumber(self.real, self.imaginary * -1)

    def __str__(self):
        if self.imaginary < 0:
            return f'({self.real}{self.imaginary}j)'

        else:
            return f'({self.real}+{self.imaginary}j)'


def addition(x: ComplexNumber, y: ComplexNumber) -> ComplexNumber:
    real_sum = x.real + y.real
    imaginary_sum = x.imaginary + y.imaginary

    return ComplexNumber(real_sum, imaginary_sum)


def subtraction(x: ComplexNumber, y: ComplexNumber) -> ComplexNumber:
    real_difference = x.real - y.real
    imaginary_difference = x.imaginary + y.imaginary

    return ComplexNumber(real_difference, imaginary_difference)


def multiplication(x: ComplexNumber, y: ComplexNumber) -> ComplexNumber:
    """
    This function multiplies two complex numbers and returns it's product
    :param x: Any complex number
    :param y: Any complex number
    :return: <class 'ComplexAlgebra.ComplexNumber'>
    """
    z1 = ComplexNumber(x.real * y.real, x.real * y.imaginary)
    z2 = ComplexNumber(0, x.imaginary * y.real)
    z3 = ComplexNumber(0, x.imaginary * y.imaginary, x.imaginary_exponent + y.imaginary_exponent)
    z3.simplify()
    product = addition(addition(z1, z2), z3)

    return product


def division(x: ComplexNumber, y: ComplexNumber) -> ComplexNumber:
    """
    This function divides two complex numbers and returns it's quotient
    :param x: numerator -> Any complex number
    :param y: denominator -> Any complex number
    :return:
    """

    z_conj = y.conjugate()
    numerator = multiplication(x, z_conj)
    denominator = y.real * y.real + y.imaginary * y.imaginary
    quotient = ComplexNumber(numerator.real/denominator, numerator.imaginary/denominator)

    return quotient
