import pandas as pd
import numpy as np


# 1. THE STRATEGY "INTERFACE"

class ImputationStrategy:
    def calculate_fill_value(self, column_data):
        raise NotImplementedError("Do not use the base class! Use a specific strategy.")


# 2. THE CONCRETE STRATEGIES


class MeanStrategy(ImputationStrategy):
    def calculate_fill_value(self, column_data):
        return column_data.mean()


class MedianStrategy(ImputationStrategy):
    def calculate_fill_value(self, column_data):
        return column_data.median()


class ModeStrategy(ImputationStrategy):
    def calculate_fill_value(self, column_data):
        return column_data.mode()[0]


# 3. THE MAIN IMPUTER CLASS

class MissingValueImputer:
    def __init__(self, strategy):
        self.strategy = strategy

    def fill_missing_data(self, dataframe, column_name):
        print(f"Fixing missing values in column '{column_name}'...")

        col_data = dataframe[column_name]

        fill_number = self.strategy.calculate_fill_value(col_data)
        print(f"Calculated fill value is: {fill_number}")

        dataframe[column_name] = dataframe[column_name].fillna(fill_number)

        return dataframe



# 4. FEATURE SCALER (Functional Programming)

class FeatureScaler:
    def __init__(self, method="minmax"):
        self.method = method

    def scale_data(self, dataframe, columns_to_scale):
        print(f"Scaling columns: {columns_to_scale} using {self.method}...")

        # FUNCTIONAL PROGRAMMING ELEMENT

        def calculate_min_max(val, col_min, col_max):
            if col_max == col_min:
                return 0.0
            return (val - col_min) / (col_max - col_min)

        def calculate_standard(val, col_mean, col_std):
            if col_std == 0:
                return 0.0
            return (val - col_mean) / col_std

        for col in columns_to_scale:
            col_data = dataframe[col]

            if self.method == "minmax":
                c_min = col_data.min()
                c_max = col_data.max()


                dataframe[col] = list(map(lambda x: calculate_min_max(x, c_min, c_max), col_data))

            elif self.method == "standard":
                c_mean = col_data.mean()
                c_std = col_data.std()

                dataframe[col] = list(map(lambda x: calculate_standard(x, c_mean, c_std), col_data))

        return dataframe



# 6. RECURSION (Configuration Parser)


def parse_pipeline_config(config_dict):
    extracted_settings = []

    for key, value in config_dict.items():
        if isinstance(value, dict):
            print(f"Digging into nested configuration: {key}...")
            extracted_settings.extend(parse_pipeline_config(value))
        else:
            extracted_settings.append((key, value))

    return extracted_settings



# 7. THE TEMPLATE METHOD PATTERN

class BasePipelineTemplate:


    def execute_pipeline(self, file_path, missing_col, scale_cols):
        print("\n=== Starting ML Preprocessing Pipeline ===")

        dataset = self.step_load_data(file_path)
        dataset = self.step_impute_missing(dataset, missing_col)
        dataset = self.step_scale_features(dataset, scale_cols)

        print("=== Pipeline Complete ===\n")
        return dataset

    def step_load_data(self, file_path):
        raise NotImplementedError()

    def step_impute_missing(self, dataset, col_name):
        raise NotImplementedError()

    def step_scale_features(self, dataset, cols):
        raise NotImplementedError()


# 8. OUR CONCRETE PIPELINE

class StandardMLPipeline(BasePipelineTemplate):

    def __init__(self, loader, imputer, scaler):
        self.loader = loader
        self.imputer = imputer
        self.scaler = scaler

    def step_load_data(self, file_path):
        return self.loader.load_multiple_files([file_path])

    def step_impute_missing(self, dataset, col_name):
        return self.imputer.fill_missing_data(dataset, col_name)

    def step_scale_features(self, dataset, cols):
        return self.scaler.scale_data(dataset, cols)