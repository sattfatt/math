import numpy as np
from mpmath import mp
import sys

"""
odd case for binary orbit
"""
    


"""
takes integer d and outputs binary orbit vector.
"""
mp.dps=1000000

def binary_orbit(d: int) -> None:
    k = (d-1)//2
    d_f = mp.mpf(d)
    k_f = mp.mpf(k)
    one = mp.mpf(1)
    two = mp.mpf(2)

    def f1(i, j):

        return mp.mpf((d_f - two*(k_f + one - i))**((d_f - one) - two*(j)) * (-(k_f+one-i)*(d_f-(k_f+one-i)))**(j-one))

    def f2(j):
        return mp.mpf((mp.mpf(-2)**((d_f-one)-two*j)))

    mat = [[f1(mp.mpf(i), mp.mpf(j)) for j in range(1, k+1)] for i in range(1, k)]
    mat.append([f2(mp.mpf(j)) for j in range(1,k+1)])
    
    mat = mp.matrix(mat);

    
    inverse = mat**-1

    v1 = [0 for k in range(k-1)]
    v1.append(d**(d-3)*d*(d-1)*(d-2))
    vnorm = [0 for k in range(k-1)]
    vnorm.append(d**(d-3))

    v1 = mp.matrix(v1)
    vnorm = mp.matrix(vnorm)

    result = inverse * v1
    normalized = inverse * vnorm
    return result, normalized


def print_result(result, normalized):
    print("Output:")
    for num in result:
        print(num)
    
    print()

    print("Normalized:")
    for num in normalized:
        print(round(num))

def print_to_file(filename="output.txt"):
    f = open(filename, "w")
    print("Output:", file=f)
    print(*result, sep=",", file=f)
    print(file=f)

if __name__ == '__main__':
    # get the first argument
    if len(sys.argv) < 2:
        print("Please specify an integer: ./BinaryOrbit.py <integer>")
        sys.exit()

    input = ""
    try:
        input = int(sys.argv[1])
    except(ValueError):
        print("Enter an integer ya dummy!")
        sys.exit()

    if input < 3:
        print("Input needs to be >= 3.")
        sys.exit()

    result, normalized = binary_orbit(input)
    
    print_result(result, normalized)
    
