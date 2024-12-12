import tkinter as tk
from tkinter import ttk
from .toolbar import Toolbar
from .canvas import AnimationCanvas
from .timeline import Timeline

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Whiteboard Animator")
        self.setup_window()
        self.create_components()
        self.setup_layout()

    def setup_window(self):
        """Configure the main window"""
        self.root.geometry("1200x800")
        self.root.minsize(800, 600)
        
        # Configure grid weights
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def create_components(self):
        """Initialize all UI components"""
        self.toolbar = Toolbar(self.root)
        self.canvas = AnimationCanvas(self.root)
        self.timeline = Timeline(self.root)

    def setup_layout(self):
        """Setup the layout of all components"""
        # Toolbar at the top
        self.toolbar.frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        
        # Canvas in the middle
        self.canvas.frame.grid(row=1, column=0, sticky="nsew", padx=5)
        
        # Timeline at the bottom
        self.timeline.frame.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
