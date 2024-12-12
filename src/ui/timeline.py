import tkinter as tk
from tkinter import ttk

class Timeline:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.create_widgets()

    def create_widgets(self):
        """Create timeline widgets"""
        # Timeline controls
        self.controls_frame = ttk.Frame(self.frame)
        self.controls_frame.pack(fill=tk.X, pady=2)
        
        self.btn_play = ttk.Button(self.controls_frame, text="▶")
        self.btn_pause = ttk.Button(self.controls_frame, text="⏸")
        self.btn_stop = ttk.Button(self.controls_frame, text="⏹")
        
        self.btn_play.pack(side=tk.LEFT, padx=2)
        self.btn_pause.pack(side=tk.LEFT, padx=2)
        self.btn_stop.pack(side=tk.LEFT, padx=2)
        
        # Timeline canvas
        self.canvas = tk.Canvas(
            self.frame,
            height=100,
            bg='lightgray'
        )
        self.canvas.pack(fill=tk.X, expand=True)