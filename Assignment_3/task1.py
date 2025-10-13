def factorial(x: int):
    fact = 1
    for i in range(1,x+1):
        fact = fact*i
    return fact

def main():
    x = int(input("Enter a number: "))
    print("Fatorial of",x,"is",factorial(x))

if __name__ == "__main__":
    main()