from fractions import gcd

args = input("Numers: ")

def GCD(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcmm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def LCM(args):
    """Return lcm of args."""
    return reduce(lcmm, args)

LCM(args)
