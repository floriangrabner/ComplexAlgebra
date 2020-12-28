from scr.ComplexAlgebra import ComplexNumber

if __name__ == '__main__':
    z = ComplexNumber(2, 1)

    if str(z) != '(2+1j)':
        raise TypeError("'__str__' method is corrupt")
