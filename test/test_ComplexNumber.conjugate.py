from scr.ComplexAlgebra import ComplexNumber

if __name__ == '__main__':
    z = ComplexNumber(7, -2)
    z = z.conjugate()

    if z.real != 7:
        raise TypeError('Real part is corrupt')

    elif z.imaginary != 2:
        raise TypeError('Imaginary part is corrupt')
