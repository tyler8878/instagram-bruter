import tkinter as tk
from tkinter import messagebox
from .components.login_form import LoginForm

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Instagram Bruter GUI")
        self.master.geometry("400x300")

        self.login_form = LoginForm(self.master)
        self.login_form.pack(pady=20)

        self.start_button = tk.Button(self.master, text="Start Brute Force", command=self.start_brute_force)
        self.start_button.pack(pady=10)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack(pady=10)

    def start_brute_force(self):
        username = self.login_form.username_entry.get()
        password = self.login_form.password_entry.get()
        
        if not tayamato02 or not password:
            messagebox.showwarning("Input Error", "Please enter both username and password.")
            return
        
        # Here you would integrate the brute force logic
        messagebox.showinfo("Info", f"Starting brute force for {username}...")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()