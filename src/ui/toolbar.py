import tkinter as tk
from tkinter import ttk, messagebox
from ..utils.file_handlers import ProjectFileHandler, ImageHandler

class Toolbar:
    def __init__(self, parent, canvas_ref):
        self.frame = ttk.Frame(parent)
        self.canvas_ref = canvas_ref
        self.project_handler = ProjectFileHandler()
        self.image_handler = ImageHandler()
        self.create_widgets()
        self.current_project = None

    def create_widgets(self):
        """Create toolbar buttons and controls"""
        # File operations
        file_frame = ttk.LabelFrame(self.frame, text="File")
        file_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.Y)

        self.btn_new = ttk.Button(file_frame, text="New Project", command=self.new_project)
        self.btn_open = ttk.Button(file_frame, text="Open Project", command=self.open_project)
        self.btn_save = ttk.Button(file_frame, text="Save Project", command=self.save_project)
        
        # Tools
        tools_frame = ttk.LabelFrame(self.frame, text="Tools")
        tools_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.Y)

        self.btn_import = ttk.Button(tools_frame, text="Import Image", command=self.import_image)
        self.btn_text = ttk.Button(tools_frame, text="Add Text", command=self.add_text)
        self.btn_draw = ttk.Button(tools_frame, text="Draw", command=self.toggle_draw_mode)
        
        # Pack buttons
        for btn in [self.btn_new, self.btn_open, self.btn_save]:
            btn.pack(side=tk.TOP, padx=2, pady=2)
            
        for btn in [self.btn_import, self.btn_text, self.btn_draw]:
            btn.pack(side=tk.TOP, padx=2, pady=2)

        # Drawing tools (initially hidden)
        self.drawing_tools_frame = ttk.LabelFrame(self.frame, text="Drawing Tools")
        
        self.color_btn = ttk.Button(self.drawing_tools_frame, text="Color")
        self.size_scale = ttk.Scale(self.drawing_tools_frame, from_=1, to=10, orient=tk.HORIZONTAL)
        
        # Tool state
        self.draw_mode = False

    def new_project(self):
        """Create a new project"""
        if messagebox.askyesno("New Project", "Create new project? Unsaved changes will be lost."):
            self.current_project = self.project_handler.new_project()
            self.canvas_ref.clear_canvas()
            messagebox.showinfo("Success", "New project created!")

    def open_project(self):
        """Open an existing project"""
        project_data = self.project_handler.load_project()
        if project_data:
            self.current_project = project_data
            self.canvas_ref.load_project(project_data)
            messagebox.showinfo("Success", "Project loaded successfully!")

    def save_project(self):
        """Save current project"""
        if self.current_project:
            self.project_handler.save_project(self.current_project)
            messagebox.showinfo("Success", "Project saved successfully!")
        else:
            messagebox.showwarning("Warning", "No active project to save!")

    def import_image(self):
        """Import an image to the canvas"""
        photo_image, pil_image = self.image_handler.import_image()
        if photo_image:
            self.canvas_ref.add_image(photo_image, pil_image)

    def add_text(self):
        """Open text input dialog"""
        text_dialog = TextInputDialog(self.frame)
        if text_dialog.result:
            self.canvas_ref.add_text(text_dialog.result)

    def toggle_draw_mode(self):
        """Toggle drawing mode"""
        self.draw_mode = not self.draw_mode
        if self.draw_mode:
            self.drawing_tools_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.Y)
            self.color_btn.pack(padx=2, pady=2)
            self.size_scale.pack(padx=2, pady=2)
            self.btn_draw.configure(style='Toggled.TButton')
        else:
            self.drawing_tools_frame.pack_forget()
            self.btn_draw.configure(style='TButton')

class TextInputDialog:
    def __init__(self, parent):
        self.result = None
        
        # Create dialog window
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Add Text")
        self.dialog.geometry("300x150")
        
        # Text entry
        self.text_entry = ttk.Entry(self.dialog)
        self.text_entry.pack(padx=20, pady=20)
        
        # Font size
        size_frame = ttk.Frame(self.dialog)
        size_frame.pack(fill=tk.X, padx=20)
        
        ttk.Label(size_frame, text="Size:").pack(side=tk.LEFT)
        self.size_var = tk.StringVar(value="12")
        self.size_entry = ttk.Spinbox(size_frame, from_=8, to=72, textvariable=self.size_var)
        self.size_entry.pack(side=tk.LEFT, padx=5)
        
        # Buttons
        btn_frame = ttk.Frame(self.dialog)
        btn_frame.pack(fill=tk.X, padx=20, pady=20)
        
        ttk.Button(btn_frame, text="OK", command=self.ok_clicked).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Cancel", command=self.cancel_clicked).pack(side=tk.LEFT)
        
        # Make dialog modal
        self.dialog.transient(parent)
        self.dialog.grab_set()
        parent.wait_window(self.dialog)

    def ok_clicked(self):
        """Handle OK button click"""
        text = self.text_entry.get()
        size = int(self.size_var.get())
        if text:
            self.result = (text, size)
            self.dialog.destroy()

    def cancel_clicked(self):
        """Handle Cancel button click"""
        self.dialog.destroy()