from scr.ComplexAlgebra import ComplexNumber, multiplication
from random import randint

if __name__ == '__main__':
    for i in range(10000):
        z1_real = randint(-100, 100)
        z1_imaginary = randint(-100, 100)

        z2_real = randint(-100, 100)
        z2_imaginary = randint(-100, 100)

        z1 = ComplexNumber(z1_real, z1_imaginary)
        z2 = ComplexNumber(z2_real, z2_imaginary)

        z_product = multiplication(z1, z2)
        test_product = complex(z1_real, z1_imaginary) * complex(z2_real, z2_imaginary)

        if z_product.real != test_product.real or z_product.imaginary != test_product.imag:
            raise TypeError(f"Function 'multiplication' is corrupt")
