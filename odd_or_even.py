print("Odd or Even")
print("What number are you thinking?")

while True:
    try:
        num = int(input())
        if type(num) == int:
            if num % 2 == 0:
                print("That's an Even Number! Have another?")
            else:
                print("That's an Odd Number! Have another?")

    except ValueError:
         print("Sorry, I didn't understand that. Please insert a whole number!")
         continue