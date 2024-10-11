from random import choice

import art


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

calculator_operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}


def perform_operation():
    print(art.logo)
    f_number = float(input("What is your first number?"))
    should_accumulate = True
    while should_accumulate:
        for operations in calculator_operations:
            print(operations)
        operation = input("Pick an operation: ")
        n_number = float(input("What is your second number?"))
        result = calculator_operations[operation](f_number, n_number)
        print(f"{f_number} {operation} {n_number} = {result}")
        input_choice = input(f'''Type 'y' to continue calculating {result}, 
        or type 'n' to start a new calculation 
        or enter 'e' to exit the program: ''').lower()

        if input_choice == "y":
            f_number = result
        elif input_choice == "n":
            should_accumulate = False
            print("\n" *20)
            perform_operation()
        else:
            return
perform_operation()