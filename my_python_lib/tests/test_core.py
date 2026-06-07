import pandas as pd
import os


from my_python_lib.data import ConcurrentDataLoader
from my_python_lib.core import (
    MeanStrategy,
    MissingValueImputer,
    FeatureScaler,
    StandardMLPipeline
)


def create_fake_dataset():

    print("Creating 'messy_data.csv' for testing...")


    data = {
        'Age': [25.0, 30.0, None, 45.0, 50.0],
        'Salary': [50000.0, 60000.0, 75000.0, 90000.0, 110000.0],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    }

    df = pd.DataFrame(data)
    df.to_csv('messy_data.csv', index=False)
    print("Fake data created successfully.\n")


def run_test():
    create_fake_dataset()

    my_strategy = MeanStrategy()
    my_imputer = MissingValueImputer(strategy=my_strategy)

    my_scaler = FeatureScaler(method="minmax")

    my_loader = ConcurrentDataLoader()

    my_pipeline = StandardMLPipeline(
        loader=my_loader,
        imputer=my_imputer,
        scaler=my_scaler
    )

    cleaned_data = my_pipeline.execute_pipeline(
        file_path='messy_data.csv',
        missing_col='Age',
        scale_cols=['Age', 'Salary']
    )

    print("\n==================================")
    print("      FINAL CLEANED DATASET       ")
    print("==================================")
    print(cleaned_data)
    print("==================================\n")

    if os.path.exists('messy_data.csv'):
        os.remove('messy_data.csv')
        print("Cleaned up temporary 'messy_data.csv' file.")


if __name__ == "__main__":
    run_test()