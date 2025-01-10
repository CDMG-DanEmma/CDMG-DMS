import ttkbootstrap as ttk
from tkinter import *
from tkinter import filedialog

class JobsScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=BOTH, expand=True, padx=10, pady=5)
        
        # Create left and right frames
        self.left_frame = ttk.Frame(self)
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        
        self.right_frame = ttk.Frame(self)
        self.right_frame.pack(side=RIGHT, fill=BOTH, padx=5)
        
        self._create_project_selector()
        self._create_recent_projects() 
        self._create_project_info()
        
    def _create_project_selector(self):
        # Project selection frame
        select_frame = ttk.LabelFrame(self.left_frame, text="Select Project", padding=10)
        select_frame.pack(fill=X, pady=5)
        
        # Project entry with autocomplete (placeholder)
        self.project_var = StringVar()
        self.project_entry = ttk.Entry(select_frame, textvariable=self.project_var)
        self.project_entry.pack(fill=X, pady=5)
        
        # Browse button
        self.browse_btn = ttk.Button(select_frame, text="Browse", command=self._browse_project)
        self.browse_btn.pack(pady=5)
        
    def _create_recent_projects(self):
        # Recent projects frame
        recent_frame = ttk.LabelFrame(self.left_frame, text="Recent Projects", padding=10)
        recent_frame.pack(fill=BOTH, expand=True, pady=5)
        
        # Recent projects listbox
        self.recent_listbox = ttk.Treeview(
            recent_frame, 
            columns=("project", "last_accessed"),
            show="headings",
            selectmode="browse"
        )
        self.recent_listbox.heading("project", text="Project")
        self.recent_listbox.heading("last_accessed", text="Last Accessed")
        self.recent_listbox.pack(fill=BOTH, expand=True)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(recent_frame, orient=VERTICAL, command=self.recent_listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.recent_listbox.configure(yscrollcommand=scrollbar.set)
        
    def _create_project_info(self):
        # Project info frame
        info_frame = ttk.LabelFrame(self.right_frame, text="Project Information", padding=10)
        info_frame.pack(fill=BOTH, expand=True)
        
        # Placeholder for project details (will be populated from SQL Server later)
        info_labels = [
            ("Project Number:", "TBD"),
            ("Project Name:", "TBD"),
            ("Client:", "TBD"),
            ("Status:", "TBD"),
            ("Total Hours:", "TBD"),
        ]
        
        for label, value in info_labels:
            frame = ttk.Frame(info_frame)
            frame.pack(fill=X, pady=2)
            ttk.Label(frame, text=label).pack(side=LEFT)
            ttk.Label(frame, text=value).pack(side=RIGHT)
            
    def _browse_project(self):
        project_path = filedialog.askdirectory(
            title="Select Project Folder",
            mustexist=True
        )
        
        if project_path:
            # Update entry with selected path
            self.project_var.set(project_path)
            
            # Add placeholder to save to recent projects
            self._add_to_recent_projects(project_path)
            
            # Update project info (placeholder for now)
            self._update_project_info(project_path)

    def _add_to_recent_projects(self, project_path):
        # Get project name from path
        project_name = project_path.split('/')[-1]
        
        # Add to treeview (temporary - will be replaced with database)
        self.recent_listbox.insert(
            '', 
            'end', 
            values=(project_name, "Just now")
        )
    
    def _update_project_info(self, project_path):
        # Placeholder - will be replaced with actual SQL Server data
        project_name = project_path.split('/')[-1]
        info = {
            "Project Number:": project_name,
            "Project Name:": project_name,
            "Client:": "Loading...",
            "Status:": "Active",
            "Total Hours:": "Loading..."
        }
        
        # Update info labels
        for widget in self.right_frame.winfo_children():
            if isinstance(widget, ttk.LabelFrame):
                for frame in widget.winfo_children():
                    if isinstance(frame, ttk.Frame):
                        label_widget = frame.winfo_children()[0]
                        label_text = label_widget.cget("text")
                        if label_text in info:
                            value_widget = frame.winfo_children()[1]
                            value_widget.config(text=info[label_text])