from tkinter import Tk, Frame, Button, Label, Toplevel, StringVar, OptionMenu
from tkinter import ttk
import pandas as pd
# from data_insights_window import DataInsightsWindow

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Main Window")
        master.geometry("800x600")

        self.frame = Frame(master)
        self.frame.pack(pady=20)

        self.label = Label(self.frame, text="Welcome to the Data Modeling and Discovery App", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.load_data_button = Button(self.frame, text="Load Data", command=self.open_data_window)
        self.load_data_button.pack(pady=10)

        self.explore_data_button = Button(self.frame, text="Explore Data", command=self.open_explore_window)
        self.explore_data_button.pack(pady=10)

        self.visualize_data_button = Button(self.frame, text="Visualize Data", command=self.open_plot_window)
        self.visualize_data_button.pack(pady=10)

        self.model_data_button = Button(self.frame, text="Model Data", command=self.open_model_window)
        self.model_data_button.pack(pady=10)

        # self.data = pd.read_csv("your_data.csv")  # Load your data here

        self.data_insights_button = Button(self.frame, text="Show Data Insights", command=self.show_data_insights)
        self.data_insights_button.pack(pady=10)

    def open_data_window(self):
        from .data_window import DataWindow
        data_window = DataWindow(self.master)
        self.master.wait_window(data_window.window)  # Wait for the data window to close
        self.data = data_window.data  # Set the loaded data

    def open_explore_window(self):
        from .explore_window import ExploreWindow

        if self.data is not None:
            self.explore_window = ExploreWindow(self.master, self.data)  # Pass the data argument
        else:
            print("No data loaded. Please load a CSV file first.")

    def open_plot_window(self):
        from .plot_window import PlotWindow

        if self.data is not None:
            self.plot_window = PlotWindow(self.master, self.data)  # Pass the data argument
        else:
            print("No data loaded. Please load a CSV file first.")

    def open_model_window(self):
        from .model_window import ModelWindow

        if self.data is not None:
            self.model_window = ModelWindow(self.master, self.data)  # Pass the data argument
        else:
            print("No data loaded. Please load a CSV file first.")

    def show_data_insights(self):
        from .data_insights_window import DataInsightsWindow
        DataInsightsWindow(self.master, self.data)

def main():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()