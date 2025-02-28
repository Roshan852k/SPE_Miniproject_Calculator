import math

def print_menu():
    print("========== Scientific Calculator ==========")
    print("1. Square Root (√x)")
    print("2. Factorial (x!)")
    print("3. Natural Logarithm (ln(x))")
    print("4. Power Function (x^b)")
    print("5. Exit")
    print("Enter your choice: ", end="")

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def main():
    while True:
        print_menu()
        try:
            choice = int(input())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 1:
            num = float(input("Enter a number: "))
            if num < 0:
                print("Square root of a negative number not possible.")
            else:
                print("Result:", math.sqrt(num))
        
        elif choice == 2:
            num = int(input("Enter a number: "))
            if num < 0:
                print("Factorial for negative numbers not possible.")
            else:
                print("Result:", factorial(num))
        
        elif choice == 3:
            num = float(input("Enter a number: "))
            if num <= 0:
                print("Natural logarithm for zero or negative numbers not possible.")
            else:
                print("Result:", math.log(num))
        
        elif choice == 4:
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            print("Result:", math.pow(base, exponent))
        
        elif choice == 5:
            print("Exiting the calculator. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")
            
  
if __name__ == "__main__":
    main()
