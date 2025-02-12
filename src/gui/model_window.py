from tkinter import Toplevel, Frame, Label, Button, Text, Scrollbar, StringVar, OptionMenu
import pandas as pd
from models.modeling import model_data

class ModelWindow:
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.window = Toplevel(master)
        self.window.title("Model Data")
        self.window.geometry("800x600")

        self.frame = Frame(self.window)
        self.frame.pack(fill="both", expand=True)

        self.label = Label(self.frame, text="Data Modeling", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # Dropdown for selecting target column
        self.target_column_var = StringVar(self.frame)
        self.target_column_var.set('Select Target Column')  # Default value

        self.target_column_menu = OptionMenu(self.frame, self.target_column_var, *self.data.columns)
        self.target_column_menu.pack(pady=10)

        # Button to start modeling
        self.start_button = Button(self.frame, text="Start Modeling", command=self.start_modeling)
        self.start_button.pack(pady=10)

        self.text_area = Text(self.frame, wrap="word")
        self.text_area.pack(fill="both", expand=True, padx=10, pady=10)

        self.scrollbar = Scrollbar(self.frame, command=self.text_area.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.text_area.config(yscrollcommand=self.scrollbar.set)

    def start_modeling(self):
        self.display_modeling()

    def display_modeling(self):
        try:
            self.text_area.delete(1.0, "end")

            # Get the selected target column
            target_column = self.target_column_var.get()
            if target_column == 'Select Target Column':
                self.text_area.insert("end", "Please select a target column.\n")
                return

            # Train models and get results
            best_model_name, best_model_score, feature_importance = model_data(self.data, target_column)

            # Display results
            self.text_area.insert("end", f"Best Model: {best_model_name}\n")
            self.text_area.insert("end", f"Score: {best_model_score}\n\n")

            if feature_importance is not None:
                self.text_area.insert("end", "Feature Importances:\n")
                for feature, importance in zip(self.data.drop(columns=[target_column]).columns, feature_importance):
                    self.text_area.insert("end", f"{feature}: {importance:.4f}\n")
            else:
                self.text_area.insert("end", "Feature importances are not available for the selected model.\n")

        except Exception as e:
            self.text_area.delete(1.0, "end")
            self.text_area.insert("end", f"Error displaying modeling: {e}")