#!/usr/bin/env python3
"""
Python Error Detector - Analyzes Python code for common errors

This script identifies common Python syntax and structural errors
to help with the python-error-fixer skill.
"""

import ast
import sys
import re
from typing import List, Dict, Tuple


def detect_syntax_errors(code: str) -> List[Dict[str, any]]:
    """
    Detect syntax errors in Python code.

    Args:
        code: The Python code to analyze

    Returns:
        List of detected syntax errors with details
    """
    errors = []

    try:
        # Try to parse the code with AST
        ast.parse(code)
    except SyntaxError as e:
        errors.append({
            'type': 'SyntaxError',
            'line': e.lineno,
            'column': e.offset,
            'message': str(e.msg),
            'text': e.text.strip() if e.text else ""
        })
    except Exception as e:
        errors.append({
            'type': type(e).__name__,
            'line': getattr(e, 'lineno', None),
            'column': getattr(e, 'offset', None),
            'message': str(e),
            'text': ""
        })

    return errors


def detect_common_errors(code: str) -> List[Dict[str, any]]:
    """
    Detect common Python errors beyond syntax issues.

    Args:
        code: The Python code to analyze

    Returns:
        List of detected potential errors with details
    """
    errors = []
    lines = code.split('\n')

    # Check for common indentation issues
    for i, line in enumerate(lines, 1):
        if line.strip().endswith(':') and i < len(lines):
            next_line = lines[i] if i < len(lines) else ""
            if next_line.strip() and not (next_line.startswith('    ') or next_line.startswith('\t')):
                errors.append({
                    'type': 'IndentationError',
                    'line': i + 1,
                    'message': 'Possible indentation issue after colon',
                    'suggestion': 'Check indentation of the line following the colon'
                })

    # Check for undefined variables in simple cases
    # This is a basic check - more complex analysis would require full AST traversal
    for i, line in enumerate(lines, 1):
        # Look for potential undefined variables in assignment patterns
        assign_match = re.search(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*[+\-*/%]=\s*([a-zA-Z_][a-zA-Z0-9_]*)', line)
        if assign_match:
            var1, var2 = assign_match.groups()
            # Simple check: if both sides are the same variable being modified, it might be undefined
            if var1 == var2 and not any(var1 in l for l in lines[:i-1] if '=' in l and var1 in l.split('=')[0]):
                errors.append({
                    'type': 'PotentialNameError',
                    'line': i,
                    'message': f'Variable {var1} might be undefined before use',
                    'suggestion': f'Ensure {var1} is defined before this line'
                })

    # Check for common issues with function definitions
    for i, line in enumerate(lines, 1):
        if 'def ' in line and not line.strip().endswith(':'):
            errors.append({
                'type': 'SyntaxError',
                'line': i,
                'message': 'Function definition missing colon',
                'suggestion': 'Add colon at the end of function definition'
            })

    # Check for print statements in Python 3
    for i, line in enumerate(lines, 1):
        if re.match(r'^\s*print\s+[^\(]', line):
            errors.append({
                'type': 'PotentialSyntaxError',
                'line': i,
                'message': 'Print statement may need parentheses in Python 3',
                'suggestion': 'Use print() with parentheses'
            })

    return errors


def analyze_python_code(code: str) -> Dict[str, any]:
    """
    Comprehensive analysis of Python code for errors.

    Args:
        code: The Python code to analyze

    Returns:
        Dictionary containing all detected errors and analysis
    """
    syntax_errors = detect_syntax_errors(code)
    common_errors = detect_common_errors(code)

    return {
        'syntax_errors': syntax_errors,
        'common_errors': common_errors,
        'total_errors': len(syntax_errors) + len(common_errors)
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python_error_detector.py <file_path>")
        print("Or pipe code to stdin")
        return 1

    if len(sys.argv) == 2:
        # Read from file
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
        except FileNotFoundError:
            print(f"Error: File {file_path} not found")
            return 1
    else:
        # Read from stdin
        code = sys.stdin.read()

    analysis = analyze_python_code(code)

    print("Python Error Analysis Results:")
    print("=" * 40)

    if analysis['syntax_errors']:
        print(f"Syntax Errors Found: {len(analysis['syntax_errors'])}")
        for error in analysis['syntax_errors']:
            print(f"  Line {error.get('line', '?')}: {error['message']}")
            if error.get('text'):
                print(f"    Code: {error['text']}")
    else:
        print("No syntax errors found.")

    if analysis['common_errors']:
        print(f"\nPotential Issues Found: {len(analysis['common_errors'])}")
        for error in analysis['common_errors']:
            print(f"  Line {error.get('line', '?')}: {error['message']}")
            if error.get('suggestion'):
                print(f"    Suggestion: {error['suggestion']}")
    else:
        print("No common issues detected.")

    print(f"\nTotal Issues: {analysis['total_errors']}")

    return 0 if analysis['total_errors'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())