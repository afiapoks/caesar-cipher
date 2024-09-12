import tkinter as tk

def on_closing():
    print("Window closed")
    root.destroy()

root = tk.Tk()
root.title("Basic Tkinter Test")
tk.Label(root, text="Hello, Tkinter!").pack()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()




 