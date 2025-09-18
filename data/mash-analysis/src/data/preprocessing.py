def load_data(file_path):
    """Load raw data from the specified file path."""
    import pandas as pd
    return pd.read_csv(file_path, sep='\t', index_col=0)

def clean_data(df):
    """Clean the data by removing missing values and duplicates."""
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def normalize_data(df):
    """Normalize the data using log2 transformation."""
    return df.apply(lambda x: np.log2(x + 1))

def preprocess_data(file_path):
    """Main function to preprocess the data."""
    raw_data = load_data(file_path)
    cleaned_data = clean_data(raw_data)
    normalized_data = normalize_data(cleaned_data)
    return normalized_data

def save_processed_data(df, output_path):
    """Save the processed data to the specified output path."""
    df.to_csv(output_path, sep='\t')