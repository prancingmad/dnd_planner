import tkinter as tk

from functions.pages import main_page
from config import WINDOW_SIZE

root = tk.Tk()
root.title("DnD Encounter Generator")
root.geometry(WINDOW_SIZE)
root.resizable(True, True)

container = tk.Frame(root)
container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

left_frame = tk.Frame(container, bg="lightgray")
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

right_frame = tk.Frame(container, width=300, bg="lightgray")
right_frame.pack(side=tk.LEFT, fill=tk.Y)
right_frame.pack_propagate(False)

main_page(root, left_frame, right_frame)

root.mainloop()