from scr.ComplexAlgebra import ComplexNumber, division
from random import randint

if __name__ == '__main__':
    for i in range(10000):
        z1_real = randint(1, 100)
        z1_imaginary = randint(1, 100)

        z2_real = randint(1, 100)
        z2_imaginary = randint(1, 100)

        z1 = ComplexNumber(z1_real, z1_imaginary)
        z2 = ComplexNumber(z2_real, z2_imaginary)

        z_quotient = division(z1, z2)
        test_quotient = complex(z1_real, z1_imaginary) / complex(z2_real, z2_imaginary)

        if round(z_quotient.real, 10) != round(test_quotient.real, 10) or \
                round(z_quotient.imaginary, 10) != round(test_quotient.imag, 10):
            raise TypeError(f"Function 'division' is corrupt")
