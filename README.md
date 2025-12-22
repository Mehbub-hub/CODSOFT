# 📝 To-Do List Application

**CodSoft Internship - Task 1**

A comprehensive task management application built with Python that helps users efficiently organize and track their daily tasks. Available in both GUI and CLI versions.

---

## 🌟 Features

### Core Functionality
- ✅ **Add Tasks** - Create new tasks with descriptions and priority levels
- ✏️ **Update Tasks** - Modify existing task details
- 🗑️ **Delete Tasks** - Remove completed or unwanted tasks
- ✓ **Mark Complete** - Track task completion status
- 📊 **View Statistics** - Monitor your productivity with detailed stats
- 🔍 **Search Tasks** - Find tasks quickly using keywords
- 🎯 **Priority Levels** - Organize tasks by High, Medium, or Low priority
- 💾 **Persistent Storage** - All tasks saved automatically in JSON format

### User Interface Options
- **GUI Version** - User-friendly graphical interface using Tkinter
- **CLI Version** - Command-line interface for terminal enthusiasts

---

## 📋 Requirements

- Python 3.6 or higher
- tkinter (for GUI version - usually comes pre-installed with Python)
- No external dependencies required!

---

## 🚀 Installation

### Step 1: Clone or Download
Download both Python files to your computer:
- `todo_app_gui.py` (GUI version)
- `todo_app_cli.py` (CLI version)

### Step 2: Verify Python Installation
Open terminal/command prompt and run:
```bash
python --version
```
or
```bash
python3 --version
```

### Step 3: No Additional Installation Required!
The application uses only Python standard libraries.

---

## 💻 How to Run

### GUI Version (Recommended for Beginners)

**Windows:**
```bash
python todo_app_gui.py
```

**Mac/Linux:**
```bash
python3 todo_app_gui.py
```

### CLI Version (For Terminal Users)

**Windows:**
```bash
python todo_app_cli.py
```

**Mac/Linux:**
```bash
python3 todo_app_cli.py
```

---

## 📖 User Guide

### GUI Version

1. **Adding a Task**
   - Type your task in the "Task" field
   - Select priority (High/Medium/Low)
   - Click "➕ Add Task" or press Enter
   
2. **Updating a Task**
   - Double-click on a task OR select it and click in the task field
   - Modify the task text and/or priority
   - Click "✏️ Update Task"

3. **Deleting a Task**
   - Select the task from the list
   - Click "🗑️ Delete Task"
   - Confirm deletion

4. **Marking Complete**
   - Select the task
   - Click "✓ Mark Complete"

5. **View Statistics**
   - Statistics are automatically displayed at the bottom
   - Shows Total, Completed, and Pending tasks

### CLI Version

The CLI presents a menu with numbered options:

```
1. View All Tasks - Display all your tasks in a formatted table
2. Add New Task - Create a new task with priority
3. Update Task - Modify existing task details
4. Delete Task - Remove a task permanently
5. Mark Task as Complete - Update task status
6. View Statistics - See detailed productivity stats
7. Search Tasks - Find tasks by keyword
8. Filter Tasks by Priority - View tasks of specific priority
9. Exit - Close the application
```

Simply enter the number corresponding to your desired action.

---

## 📁 File Structure

```
todo-list-app/
│
├── todo_app_gui.py          # GUI version
├── todo_app_cli.py          # CLI version
├── tasks.json               # Auto-generated data file
└── README.md               # This file
```

---

## 💾 Data Storage

- Tasks are automatically saved in `tasks.json`
- The file is created in the same directory as the script
- Data persists between sessions
- JSON format makes it easy to backup or transfer

### Sample tasks.json structure:
```json
[
    {
        "id": 1,
        "task": "Complete Python project",
        "priority": "High",
        "status": "Pending",
        "created": "2024-12-14 10:30"
    }
]
```

---

## 🎨 GUI Features

### Visual Elements
- **Color-coded priorities:**
  - 🔴 High Priority (Red)
  - 🟡 Medium Priority (Yellow)
  - 🟢 Low Priority (Green)

- **Status indicators:**
  - ✓ Completed tasks
  - ○ Pending tasks

- **Interactive elements:**
  - Double-click tasks to edit
  - Press Enter to quickly add tasks
  - Confirmation dialogs for destructive actions

---

## 🔧 Troubleshooting

### Issue: "python is not recognized"
**Solution:** Make sure Python is installed and added to PATH
- Download Python from [python.org](https://www.python.org/)
- During installation, check "Add Python to PATH"

### Issue: GUI window doesn't appear
**Solution:** Tkinter might not be installed
- On Ubuntu/Debian: `sudo apt-get install python3-tk`
- On Mac: Tkinter comes with Python
- On Windows: Reinstall Python with tkinter enabled

### Issue: Tasks not saving
**Solution:** 
- Check if you have write permissions in the directory
- Make sure the `tasks.json` file isn't open in another program

### Issue: "ModuleNotFoundError"
**Solution:** Make sure you're using Python 3.6 or higher
- All required modules are part of Python's standard library

---

## 📝 Features Explained

### Priority System
Tasks can be assigned three priority levels:
- **High:** Urgent and important tasks
- **Medium:** Regular tasks (default)
- **Low:** Nice-to-have tasks

### Task Status
- **Pending:** Task not yet completed
- **Completed:** Task finished (marked with ✓)

### Statistics Dashboard
Track your productivity with:
- Total number of tasks
- Completed tasks count
- Pending tasks count
- Breakdown by priority level
- Completion rate percentage

---

## 🎯 Use Cases

1. **Daily Task Management**
   - Keep track of daily to-dos
   - Prioritize urgent work

2. **Project Planning**
   - Break down projects into tasks
   - Monitor progress

3. **Study Planning**
   - Organize assignments
   - Track study goals

4. **Personal Goals**
   - Set and achieve personal objectives
   - Build productive habits

---

## 🔄 Future Enhancements (Ideas)

- Add due dates and reminders
- Task categories/tags
- Export tasks to PDF/Excel
- Dark mode theme
- Task notes and descriptions
- Recurring tasks
- Cloud synchronization
- Mobile app version

---

## 👨‍💻 Developer Information

**Project:** To-Do List Application  
**Task:** CodSoft Internship Task 1  
**Language:** Python 3  
**Version:** 1.0.0  
**Date:** December 2024

---

## 📜 License

This project is created as part of the CodSoft internship program and is free to use for educational purposes.

---

## 🤝 Contributing

This is an internship project, but suggestions and improvements are welcome!

---

## 📞 Support

If you encounter any issues or have questions:
1. Check the Troubleshooting section above
2. Review the User Guide
3. Contact your internship coordinator

---

## ⭐ Acknowledgments

- **CodSoft** for providing this internship opportunity
- Python Software Foundation for the excellent standard library
- Tkinter for the GUI framework

---

## 📚 Learning Outcomes

By completing this project, you'll learn:
- File handling in Python (JSON)
- GUI development with Tkinter
- CLI application development
- Data persistence
- User input validation
- Error handling
- Code organization and structure

---

**Happy Task Managing! 🎉**

*Remember: Consistent task management is key to productivity!*