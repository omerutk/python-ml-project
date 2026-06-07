import pandas as pd
import concurrent.futures
import os


# 5. CONCURRENT DATA LOADER

class ConcurrentDataLoader:
    def __init__(self):
        pass

    def load_single_file(self, filepath):
        """This function handles loading just one file."""
        print(f"Reading {filepath} on a separate thread...")

        return pd.read_csv(filepath)

    def load_multiple_files(self, filepaths):
        """This function loads multiple files at the exact same time."""
        print(f"Starting concurrent load for {len(filepaths)} files...")

        loaded_dataframes = []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(self.load_single_file, filepaths)

            for df in results:
                loaded_dataframes.append(df)

        print("All files loaded successfully!")

        combined_dataframe = pd.concat(loaded_dataframes, ignore_index=True)
        return combined_dataframe





