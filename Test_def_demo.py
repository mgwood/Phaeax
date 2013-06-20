import time
import mwmath

def is_prime(n):
    return mwmath.is_prime(n)


def is_even(n):
    return n%2==0


def is_odd(n):
    return not is_even(n)


def main():

    print is_prime(3)

    print is_even(3)

    print is_odd(3)


def return_False():

    return is_even(3)
