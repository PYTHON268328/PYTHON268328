import math
while True:
    q = input("What operation would you like to perform (please enter full name)?\nSupported operations: addition, subtraction, multiplication, division, square root, cube root,
    power: ")

    # Check if the input operation is supported
    if q not in ["addition", "subtraction", "multiplication", "division", "square root", "cube root", "power"]:
        print("Operation not available")
    else:
        # Perform the selected operation
        if q == "addition":
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print("Adding", x, "and", y, "results in:", x + y)
        
        elif q == "subtraction":
            r = float(input("Enter the first number: "))
            t = float(input("Enter the second number: "))
            print("Subtracting", t, "from", r, "results in:", r - t)
        elif q == "multiplication":
            u = float(input("Enter the first number: "))
            i = float(input("Enter the second number: "))
            print("Multiplying", u, "and", i, "results in:", u * i)
        
        elif q == "division":
            o = float(input("Enter the numerator: "))
            p = float(input("Enter the denominator (not equal to 0): "))
            if p != 0:
                print("Dividing", o, "by", p, "results in:", o / p)
            else:
                print("Cannot divide by zero!")
        
        elif q == "square root":
            a = float(input("Enter the number to find its square root: "))
            if a >= 0:
                print("The square root of", a, "is:", math.sqrt(a))
            else:
                print("Cannot find square root of negative number!")
             
        elif q == "cube root":
            m = float(input("Enter the number to find its cube root: "))
            if m >= 0:
                print("The cube root of", m, "is:", m ** (1 / 3))
            else:
                print("Cannot find cube root of negative number!")

        elif q == "power":
            d = float(input("Enter the number: "))
            f = float(input("Enter the power: "))
            print(d, "raised to the power", f, "results in", d ** f)

    choice = input("Do you want to perform another operation? (yes/no): ")
    if choice.lower() != "yes":
        break



