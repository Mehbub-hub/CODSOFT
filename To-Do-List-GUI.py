import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("600x700")
        self.root.config(bg="#f0f0f0")
        
        # File to store tasks
        self.data_file = "tasks.json"
        self.tasks = self.load_tasks()
        
        # Create UI
        self.create_widgets()
        self.refresh_task_list()
    
    def create_widgets(self):
        # Title
        title_frame = tk.Frame(self.root, bg="#2c3e50", pady=15)
        title_frame.pack(fill="x")
        title_label = tk.Label(title_frame, text="📝 MY TO-DO LIST", 
                              font=("Arial", 24, "bold"), 
                              bg="#2c3e50", fg="white")
        title_label.pack()
        
        # Input Frame
        input_frame = tk.Frame(self.root, bg="#f0f0f0", pady=20)
        input_frame.pack(fill="x", padx=20)
        
        tk.Label(input_frame, text="Task:", font=("Arial", 12), 
                bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
        
        self.task_entry = tk.Entry(input_frame, font=("Arial", 12), width=40)
        self.task_entry.grid(row=0, column=1, padx=10, pady=5)
        self.task_entry.bind('<Return>', lambda e: self.add_task())
        
        tk.Label(input_frame, text="Priority:", font=("Arial", 12), 
                bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
        
        self.priority_var = tk.StringVar(value="Medium")
        priority_combo = ttk.Combobox(input_frame, textvariable=self.priority_var,
                                     values=["High", "Medium", "Low"],
                                     font=("Arial", 10), state="readonly", width=15)
        priority_combo.grid(row=1, column=1, sticky="w", padx=10, pady=5)
        
        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(pady=10)
        
        self.add_btn = tk.Button(btn_frame, text="➕ Add Task", 
                                font=("Arial", 11, "bold"),
                                bg="#27ae60", fg="white", 
                                command=self.add_task,
                                cursor="hand2", padx=15, pady=8)
        self.add_btn.grid(row=0, column=0, padx=5)
        
        self.update_btn = tk.Button(btn_frame, text="✏️ Update Task", 
                                   font=("Arial", 11, "bold"),
                                   bg="#f39c12", fg="white", 
                                   command=self.update_task,
                                   cursor="hand2", padx=15, pady=8)
        self.update_btn.grid(row=0, column=1, padx=5)
        
        self.delete_btn = tk.Button(btn_frame, text="🗑️ Delete Task", 
                                   font=("Arial", 11, "bold"),
                                   bg="#e74c3c", fg="white", 
                                   command=self.delete_task,
                                   cursor="hand2", padx=15, pady=8)
        self.delete_btn.grid(row=0, column=2, padx=5)
        
        self.complete_btn = tk.Button(btn_frame, text="✓ Mark Complete", 
                                     font=("Arial", 11, "bold"),
                                     bg="#3498db", fg="white", 
                                     command=self.mark_complete,
                                     cursor="hand2", padx=15, pady=8)
        self.complete_btn.grid(row=0, column=3, padx=5)
        
        # Task List Frame
        list_frame = tk.Frame(self.root, bg="#f0f0f0")
        list_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        tk.Label(list_frame, text="Your Tasks:", font=("Arial", 14, "bold"), 
                bg="#f0f0f0").pack(anchor="w", pady=5)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")
        
        # Listbox
        self.task_listbox = tk.Listbox(list_frame, font=("Arial", 11),
                                       height=15, 
                                       yscrollcommand=scrollbar.set,
                                       selectmode=tk.SINGLE,
                                       bg="white", 
                                       selectbackground="#3498db")
        self.task_listbox.pack(fill="both", expand=True)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Bind double-click to edit
        self.task_listbox.bind('<Double-Button-1>', lambda e: self.load_task_to_edit())
        
        # Statistics Frame
        stats_frame = tk.Frame(self.root, bg="#ecf0f1", pady=10)
        stats_frame.pack(fill="x", padx=20, pady=10)
        
        self.stats_label = tk.Label(stats_frame, text="", 
                                    font=("Arial", 10),
                                    bg="#ecf0f1")
        self.stats_label.pack()
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.tasks, f, indent=4)
    
    def add_task(self):
        """Add a new task"""
        task_text = self.task_entry.get().strip()
        if not task_text:
            messagebox.showwarning("Warning", "Please enter a task!")
            return
        
        task = {
            "id": len(self.tasks) + 1,
            "task": task_text,
            "priority": self.priority_var.get(),
            "status": "Pending",
            "created": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        self.tasks.append(task)
        self.save_tasks()
        self.refresh_task_list()
        self.task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Task added successfully!")
    
    def update_task(self):
        """Update selected task"""
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task to update!")
            return
        
        task_text = self.task_entry.get().strip()
        if not task_text:
            messagebox.showwarning("Warning", "Please enter new task text!")
            return
        
        index = selected[0]
        self.tasks[index]["task"] = task_text
        self.tasks[index]["priority"] = self.priority_var.get()
        
        self.save_tasks()
        self.refresh_task_list()
        self.task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Task updated successfully!")
    
    def delete_task(self):
        """Delete selected task"""
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task to delete!")
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this task?"):
            index = selected[0]
            del self.tasks[index]
            
            # Reassign IDs
            for i, task in enumerate(self.tasks):
                task["id"] = i + 1
            
            self.save_tasks()
            self.refresh_task_list()
            self.task_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Task deleted successfully!")
    
    def mark_complete(self):
        """Mark selected task as complete"""
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task to mark as complete!")
            return
        
        index = selected[0]
        if self.tasks[index]["status"] == "Completed":
            messagebox.showinfo("Info", "Task is already completed!")
            return
        
        self.tasks[index]["status"] = "Completed"
        self.save_tasks()
        self.refresh_task_list()
        messagebox.showinfo("Success", "Task marked as complete!")
    
    def load_task_to_edit(self):
        """Load selected task into entry field for editing"""
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, self.tasks[index]["task"])
            self.priority_var.set(self.tasks[index]["priority"])
    
    def refresh_task_list(self):
        """Refresh the task listbox"""
        self.task_listbox.delete(0, tk.END)
        
        for task in self.tasks:
            status_icon = "✓" if task["status"] == "Completed" else "○"
            priority_icon = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}[task["priority"]]
            display_text = f"{status_icon} {priority_icon} {task['task']} [{task['priority']}]"
            
            self.task_listbox.insert(tk.END, display_text)
            
            # Color completed tasks differently
            if task["status"] == "Completed":
                self.task_listbox.itemconfig(tk.END, fg="gray")
        
        # Update statistics
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["status"] == "Completed")
        pending = total - completed
        self.stats_label.config(text=f"Total: {total} | Completed: {completed} | Pending: {pending}")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
