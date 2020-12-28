from scr.ComplexAlgebra import ComplexNumber

z = ComplexNumber(real=2, imaginary=1, imaginary_exponent=2)
z.simplify()

if __name__ == '__main__':

    if z.real != 1:
        raise TypeError('Real part has a wrong value')

    elif z.imaginary != 0:
        raise TypeError('Imaginary part has a wrong value')

    elif z.imaginary_exponent != 1:
        raise TypeError('Imaginary exponent has a wrong value')
