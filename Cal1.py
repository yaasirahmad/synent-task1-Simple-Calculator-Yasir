# Simple Calculator

print("Simple Calculator")
print("Type 'quit' to exit\n")

while True:
    a = input("First number: ")
    if a == "quit":
        break

    op = input("Operator (+, -, *, /): ")
    if op == "quit":
        break

    b = input("Second number: ")
    if b == "quit":
        break

    # Validate numbers
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("Invalid number! Try again.\n")
        continue

    # Calculate
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("Can't divide by zero!\n")
            continue
        result = a / b
    else:
        print("Invalid operator! Use +, -, *, /\n")
        continue

    # Show result (remove .0 for whole numbers)
    if result == int(result):
        result = int(result)

    print(f"Answer: {result}\n")

print("Goodbye!")