import ttkbootstrap as ttk
from main_window import MainWindow

def main():
    root = ttk.Window(
        title="CDMG File Manager",
        themename="litera",  # Back to original light theme
        size=(1024, 768),
        resizable=(True, True)
    )
    app = MainWindow(root) 
    root.mainloop()
 
if __name__ == "__main__":
    main()