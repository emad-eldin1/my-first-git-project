# calculator.py
def add(a, b):
    """Add two numbers and return the result"""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result"""
    return a - b

# Basic test cases
if __name__ == "__main__":
    print(f"Adding 5 and 3: {add(5, 3)}")          # Should output 8
    print(f"Subtracting 10 and 4: {subtract(10, 4)}")  # Should output 6
     
