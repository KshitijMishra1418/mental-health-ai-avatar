import tkinter as tk
from tkinter import messagebox

class GreetingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Greeting App")
        self.root.geometry("300x150")

        self.label = tk.Label(root, text="Enter your name:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Greet", command=self.greet_user)
        self.button.pack(pady=10)

    def greet_user(self):
        name = self.entry.get()
        if name.strip():
            messagebox.showinfo("Greeting", f"Hello, {name}!")
        else:
            messagebox.showwarning("Input Error", "Please enter your name.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GreetingApp(root)
    root.mainloop()
