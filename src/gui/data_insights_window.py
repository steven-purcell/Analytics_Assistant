from tkinter import Toplevel, Frame, Scrollbar
import pandas as pd
from ydata_profiling import ProfileReport
import webbrowser
import tempfile
import os

class DataInsightsWindow:
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.window = Toplevel(master)
        self.window.title("Data Insights")
        self.window.geometry("800x600")

        self.frame = Frame(self.window)
        self.frame.pack(fill="both", expand=True)

        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.pack(side="right", fill="y")

        self.generate_insights()

    def generate_insights(self):
        profile = ProfileReport(self.data, minimal=True, title="Data Insights", explorative=True)
        insights = profile.to_html()

        # Save the HTML content to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_file:
            temp_file.write(insights.encode('utf-8'))
            temp_file_path = temp_file.name

        # Open the temporary file in the default web browser
        webbrowser.open(f"file://{os.path.abspath(temp_file_path)}")
        self.window.destroy()  # Close the Tkinter window after opening the browser