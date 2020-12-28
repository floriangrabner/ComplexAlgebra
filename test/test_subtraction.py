from scr.ComplexAlgebra import ComplexNumber, subtraction
from random import randint

if __name__ == '__main__':
    for i in range(10000):
        z1_real = randint(-100, 100)
        z1_imaginary = randint(-100, 100)

        z2_real = randint(-100, 100)
        z2_imaginary = randint(-100, 100)

        z1 = ComplexNumber(z1_real, z1_imaginary)
        z2 = ComplexNumber(z2_real, z2_imaginary)

        z_difference = subtraction(z1, z2)
        test_difference = complex(z1_real, z1_imaginary) - complex(z2_real, z2_imaginary)

        if z_difference.real != test_difference.real or z_difference.imaginary != test_difference.imag:
            raise TypeError(f"Function 'subtraction' is corrupt")
