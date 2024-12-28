# main.py
import logging
import multiprocessing
from tkinter import messagebox
import traceback
from gui import run_gui

if __name__ == "__main__":
    try:
        multiprocessing.freeze_support()  # Required for Windows executables
        run_gui()
    except Exception as e:
        logging.critical(f"Critical error in main: {str(e)}\n{traceback.format_exc()}")
        messagebox.showerror("Critical Error", f"A critical error occurred:\n{str(e)}")