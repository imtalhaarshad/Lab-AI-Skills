# Common Python Error Patterns and Fixes

This reference contains common Python error patterns and their typical fixes while preserving code style.

## Syntax Errors

### Missing Colon
**Problem:**
```python
def my_function(x)
    return x * 2
```

**Fix:**
```python
def my_function(x):  # Add the missing colon
    return x * 2
```

### Indentation Error
**Problem:**
```python
def my_function(x):
return x * 2
```

**Fix:**
```python
def my_function(x):
    return x * 2  # Add proper indentation
```

### Mismatched Parentheses
**Problem:**
```python
result = calculate(1, 2, 3
```

**Fix:**
```python
result = calculate(1, 2, 3)  # Add closing parenthesis
```

### Missing Quotes
**Problem:**
```python
name = John
```

**Fix:**
```python
name = "John"  # Add quotes around string
```

## Runtime Errors

### Division by Zero
**Problem:**
```python
def calculate_average(total, count):
    return total / count
```

**Fix:**
```python
def calculate_average(total, count):
    if count == 0:
        return 0  # or raise an exception
    return total / count
```

### Index Out of Range
**Problem:**
```python
def get_item(items, index):
    return items[index]
```

**Fix:**
```python
def get_item(items, index):
    if 0 <= index < len(items):
        return items[index]
    else:
        return None  # or raise an exception
```

### Undefined Variable
**Problem:**
```python
def calculate():
    result = x + 5  # x is not defined
    return result
```

**Fix:**
```python
def calculate(x):  # Accept x as parameter
    result = x + 5
    return result
```

## Logic Errors

### Off-by-One Error
**Problem:**
```python
def print_numbers(n):
    for i in range(n+1):  # This will print 0 to n, maybe not intended
        print(i)
```

**Fix:**
```python
def print_numbers(n):
    for i in range(n):  # This will print 0 to n-1
        print(i)
```

### Wrong Operator
**Problem:**
```python
def is_equal(a, b):
    return a = b  # Assignment instead of comparison
```

**Fix:**
```python
def is_equal(a, b):
    return a == b  # Use equality operator
```

## Best Practices for Error Fixes

### Preserve Original Style
- Keep variable names unchanged
- Maintain original function signatures
- Keep original comments
- Preserve original code structure

### Minimal Changes
- Only fix what's broken
- Don't refactor unnecessarily
- Don't improve code beyond fixing the error
- Don't add features unless required for the fix

### Error Handling Patterns
- Use defensive programming where appropriate
- Add boundary checks for array/list access
- Handle edge cases that could cause runtime errors
- Maintain the original function's contract