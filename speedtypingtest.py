import time
import tkinter as tk

def calculate_typing_speed(start_time, end_time, text):
    total_time = end_time - start_time
    words = len(text.split())
    speed = words / total_time
    return speed

def start_typing(event):
    global start_time
    start_time = time.time()

def end_typing(event):
    end_time = time.time()
    user_input = text_entry.get("1.0", "end-1c")
    typing_speed = calculate_typing_speed(start_time, end_time, user_input)
    result_label.configure(text="Your typing speed is {:.2f} words per second.".format(typing_speed))

root = tk.Tk()
root.title("Speed Typing Test")

text = "The quick brown fox jumps over the lazy dog."

instruction_label = tk.Label(root, text="Type the following text:")
instruction_label.pack()

text_label = tk.Label(root, text=text)
text_label.pack()

text_entry = tk.Text(root, height=5, width=30)
text_entry.pack()
text_entry.bind("<Return>", start_typing)

result_label = tk.Label(root)
result_label.pack()

submit_button = tk.Button(root, text="Submit")
submit_button.pack()
submit_button.bind("<Button-1>", end_typing)

root.mainloop()
