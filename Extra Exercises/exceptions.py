# exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! Idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz.")
except Exception as e:
    print(e)
    print("Something went wrong. _I_")
else:
    print("------")
finally:
    print(result)

