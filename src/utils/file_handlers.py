import json
import os
from PIL import Image, ImageTk
from tkinter import filedialog

class ProjectFileHandler:
    @staticmethod
    def new_project():
        return {
            'name': 'Untitled Project',
            'canvas_size': (800, 600),
            'elements': [],
            'timeline': []
        }

    @staticmethod
    def save_project(project_data, file_path=None):
        if not file_path:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".wbp",
                filetypes=[("Whiteboard Project", "*.wbp")]
            )
        
        if file_path:
            with open(file_path, 'w') as f:
                json.dump(project_data, f)
            return file_path
        return None

    @staticmethod
    def load_project():
        file_path = filedialog.askopenfilename(
            filetypes=[("Whiteboard Project", "*.wbp")]
        )
        if file_path:
            with open(file_path, 'r') as f:
                return json.load(f)
        return None

class ImageHandler:
    SUPPORTED_FORMATS = [
        ("PNG files", "*.png"),
        ("JPEG files", "*.jpg *.jpeg"),
        ("All files", "*.*")
    ]

    @staticmethod
    def import_image():
        file_path = filedialog.askopenfilename(filetypes=ImageHandler.SUPPORTED_FORMATS)
        if file_path:
            image = Image.open(file_path)
            # Resize if image is too large while maintaining aspect ratio
            max_size = (800, 600)
            image.thumbnail(max_size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(image), image
        return None, None

    @staticmethod
    def save_image(image, file_path=None):
        if not file_path:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=ImageHandler.SUPPORTED_FORMATS
            )
        if file_path:
            image.save(file_path)
            return file_path
        return None