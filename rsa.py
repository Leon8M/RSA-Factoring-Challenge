import sys
import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def pollards_rho(n):
    x = random.randint(1, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1

    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(abs(x - y), n)

    return d


def factorize_rsa_number(file_path):
    with open(file_path, 'r') as file:
        num = int(file.readline().strip())
        factor1 = pollards_rho(num)
        factor2 = num // factor1
        print(f"{num}={factor1}*{factor2}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factorize_rsa_number(file_path)
