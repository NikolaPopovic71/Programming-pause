import time
from tkinter import Tk, Label, Entry, Button, StringVar, Toplevel
from tkinter import ttk
import threading

def apply_theme(theme):
    if theme == "dark":
        root.configure(bg='#2e2e2e')
        style.configure("TLabel", background='#2e2e2e', foreground='#ffffff')
        style.configure("TEntry", fieldbackground='#4d4d4d', foreground='#2e2e2e')
        style.configure("TButton", background='#4d4d4d', foreground='#2e2e2e')
        style.map("TButton", background=[('active', '#3e3e3e')], foreground=[('active', '#2e2e2e')])
    else:
        root.configure(bg='#f0f0f0')
        style.configure("TLabel", background='#f0f0f0', foreground='#000000')
        style.configure("TEntry", fieldbackground='#ffffff', foreground='#000000')
        style.configure("TButton", background='#ffffff', foreground='#000000')
        style.map("TButton", background=[('active', '#e0e0e0')], foreground=[('active', '#000000')])

def start_timer():
    try:
        minutes = int(time_input.get())
        seconds = minutes * 60
        threading.Thread(target=timer_thread, args=(seconds,)).start()
    except ValueError:
        custom_messagebox("Error", "Invalid Input\nPlease enter a valid number")

def timer_thread(seconds):
    root.withdraw()
    time.sleep(seconds)
    root.deiconify()
    show_break_message()

def show_break_message():
    instructions = (
        "Time to take a break!\n\nHere are some exercises:\n\n"
        "1. Stand up and stretch your body.\n\n"
        "2. Look away from the screen for 20 seconds.\n\n"
        "3. Roll your shoulders back and forth.\n\n"
        "4. Blink your eyes slowly 10 times.\n\n"
        "5. Rotate your neck gently from side to side.\n\n"
        "6. Take a short walk around the room."
    )
    custom_messagebox("Break Time!", instructions)
    time_input.set("")  # Clear the entry field

def change_theme():
    global current_theme
    if current_theme == "dark":
        current_theme = "light"
        apply_theme("light")
    else:
        current_theme = "dark"
        apply_theme("dark")

def custom_messagebox(title, message):
    msg_box = Toplevel(root)
    msg_box.title(title)
    msg_box.attributes('-fullscreen', True)  # Make the message box fullscreen

    if current_theme == "dark":
        msg_box.configure(bg='#2e2e2e')
        bg_color = '#2e2e2e'
        fg_color = '#ffffff'
    else:
        msg_box.configure(bg='#f0f0f0')
        bg_color = '#f0f0f0'
        fg_color = '#000000'

    font_style = ("Helvetica", 24)  # Example font size, you can adjust as needed

    msg_label = Label(msg_box, text=message, wraplength=800, justify='left', font=font_style, bg=bg_color, fg=fg_color)
    msg_label.pack(pady=20)

    ok_button = Button(msg_box, text="OK", command=msg_box.destroy, font=font_style, bg=bg_color, fg=fg_color)
    ok_button.pack(pady=30)

# Set up the GUI
root = Tk()
root.title("Break Reminder")
root.geometry("500x400")

style = ttk.Style()
current_theme = "light"
apply_theme(current_theme)

change_theme_button = ttk.Button(root, text="Change theme!", command=change_theme, style="TButton")
change_theme_button.pack(pady=50)

entry_label = ttk.Label(root, text="Enter time in minutes:", style="TLabel")
entry_label.pack(pady=10)

time_input = StringVar()
time_entry = ttk.Entry(root, textvariable=time_input, style="TEntry")
time_entry.pack(pady=20)

start_time_button = ttk.Button(root, text="Start Timer", command=start_timer, style="TButton")
start_time_button.pack(pady=40)

root.mainloop()
