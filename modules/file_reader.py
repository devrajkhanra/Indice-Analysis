# modules/file_reader.py

import pandas as pd

def read_file(file_path):
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error while reading file '{file_path}': {e}")
        return None
