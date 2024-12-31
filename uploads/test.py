def test_function():
    # Simple function to test the debugger
    a = 10
    b = 20
    c = a + b
    print(f"Result of addition: {c}")
    return c

def another_function():
    # Another function to test the debugger with more variables
    x = 30
    y = 40
    z = x * y
    print(f"Result of multiplication: {z}")
    return z

def main():
    test_function()
    another_function()

# Run the main function to trigger the debugging process
if __name__ == "__main__":
    main()
