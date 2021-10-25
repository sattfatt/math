import numpy as np
import sys

"""
odd case for binary orbit
"""
    


"""
takes integer d and outputs binary orbit vector.
"""


def binary_orbit(d: int) -> None:
    k = (d-1)//2

    def f1(i, j):
        return (d - 2*(k + 1 - i))**((d - 1) - 2*(j)) * (-(k+1-i)*(d-(k+1-i)))**(j-1)

    def f2(j):
        return ((-2)**((d-1)-2*j))

    mat = [[f1(i, j) for j in range(1, k+1)] for i in range(1, k)]
    mat.append([f2(j) for j in range(1,k+1)])
    
    mat = np.longfloat(mat)

    inverse = np.linalg.inv(mat)

    v1 = [0 for k in range(k-1)]
    v1.append(d**(d-3)*d*(d-1)*(d-2))
    vnorm = [0 for k in range(k-1)]
    vnorm.append(d**(d-3))

    result = np.dot(inverse, v1)
    normalized = np.dot(inverse, vnorm)
    return result, normalized


def print_result(result, normalized):
    print("Output:")
    for num in result:
        print(round(num))
    
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
    
