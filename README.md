# ReLive Debugger

Welcome to the **ReLive Debugger** – a powerful tool for running, debugging, and inspecting Python and JavaScript code directly in the browser. This interactive ReLive debugger allows developers to load code, set breakpoints, step through execution, and monitor program flow in real-time with a rich graphical and console interface.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
  - [Step-through Debugging](#step-through-debugging)
  - [Breakpoints](#breakpoints)
  - [Debug Console](#debug-console)
  - [Graphical View](#graphical-view)
  - [Code Editor](#code-editor)
- [Installation](#installation)
- [Usage](#usage)
  - [Starting the Debugger](#starting-the-debugger)
  - [Step Execution](#step-execution)
  - [Continue Execution](#continue-execution)
  - [Quit Debugger](#quit-debugger)
  - [Setting Breakpoints](#setting-breakpoints)
  - [File Upload](#file-upload)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

The **ReLive Debugger** is an interactive tool designed for **Python** and **JavaScript** code, built to run entirely in the browser. It allows users to easily inspect their code, step through it line by line, and check for errors or unexpected behavior in a highly visual and user-friendly interface.

### Key Features:

- **Step-through Debugging**: Go through your code one line at a time, inspecting variables and program flow.
- **Breakpoints**: Pause code execution at specific points to check state.
- **Live Console**: View the output of your code, including errors and print statements.
- **Graphical View**: A simple and intuitive visualization of your code's execution.
- **Code Editor**: View your code directly in the browser with highlighted syntax.

---

## Features

### Step-through Debugging

Step-through debugging lets you execute your code one line at a time, making it easier to understand the flow and catch bugs early. The current line of code will be highlighted, and the program will pause on each step.

For example, consider the following Python code:

```python
def main():
    print("Hello, Debugger!")
    x = 5
    y = 20
    result = x + y
    print(f"Result: {result}")
main()
```

### Breakpoints

Breakpoints are set at specific points in the code where the debugger will pause execution. This allows you to inspect the state of variables and the program's flow at critical points.

To set breakpoints, simply specify the line numbers in the Breakpoints input field:

```
5, 10, 15
```


The program will pause at lines 5, 10, and 15, allowing you to inspect variables or perform any other action needed to diagnose issues.

**Example:**

```python
def test_function():
    a = 10
    b = 20
    breakpoint()  # Execution pauses here
    result = a + b
    print(result)

```
### Debug Console

The debug console is where the output of your code will be displayed. It shows print statements, exceptions, and any other runtime information.

For example, the output in the console might look like this:

```
Hello, Debugger! Result: 25
```


This provides an interactive way to follow the output and inspect the behavior of your program.



### Graphical View
The graphical view is a simple, visual representation of the program's execution. It highlights the currently executing line of code and any breakpoints that have been set.

The graphical view makes it easier to understand the flow of the program, especially when dealing with complex logic.

### Code Editor
The code editor displays your code with syntax highlighting. As you step through the program, the current line is highlighted, and the editor scrolls to ensure the active line is visible.

```ruby
1: def main():
2:     print("Hello, Debugger!")
3:     x = 5
4:     y = 20
5:     result = x + y
6:     print(f"Result: {result}")
7: main()
```

The code editor enables you to interact with your code directly in the browser, allowing you to make edits, view variables, and debug errors.


# Installation
### Prerequisites
• Web Server: A local web server to run the debugger.

• Python: Required for Python code execution (Flask or Django can be used).

• JavaScript Runtime: For executing JavaScript code in the browser.

### Steps:
1. Clone repo:
```ruby
git clone https://github.com/yourusername/web-debugger.git
```
2. Navigate to project directory:
```ruby
cd web-debugger

```
3. Install dependencies:
```ruby
pip install flask
```
4. Start the server
```ruby
python app.py
```

# Usage
### Starting the Debugger
To begin debugging, upload a Python or JavaScript file via the file input. Once the file is uploaded, click the Start Debugger button, and the debugger will initialize.

### Step Execution
To execute the code step by step, click the Step button. The debugger will pause at the current line, allowing you to inspect the program's state and variables.

### Continue Execution
Click Continue to run the code until the next breakpoint or the end of the program.

### Quit Debugger
Click Quit to stop the debugging session and reset the state of the debugger.

### Setting Breakpoints
To set breakpoints, enter the line numbers (comma-separated) into the Breakpoints field, such as:
```
5, 10, 15
```
Click Set Breakpoints, and the debugger will pause execution at those points.

### Debug Console

This shows the output and any other relevant data to be shown in the console of the debugger.

### File Upload
Upload your Python or JavaScript file using the file input field:

```ruby
<input type="file" id="fileInput" accept=".py, .js" />
```
After selecting your file, the debugger will load it and allow you to step through the code.
