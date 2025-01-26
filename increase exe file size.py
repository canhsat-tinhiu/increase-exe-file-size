import os
import tkinter as tk
from tkinter import filedialog
def increase_file_size(file_path, target_size_mb=670):

# def increase_file_size(file_path, target_size_mb=670):
    target_size = target_size_mb * 1024 * 1024
    current_size = os.path.getsize(file_path)
    bytes_to_add = target_size - current_size
    
    if bytes_to_add > 0:
        with open(file_path, 'ab') as f:
            f.write(b'\0' * bytes_to_add)

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Chọn file .exe", filetypes=[("Executable files", "*.exe")])
    if file_path:
        increase_file_size(file_path)

select_file()
