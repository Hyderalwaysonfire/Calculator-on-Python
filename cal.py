import customtkinter as ctk
from tkinter import messagebox
import math

# Functionality for calculator
def on_click(key):
    if key == "=":
        try:
            result = eval(display.get())
            display.delete(0, ctk.END)
            display.insert(ctk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
    elif key == "C":
        display.delete(0, ctk.END)
    elif key == "√":
        try:
            result = math.sqrt(float(display.get()))
            display.delete(0, ctk.END)
            display.insert(ctk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
    elif key == "^":
        display.insert(ctk.END, "**")
    else:
        display.insert(ctk.END, key)

# Configure customtkinter appearance
ctk.set_appearance_mode("Dark")  # Modes: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

# Main window
root = ctk.CTk()
root.title("Responsive 3D Calculator")
root.geometry("400x600")
root.minsize(400, 600)

# Responsive grid configuration for the root window
root.grid_rowconfigure(0, weight=1)  # For display
root.grid_rowconfigure(1, weight=3)  # For buttons
root.grid_columnconfigure(0, weight=1)

# Display entry
display = ctk.CTkEntry(root, font=("Arial", 24), justify="right", height=50)
display.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Button configuration
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/",
    "√", "^"
]

# Button colors for specific operations
operation_colors = {
    "+": "#ffa07a",  # Light Salmon for Addition
    "-": "#98fb98",  # Pale Green for Subtraction
    "*": "#ffd700",  # Gold for Multiplication
    "/": "#87ceeb",  # Sky Blue for Division
    "√": "#da70d6",  # Orchid for Root
    "^": "#ff69b4"   # Hot Pink for Power
}

# Button frame
button_frame = ctk.CTkFrame(root)
button_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

# Responsive grid configuration for the button frame
for i in range(5):  # 5 rows
    button_frame.grid_rowconfigure(i, weight=1)
for j in range(4):  # 4 columns
    button_frame.grid_columnconfigure(j, weight=1)

# Create buttons dynamically
for i, btn in enumerate(buttons):
    # Use default button color unless it's an operation
    color = operation_colors.get(btn, "#1f6aa5")  # Default for others
    hover_color = "#4a90e2" if btn not in operation_colors else "#d3d3d3"  # Hover effect

    button = ctk.CTkButton(
        button_frame, text=btn, font=("Arial", 20),
        corner_radius=10, fg_color=color, hover_color=hover_color,
        command=lambda b=btn: on_click(b)
    )
    button.grid(row=i // 4, column=i % 4, padx=5, pady=5, sticky="nsew")

# Run the application
root.mainloop()
