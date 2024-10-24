import os
from tkinter import Tk
from interface import USBInterface
import subprocess

# Diese Funktion erstellt das USB-Image
def create_usb_image(usb_drive):
    # Fester Speicherpfad für die Images
    cloned_images_dir = os.path.join(os.getcwd(), 'cloned_images')

    # Erstelle das Verzeichnis, falls es nicht existiert
    if not os.path.exists(cloned_images_dir):
        os.makedirs(cloned_images_dir)

    # Image-Datei Name erstellen (z.B. mit Zeitstempel)
    image_name = "usb_image.img"
    save_path = os.path.join(cloned_images_dir, image_name)

    print(f"Erstelle Image von {usb_drive} und speichere unter {save_path}...")

    # Win32DiskImager Pfad anpassen (Windows)
    win32diskimager_path = r"C:\Program Files (x86)\ImageWriter\Win32DiskImager.exe"

    # Subprocess-Aufruf für Win32DiskImager
    try:
        subprocess.run([win32diskimager_path, '/read', usb_drive, save_path], check=True)
        print(f"Image erfolgreich erstellt und gespeichert unter: {save_path}")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Erstellen des Images: {e}")

# Die Hauptfunktion, die die GUI startet
def main():
    root = Tk()
    
    # Übergibt die Image-Erstellungsfunktion an die GUI
    app = USBInterface(root, create_usb_image)
    
    root.mainloop()

# Startet das Programm
if __name__ == "__main__":
    main()
