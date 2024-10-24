import tkinter as tk
from tkinter import filedialog

class USBInterface:
    def __init__(self, root, main_callback):  # Jetzt nimmt es das main_callback-Argument entgegen
        self.root = root
        self.main_callback = main_callback  # Callback zur Übergabe an main.py
        self.root.title("USB Image Creator")

        # Button to select the USB drive
        self.usb_button = tk.Button(root, text="USB-Laufwerk auswählen", command=self.select_usb_drive)
        self.usb_button.pack(pady=10)

        # Label to show the selected USB drive
        self.usb_label = tk.Label(root, text="Kein USB-Laufwerk ausgewählt")
        self.usb_label.pack()

        # Button to start the cloning process
        self.clone_button = tk.Button(root, text="Image erstellen", command=self.create_image)
        self.clone_button.pack(pady=20)

        self.usb_drive = None

    def select_usb_drive(self):
        self.usb_drive = filedialog.askdirectory(title="USB-Laufwerk auswählen")
        if self.usb_drive:
            self.usb_label.config(text=f"Ausgewähltes USB-Laufwerk: {self.usb_drive}")

    def create_image(self):
        if not self.usb_drive:
            print("Kein USB-Laufwerk ausgewählt!")
            return

        # Übergibt das ausgewählte USB-Laufwerk an die Hauptlogik (main.py)
        self.main_callback(self.usb_drive)
