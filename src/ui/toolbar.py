import tkinter as tk
from tkinter import ttk

class Toolbar:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.create_widgets()

    def create_widgets(self):
        """Create toolbar buttons and controls"""
        # File operations
        self.btn_new = ttk.Button(self.frame, text="New Project")
        self.btn_open = ttk.Button(self.frame, text="Open")
        self.btn_save = ttk.Button(self.frame, text="Save")
        
        # Tools
        self.btn_import = ttk.Button(self.frame, text="Import Image")
        self.btn_text = ttk.Button(self.frame, text="Add Text")
        self.btn_draw = ttk.Button(self.frame, text="Draw")
        
        # Export
        self.btn_export = ttk.Button(self.frame, text="Export Video")
        
        # Layout
        buttons = [self.btn_new, self.btn_open, self.btn_save, 
                  ttk.Separator(self.frame, orient='vertical'),
                  self.btn_import, self.btn_text, self.btn_draw,
                  ttk.Separator(self.frame, orient='vertical'),
                  self.btn_export]
        
        for i, button in enumerate(buttons):
            button.pack(side=tk.LEFT, padx=2, pady=2)