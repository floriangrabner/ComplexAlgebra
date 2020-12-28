from scr.ComplexAlgebra import ComplexNumber

if __name__ == '__main__':
    z = ComplexNumber(real=2, imaginary=1, imaginary_exponent=2)
    z.simplify()

    if z.real != 1:
        raise TypeError('Real part is corrupt')

    elif z.imaginary != 0:
        raise TypeError('Imaginary part is corrupt')

    elif z.imaginary_exponent != 1:
        raise TypeError('Imaginary exponent is corrupt')
