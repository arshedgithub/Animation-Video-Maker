import tkinter as tk
from tkinter import ttk

class AnimationCanvas:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.create_canvas()
        self.elements = []
        self.drawing = False
        self.last_x = None
        self.last_y = None

    def create_canvas(self):
        """Create the main drawing canvas"""
        self.canvas = tk.Canvas(
            self.frame,
            bg='white',
            width=800,
            height=600
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Bind mouse events for drawing
        self.canvas.bind('<Button-1>', self.start_drawing)
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.bind('<ButtonRelease-1>', self.stop_drawing)

    def clear_canvas(self):
        """Clear all elements from canvas"""
        self.canvas.delete("all")
        self.elements = []

    def load_project(self, project_data):
        """Load project data onto canvas"""
        self.clear_canvas()
        if 'elements' in project_data:
            for element in project_data['elements']:
                if element['type'] == 'image':
                    # Handle image loading
                    pass
                elif element['type'] == 'text':
                    self.add_text(element['content'])
                elif element['type'] == 'drawing':
                    # Handle drawing loading
                    pass

    def add_image(self, photo_image, pil_image):
        """Add an image to the canvas"""
        image_item = self.canvas.create_image(
            400, 300,  # Center of canvas
            image=photo_image,
            anchor=tk.CENTER
        )
        # Keep reference to prevent garbage collection
        self.canvas.photo = photo_image
        self.elements.append({
            'type': 'image',
            'item': image_item,
            'image': photo_image
        })

    def add_text(self, text_data):
        """Add text to the canvas"""
        text, size = text_data
        text_item = self.canvas.create_text(
            400, 300,  # Center of canvas
            text=text,
            font=('Arial', size),
            fill='black'
        )
        self.elements.append({
            'type': 'text',
            'item': text_item,
            'content': text
        })
        self._make_draggable(text_item)

    def start_drawing(self, event):
        """Start drawing on canvas"""
        if hasattr(self, 'draw_mode') and self.draw_mode:
            self.drawing = True
            self.last_x = event.x
            self.last_y = event.y

    def draw(self, event):
        """Draw on canvas"""
        if self.drawing and self.last_x and self.last_y:
            line = self.canvas.create_line(
                self.last_x, self.last_y,
                event.x, event.y,
                width=2,
                fill='black',
                capstyle=tk.ROUND,
                smooth=True
            )
            self.elements.append({
                'type': 'drawing',
                'item': line
            })
            self.last_x = event.x
            self.last_y = event.y

    def stop_drawing(self, event):
        """Stop drawing on canvas"""
        self.drawing = False
        self.last_x = None
        self.last_y = None

    def _make_draggable(self, item):
        """Make an item draggable on the canvas"""
        self.canvas.tag_bind(item, '<Button-1>', lambda e: self._drag_start(e, item))
        self.canvas.tag_bind(item, '<B1-Motion>', lambda e: self._drag_motion(e, item))

    def _drag_start(self, event, item):
        """Start dragging an item"""
        self._drag_data = {'item': item, 'x': event.x, 'y': event.y}

    def _drag_motion(self, event, item):
        """Handle item dragging"""
        if self._drag_data:
            dx = event.x - self._drag_data['x']
            dy = event.y - self._drag_data['y']
            self.canvas.move(self._drag_data['item'], dx, dy)
            self._drag_data['x'] = event.x
            self._drag_data['y'] = event.y