#Python Utility Suite 🚀

A collection of three distinct Python implementations demonstrating functional programming, interactive CLI tools, and command-line argument handling.
1. Recursive Number Guessing Game 🎮
A smart, level-based guessing game built with modern Python syntax.
Key Features:
Recursion & Functional Logic: Uses recursive function calls instead of traditional loops.
Walrus Operator (:=): Implements assignment expressions for cleaner input handling.
Level Management: Uses Python Dictionaries to map difficulty levels (Easy, Medium, Hard) to attempt limits.
Smart Error Recovery: Invalid inputs (non-integers) are caught via Exception Handling, allowing the user to retry without losing an attempt.
2. Interactive Menu-Driven Calculator 🧮
A robust, loop-based calculator designed for continuous user interaction.
Key Features:
Modular Design: Separate functions for add, subtract, multiply, and divide.
Input Validation: Uses try-except blocks to prevent crashes from invalid float conversions.
Zero-Division Safety: Includes a logical check to handle denominators of zero gracefully.
Persistent Interface: A while True loop ensures the tool stays active until the user explicitly exits.
3. Command Line Interface (CLI) Calculator 🖥️
A developer-focused tool that executes calculations directly via terminal arguments.
Usage:
python main.py <operation> <num1> <num2>
(e.g., python main.py add 10 5)
Key Features:
System Integration: Utilizes the sys.argv module to process external arguments.
Scripting Ready: Perfect for being called from other shell scripts or automation workflows.
Usage Guidance: Automatically displays a help message if the incorrect number of arguments is provided.
