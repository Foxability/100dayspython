from calculator_art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }

def calculator():

    print(logo)

    temp_answer = float(input("What's the first number?: "))

    for symbol in operations:
            print(symbol)

    should_stop = False

    while not should_stop:
        
        operation_symbol = input("Pick an operation from the line above: ")
        next_num = float(input("What's the next number?: "))
        answer = operations[operation_symbol](temp_answer, next_num)
        print(f"{temp_answer} {operation_symbol} {next_num} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start over.").lower() == 'n':
             should_stop = True 
             calculator()
        else:
            temp_answer = answer

calculator()




