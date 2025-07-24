
import pandas as pd

def load_data(filepath, file_type='csv'):
    """
    Loads data from a given filepath.
    Args:
        filepath (str): Path to the data file.
        file_type (str): Type of the file ('csv', 'excel', etc.).
    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    if file_type == 'csv':
        return pd.read_csv(filepath)
    elif file_type == 'excel':
        return pd.read_excel(filepath)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

def save_data(df, filepath, file_type='csv'):
    """
    Saves a DataFrame to a given filepath.
    Args:
        df (pd.DataFrame): DataFrame to save.
        filepath (str): Path to save the data file.
        file_type (str): Type of the file ('csv', 'excel', etc.).
    """
    if file_type == 'csv':
        df.to_csv(filepath, index=False)
    elif file_type == 'excel':
        df.to_excel(filepath, index=False)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

def clean_column_names(df):
    """
    Cleans DataFrame column names to be lowercase and replace spaces with underscores.
    Args:
        df (pd.DataFrame): Input DataFrame.
    Returns:
        pd.DataFrame: DataFrame with cleaned column names.
    """
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('[^a-zA-Z0-9_]', '', regex=True)
    return df