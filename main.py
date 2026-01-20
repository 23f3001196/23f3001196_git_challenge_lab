from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def main():
    a = 10
    b = 5

    print(f"Addition of {a} and {b}: {add(a, b)}")
    print(f"Subtraction of {a} and {b}: {subtract(a, b)}")
    print(f"Multiplication of {a} and {b}: {multiply(a, b)}")
    print(f"Division of {a} and {b}: {divide(a, b)}")


main()
