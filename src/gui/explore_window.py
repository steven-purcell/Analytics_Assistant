from tkinter import Toplevel, Frame, Label, Text, Scrollbar
import pandas as pd

class ExploreWindow:
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.window = Toplevel(master)
        self.window.title("Explore Data")
        self.window.geometry("800x600")

        self.frame = Frame(self.window)
        self.frame.pack(fill="both", expand=True)

        self.label = Label(self.frame, text="Data Exploration", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.text_area = Text(self.frame, wrap="word")
        self.text_area.pack(fill="both", expand=True, padx=10, pady=10)

        self.scrollbar = Scrollbar(self.frame, command=self.text_area.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.text_area.config(yscrollcommand=self.scrollbar.set)

        self.display_exploration()

    def display_exploration(self):
        try:
            self.text_area.delete(1.0, "end")
            self.text_area.insert("end", f"Data Preview:\n{self.data.head()}\n\n")
            self.text_area.insert("end", f"Descriptive Statistics:\n{self.data.describe()}\n\n")
            self.text_area.insert("end", f"Missing Values:\n{self.data.isnull().sum()}\n\n")
            self.text_area.insert("end", f"Data Types:\n{self.data.dtypes}\n")
        except Exception as e:
            self.text_area.delete(1.0, "end")
            self.text_area.insert("end", f"Error displaying data: {e}")