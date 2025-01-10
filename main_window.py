import ttkbootstrap as ttk
from tkinter import *

class MainWindow:
    def __init__(self, root):
        self.root = root
        
        # Configure main grid
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        
        # Create navigation frame
        self.nav_frame = ttk.Frame(root, style='primary.TFrame')
        self.nav_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        
        # Navigation buttons
        self.jobs_btn = ttk.Button(
            self.nav_frame, 
            text="Jobs", 
            command=self.show_jobs_screen,
            style='primary.TButton'
        )
        self.jobs_btn.pack(side=LEFT, padx=5)
        
        self.search_btn = ttk.Button(
            self.nav_frame, 
            text="Search Files", 
            command=self.show_search_screen,
            style='primary.TButton'
        )
        self.search_btn.pack(side=LEFT, padx=5)
        
        self.metadata_btn = ttk.Button(
            self.nav_frame, 
            text="File Metadata", 
            command=self.show_metadata_screen,
            style='primary.TButton'
        )
        self.metadata_btn.pack(side=LEFT, padx=5)
        
        # Main content frame
        self.content_frame = ttk.Frame(root)
        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        
        # Start with jobs screen
        self.current_screen = None  
        self.show_jobs_screen()
    
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_jobs_screen(self):
        self.clear_content()
        from jobs_screen import JobsScreen
        self.current_screen = JobsScreen(self.content_frame)
    
    def show_search_screen(self):
        self.clear_content()
        label = ttk.Label(self.content_frame, text="Search Screen - Coming Soon")
        label.pack(expand=True)
    
    def show_metadata_screen(self):
        self.clear_content()
        label = ttk.Label(self.content_frame, text="Metadata Screen - Coming Soon")
        label.pack(expand=True)