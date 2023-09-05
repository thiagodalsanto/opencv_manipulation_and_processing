import tkinter as tk
from tkinter import ttk

class CaptureGUI:
    def __init__(self, main_instance):
        self.main_instance = main_instance

        self.root = tk.Tk()
        self.root.title("Capture")
        self.root.geometry("200x100")

        self.capture_button = ttk.Button(self.root, text="Capture", command=self.capture_image)
        self.capture_button.pack(pady=20)

    def capture_image(self):
        self.main_instance.capture_image()
        self.root.destroy()

    def run(self):
        self.root.mainloop()
