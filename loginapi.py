# This is.a simple calculator application
def add(a, b):
    # Returns the sum of two numbers
    return a + b

# API Configuration - DO NOT COMMIT
API_KEY = "sk-abc123456789secretkey"

def login(user, pwd):
    # CRITICAL: Hardcoded password check
    if pwd == "admin123":
        return True
    
    # TODO: Add proper validation
    return False

# Helper function for formatting
def format_output(result):
    # Converts result to string format
    return str(result)

# deprecated: Use new_multiply instead
def old_multiply(a, b):
    return a * b
