import sys


def factorize(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return f"{num}={i}*{num // i}"
    return f"{num}={num}*1"


def factorize_numbers(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            num = int(line.strip())
            factorization = factorize(num)
            print(factorization)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factorize_numbers(file_path)
