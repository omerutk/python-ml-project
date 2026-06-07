# Helper functions

def check_missing_values(dataframe):

    print("\n--- Missing Values Report ---")
    missing_counts = dataframe.isnull().sum()
    print(missing_counts[missing_counts > 0])
    print("-----------------------------\n")

    return dataframe.isnull().values.any()