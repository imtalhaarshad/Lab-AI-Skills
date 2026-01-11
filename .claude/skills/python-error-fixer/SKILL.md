---
name: python-error-fixer
description: Identify and fix Python code errors while preserving the original code's tone, style, and intent. Use when Claude encounters Python syntax errors, runtime errors, logical errors, or any other Python-related issues that need resolution without changing the fundamental approach or style of the code.
---

# Python Error Fixer

## Overview

This skill helps identify and fix Python code errors while maintaining the original code's tone, style, and intent. The focus is on resolving errors without altering the code's fundamental approach or changing its personality.

## Error Identification and Resolution Process

When presented with Python code containing errors:

1. **Analyze the error** - Identify the specific type of error (syntax, runtime, logical, semantic)
2. **Preserve original intent** - Maintain the original logic flow and approach
3. **Maintain code style** - Keep the same variable names, function names, and structural patterns
4. **Fix the error** - Apply minimal changes needed to resolve the issue
5. **Verify functionality** - Ensure the fix doesn't break existing functionality

## Types of Errors to Address

### Syntax Errors
- Missing colons, parentheses, brackets
- Incorrect indentation
- Invalid character sequences
- Misplaced keywords

### Runtime Errors
- Division by zero
- Index out of range
- Undefined variables
- Type mismatches
- Attribute errors

### Logical Errors
- Incorrect loop conditions
- Wrong operator precedence
- Off-by-one errors
- Incorrect algorithm implementation

### Semantic Issues
- Unused imports or variables
- Shadowed variables
- Improper exception handling

## Fixing Approach

### Preserve Original Style
- Keep the same variable and function names
- Maintain the original code structure
- Retain the author's coding style and patterns
- Keep comments intact where possible

### Minimal Changes
- Apply the smallest change needed to fix the error
- Avoid refactoring unless absolutely necessary
- Don't improve code beyond fixing the error
- Don't optimize unless the optimization directly fixes the error

### Error-Specific Fixes

#### For Syntax Errors:
- Add missing punctuation
- Fix indentation issues
- Correct keyword spelling
- Match opening and closing brackets/parentheses

#### For Runtime Errors:
- Add bounds checking for arrays/lists
- Handle division by zero
- Initialize undefined variables
- Add proper exception handling

#### For Logical Errors:
- Correct condition expressions
- Fix loop termination conditions
- Adjust indexing if off-by-one
- Verify algorithm implementation

## Examples

### Before and After
```
# Problematic code:
def calculate_average(numbers):
    total = 0
    for num in numbers
        total += num
    return total / len(numbers)  # Potential division by zero

# Fixed code (preserving style):
def calculate_average(numbers):
    if not numbers:  # Added safety check
        return 0
    total = 0
    for num in numbers:  # Added missing colon
        total += num
    return total / len(numbers)  # Now safe from division by zero
```

## Validation

After fixing errors, verify:
1. The code runs without throwing exceptions
2. The original functionality is preserved
3. The code style matches the original
4. The fix addresses the specific error reported