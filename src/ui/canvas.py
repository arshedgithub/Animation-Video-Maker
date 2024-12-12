import tkinter as tk
from tkinter import ttk

class AnimationCanvas:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.create_canvas()

    def create_canvas(self):
        """Create the main drawing canvas"""
        self.canvas = tk.Canvas(
            self.frame,
            bg='white',
            width=800,
            height=600
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Add scrollbars
        self.h_scrollbar = ttk.Scrollbar(
            self.frame,
            orient=tk.HORIZONTAL,
            command=self.canvas.xview
        )
        self.v_scrollbar = ttk.Scrollbar(
            self.frame,
            orient=tk.VERTICAL,
            command=self.canvas.yview
        )
        
        self.canvas.configure(
            xscrollcommand=self.h_scrollbar.set,
            yscrollcommand=self.v_scrollbar.set
        )
        
        # Layout scrollbars
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
