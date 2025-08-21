while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        print("Loop stopped.")
        break
    elif number % 2 == 0:
        print("Even!")
    else:
        print("Odd!")
