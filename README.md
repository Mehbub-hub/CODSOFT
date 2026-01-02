# CodSoft Python Programming Internship Projects

**Intern Name:** Mehbub Razza  
**Internship:** Python Programming at CodSoft  
**Repository:** Python Internship Projects Collection

---

## 📋 Table of Contents
- [Overview](#overview)
- [Projects](#projects)
  - [1. To-Do List Manager](#1-to-do-list-manager)
  - [2. Simple Calculator](#2-simple-calculator)
  - [3. Password Generator](#3-password-generator)
- [Technologies Used](#technologies-used)
- [Installation & Setup](#installation--setup)
- [How to Run](#how-to-run)
- [Screenshots & Features](#screenshots--features)
- [Learning Outcomes](#learning-outcomes)
- [Contact](#contact)

---

## 🎯 Overview

This repository contains three Python projects completed during my internship at CodSoft. Each project demonstrates different aspects of Python programming, from GUI development to security implementations and user interaction design.

---

## 📂 Projects

### 1. To-Do List Manager

A comprehensive task management application with a graphical user interface built using Tkinter.

#### Features:
- ✅ **Add Tasks** - Create new tasks with custom priorities
- ✏️ **Update Tasks** - Modify existing tasks and their priorities
- 🗑️ **Delete Tasks** - Remove completed or unwanted tasks
- ✓ **Mark Complete** - Track task completion status
- 🎨 **Priority Levels** - Categorize tasks as High, Medium, or Low
- 💾 **Persistent Storage** - Tasks saved to JSON file (`tasks.json`)
- 📊 **Statistics Dashboard** - View total, completed, and pending tasks
- 🎯 **Visual Indicators** - Color-coded priorities and completion status
- ⌨️ **Keyboard Shortcuts** - Press Enter to add tasks quickly
- 🖱️ **Double-Click Edit** - Double-click any task to edit it

#### Technical Highlights:
- JSON-based data persistence
- Object-oriented programming structure
- Event-driven GUI with Tkinter
- Real-time statistics tracking
- Input validation and error handling

#### File Structure:
```
📁 To-Do List Manager/
├── todo_app.py          # Main application code
└── tasks.json           # Auto-generated data file
```

---

### 2. Simple Calculator

An intuitive calculator application with a clean, user-friendly interface for basic arithmetic operations.

#### Features:
- ➕ **Addition** - Add two numbers
- ➖ **Subtraction** - Subtract second number from first
- ✖️ **Multiplication** - Multiply two numbers
- ➗ **Division** - Divide with zero-division error handling
- 🎨 **Modern UI** - Clean, professional interface design
- 🔄 **Clear Function** - Reset all inputs with one click
- ⚠️ **Error Handling** - Validates inputs and handles exceptions
- 📱 **Fixed Layout** - Consistent 400x550 window size

#### Technical Highlights:
- Radio button selection for operations
- Input validation for numeric values
- Exception handling for edge cases
- Responsive button interactions
- Color-coded result display

#### File Structure:
```
📁 Simple Calculator/
└── calculator.py        # Main application code
```

---

### 3. Password Generator

A cryptographically secure password generator with customizable complexity options and strength analysis.

#### Features:
- 🔐 **Cryptographically Secure** - Uses `secrets` module for true randomness
- ⚙️ **Customizable Options:**
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Special symbols (!@#$%^&*...)
- 📏 **Flexible Length** - Generate passwords from 4 to 128+ characters
- 💪 **Strength Analysis** - Real-time password strength assessment
- 🔢 **Entropy Calculation** - Displays cryptographic entropy in bits
- ✅ **Character Guarantee** - Ensures at least one character from each selected type
- 📊 **Strength Ratings:**
  - ⚠️ WEAK (< 28 bits)
  - ⚡ FAIR (28-35 bits)
  - ✓ GOOD (36-59 bits)
  - ✓✓ STRONG (60-127 bits)
  - ✓✓✓ VERY STRONG (128+ bits)
- 💡 **Security Tips** - Built-in best practices guide

#### Technical Highlights:
- Uses `secrets` module for cryptographic randomness
- Mathematical entropy calculation
- Character pool composition analysis
- Input validation and error handling
- Interactive command-line interface
- Continuous generation mode

#### File Structure:
```
📁 Password Generator/
└── password_generator.py  # Main application code
```

---

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **Tkinter** - GUI framework for desktop applications
- **JSON** - Data storage and persistence
- **secrets** - Cryptographically secure random generation
- **string** - Character set definitions
- **datetime** - Timestamp functionality

---

## 💻 Installation & Setup

### Prerequisites:
- Python 3.6 or higher installed on your system
- Tkinter (usually comes pre-installed with Python)

### Steps:

1. **Clone the repository:**
```bash
git clone https://github.com/Mehbub-hub/codsoft-python-internship.git
cd codsoft-python-internship
```

2. **Verify Python installation:**
```bash
python --version
```

3. **No additional dependencies required!** All projects use Python standard library modules.

---

## 🚀 How to Run

### To-Do List Manager:
```bash
python todo_app.py
```

### Simple Calculator:
```bash
python calculator.py
```

### Password Generator:
```bash
python password_generator.py
```

---

## 📸 Screenshots & Features

### To-Do List Manager
- Modern dark-themed header
- Priority-based color coding (🔴 High, 🟡 Medium, 🟢 Low)
- Real-time task statistics
- Intuitive button layout

### Simple Calculator
- Clean green-themed interface
- Large, readable input fields
- Clear result display panel
- Radio button operation selection

### Password Generator
- Command-line interface with formatted output
- Detailed password analysis
- Security tips and recommendations
- Batch generation capability

---

## 📚 Learning Outcomes

Through these projects, I gained practical experience in:

1. **GUI Development**
   - Tkinter widget management
   - Event handling and user interactions
   - Layout design and styling

2. **Data Management**
   - JSON file operations
   - Data persistence techniques
   - CRUD operations implementation

3. **Security Practices**
   - Cryptographic random generation
   - Password strength analysis
   - Security best practices

4. **Software Design**
   - Object-oriented programming
   - Error handling and validation
   - User experience considerations

5. **Problem Solving**
   - Algorithm implementation
   - Edge case handling
   - Code optimization

---

## 📞 Contact

**Mehbub Razza**

- 📧 Email: [mehbubraza69@gmail.com]
- 💼 LinkedIn: [www.linkedin.com/in/mehbub-razza-8b2a23399]
- 🐙 GitHub: [@myusername](https://github.com/Mehbub-hub)

---

## 📝 License

This project is part of my internship at CodSoft and is available for educational purposes.

---

## 🙏 Acknowledgments

Special thanks to **CodSoft** for providing this internship opportunity and guidance throughout the development of these projects.

---

### ⭐ If you find these projects helpful, please consider giving this repository a star!

---

*Last Updated: January 2026*
