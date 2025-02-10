def load_csv(file_path):
    import pandas as pd
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None

def generate_report(data):
    if data is not None:
        report = {
            'shape': data.shape,
            'columns': data.columns.tolist(),
            'dtypes': data.dtypes.astype(str).to_dict(),
            'missing_values': data.isnull().sum().to_dict(),
            'descriptive_stats': data.describe(include='all').to_dict()
        }
        return report
    return None

def visualize_data(data, columns):
    import matplotlib.pyplot as plt
    import seaborn as sns

    if not columns or len(columns) == 0:
        print("No columns selected for visualization.")
        return

    for column in columns:
        if column in data.columns:
            plt.figure(figsize=(10, 6))
            sns.histplot(data[column], kde=True)
            plt.title(f'Distribution of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.show()
        else:
            print(f"Column {column} does not exist in the data.")