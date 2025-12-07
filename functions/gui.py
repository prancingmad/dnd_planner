import tkinter as tk
import config

from config import (
    BUTTON_PACK_OPTIONS,
    REGIONS_BUTTON_LABELS,
    SPECIFIC_REGION_BUTTON_LABELS
)
from functions.general import (
    load_json
)

def clear_widgets(parent):
    for w in parent.winfo_children():
        w.destroy()

def create_scrollable_frame(parent):
    canvas = tk.Canvas(parent)
    scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return scrollable_frame

def initiate_page(root, left_frame, right_frame, header_text, placeholder_text):
    clear_widgets(left_frame)
    clear_widgets(right_frame)

    header_label = tk.Label(left_frame, text=header_text, font=("Arial", 12, "bold"))
    header_label.pack(pady=10)

    placeholder_label = tk.Label(left_frame, text=placeholder_text, anchor="nw", justify="left")
    placeholder_label.pack(fill=tk.BOTH, expand=True)

    scroll_frame = create_scrollable_frame(left_frame)
    return scroll_frame

def initiate_buttons(root, left_frame, right_frame, labels):
    from functions.onclick import on_button_click
    button_frame = tk.Frame(right_frame)
    button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    for label in labels:
        btn = tk.Button(button_frame, text=label,
                        command=lambda l=label: on_button_click(l, root, left_frame, right_frame))
        btn.pack(**BUTTON_PACK_OPTIONS)

def generate_buttons(root, left_frame, right_frame):
    from functions.onclick import on_button_click

    static_container = tk.Frame(right_frame)
    static_container.pack(fill=tk.X, padx=10, pady=10)

    if config.button_flag == "Regions":
        static_labels = REGIONS_BUTTON_LABELS
    else:
        static_labels = SPECIFIC_REGION_BUTTON_LABELS

    for label in static_labels:
        btn = tk.Button(static_container, text=label, command=lambda l=label: on_button_click(l, root, left_frame, right_frame))
        btn.pack(fill=tk.X, padx=5, pady=5)

    back_btn = tk.Button(right_frame, text="Go Back", command=lambda l="Go Back": on_button_click(l, root, left_frame, right_frame))
    back_btn.pack(fill=tk.X, padx=5, pady=5)

    scroll_frame = create_scrollable_frame(right_frame)
    scroll_frame.pack(fill=tk.BOTH, expand=True)

    data = load_json("regions.json")
    items_to_list = []

    if config.regions_flag == "Regions":
        items_to_list = list(data.keys())
    else:
        pass

    for label in items_to_list:
        btn = tk.Button(scroll_frame, text=label,
                        command=lambda l=label: on_button_click(l, root, left_frame, right_frame))
        btn.pack(fill=tk.X, padx=5, pady=5)