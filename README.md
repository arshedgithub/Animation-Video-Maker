CODE STRUCTURE
==============

animator_video_maker/
│
├── requirements.txt          # Project dependencies
├── main.py                  # Application entry point
├── README.md                # Project documentation
│
├── src/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py      # Application settings and constants
│   │   └── paths.py         # Path configurations
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── animator.py      # Core animation logic
│   │   ├── drawer.py        # Drawing and sketching logic
│   │   └── exporter.py      # Video export functionality
│   │
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── main_window.py   # Main application window
│   │   ├── timeline.py      # Timeline component
│   │   ├── toolbar.py       # Toolbar component
│   │   └── canvas.py        # Drawing canvas component
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── image_processing.py  # Image manipulation utilities
│   │   ├── file_handlers.py     # File operations
│   │   └── validators.py        # Input validation
│   │
│   └── models/
│       ├── __init__.py
│       ├── frame.py         # Frame data structure
│       ├── animation.py     # Animation data structure
│       └── project.py       # Project data structure
│
├── assets/                  # Static assets
│   ├── cursors/            # Custom cursor images
│   ├── icons/              # UI icons
│   └── templates/          # Animation templates
│
├── tests/                  # Unit tests
│   ├── __init__.py
│   ├── test_animator.py
│   ├── test_drawer.py
│   └── test_exporter.py
│
└── docs/                   # Documentation
    ├── setup.md
    ├── usage.md
    └── api.md