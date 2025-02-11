from tkinter import Toplevel, Frame, Label, Button, StringVar, OptionMenu
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

class PlotWindow:
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.window = Toplevel(master)
        self.window.title("Plot Window")
        self.window.geometry("600x400")

        self.selected_column = StringVar(self.window)
        self.column_options = self.data.columns.tolist()

        self.create_widgets()

    def create_widgets(self):
        Label(self.window, text="Select Column for Plotting:").pack(pady=10)

        OptionMenu(self.window, self.selected_column, *self.column_options).pack(pady=10)

        Button(self.window, text="Generate Histogram", command=self.plot_histogram).pack(pady=5)
        Button(self.window, text="Generate Box Plot", command=self.plot_box).pack(pady=5)
        Button(self.window, text="Generate Scatter Plot", command=self.plot_scatter).pack(pady=5)
        Button(self.window, text="Generate Correlation Heatmap", command=self.plot_heatmap).pack(pady=5)

    def plot_histogram(self):
        column = self.selected_column.get()
        data_column = self.data[column]

        # # Encode categorical column if necessary
        # if data_column.dtype == 'object' or data_column.dtype.name == 'category':
        #     label_encoder = LabelEncoder()
        #     data_column = label_encoder.fit_transform(data_column)

        plt.figure(figsize=(8, 6))
        sns.histplot(data_column, kde=True)
        plt.title(f"Histogram of {column}")
        plt.show()

    def plot_box(self):
        plt.figure(figsize=(8, 6))
        sns.boxplot(y=self.data[self.selected_column.get()])
        plt.title(f"Box Plot of {self.selected_column.get()}")
        plt.show()

    def plot_scatter(self):
        if len(self.column_options) < 2:
            print("Need at least two columns for scatter plot.")
            return
        x_column = self.column_options[0]  # Default to first column
        y_column = self.selected_column.get()
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=self.data[x_column], y=self.data[y_column])
        plt.title(f"Scatter Plot of {y_column} vs {x_column}")
        plt.show()

    def plot_heatmap(self):
        # Encode categorical columns if necessary
        data_encoded = self.data.copy()
        for column in data_encoded.select_dtypes(include=['object', 'category']).columns:
            label_encoder = LabelEncoder()
            data_encoded[column] = label_encoder.fit_transform(data_encoded[column])

        plt.figure(figsize=(10, 8))
        correlation_matrix = data_encoded.corr()
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.show()