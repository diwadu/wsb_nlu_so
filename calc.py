import sys

def sum(x, y):
    return x + y

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <number1> <number2>.")
        sys.exit(1)

    result = sum(int(sys.argv[1]), int(sys.argv[2]))
    print(result)
