from tkinter import Toplevel, Frame, Label, Button, filedialog, Text, Scrollbar
import pandas as pd

class DataWindow:
    def __init__(self, master):
        self.master = master
        self.window = Toplevel(master)
        self.window.title("Data Window")
        self.window.geometry("800x600")

        self.frame = Frame(self.window)
        self.frame.pack(fill="both", expand=True)

        self.label = Label(self.frame, text="Load and Preview CSV Data", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.load_button = Button(self.frame, text="Load CSV", command=self.load_csv)
        self.load_button.pack(pady=10)

        self.text_area = Text(self.frame, wrap="word")
        self.text_area.pack(fill="both", expand=True, padx=10, pady=10)

        self.scrollbar = Scrollbar(self.frame, command=self.text_area.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.text_area.config(yscrollcommand=self.scrollbar.set)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.data = pd.read_csv(file_path)
            self.display_data(file_path)
            # self.window.destroy()

    def display_data(self, file_path):
        try:
            data = pd.read_csv(file_path)
            self.text_area.delete(1.0, "end")
            self.text_area.insert("end", f"Data Preview:\n{data.head()}\n\n")
            # self.text_area.insert("end", f"Data Shape:\n{data.shape}\n{data.shape[0]} rows x {data.shape[1]} columns\n\n")
            self.text_area.insert("end", f"Descriptive Statistics:\n{data.describe()}\n\n")
            self.text_area.insert("end", f"Missing Values:\n{data.isnull().sum()}\n\n")
            self.text_area.insert("end", f"Data Types:\n{data.dtypes}\n")
        except Exception as e:
            self.text_area.delete(1.0, "end")
            self.text_area.insert("end", f"Error loading file: {e}")