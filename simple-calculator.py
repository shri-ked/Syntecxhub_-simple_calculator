def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Error: Cannot divide by zero."
        return a / b
    else:
        return "Error: Invalid operator."

def main():
    while True:
        print("\n--- Simple Calculator ---")
        print("Enter 'clear' to reset")
        print("Enter 'exit' to quit\n")

        user = input("Enter calculation (example: 5 + 3): ")

        if user == "exit":
            print("Goodbye!")
            break

        if user == "clear":
            print("Cleared.\n")
            continue

        parts = user.split()
        if len(parts) != 3:
            print("Invalid format! Use: number operator number")
            continue

        a = float(parts[0])
        op = parts[1]
        b = float(parts[2])

        result = calculate(a, op, b)
        print("Result:", result)

main()
