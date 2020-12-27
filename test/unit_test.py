import ComplexAlgebra
from ComplexAlgebra import ComplexNumber

z1 = ComplexNumber(2, 1)
z2 = ComplexNumber(3, 1)

z3 = ComplexAlgebra.add(z1, z2)
print(z3)

z1 = complex(2, 1)
z2 = complex(3, 1)

z3 = z1 * z2

x = ComplexNumber(2, 1, 1)
ComplexAlgebra.simplify(x)
print(x)

x = ComplexNumber(0, 2, 2)
ComplexAlgebra.simplify(x)
print(x)

