import math


n=float(input("Enter a number: "))

def calc(n):
    Square_root=math.sqrt(n)
    logarithm= math.log(n)
    Sine= math.sin(n)
    return {
        "Square Root": Square_root,
        "Logarithm": logarithm,
        "Sine": Sine
    }


print(calc(n))
