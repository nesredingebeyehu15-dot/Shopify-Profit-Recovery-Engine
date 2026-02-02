import pandas as pd
import os

def load_raw_data(file_path):
    """
    Loads raw data from a CSV file and converts date columns to datetime objects.
    
    Args:
        file_path (str): The relative or absolute path to the CSV file.
        
    Returns:
        pd.DataFrame: The loaded and processed dataframe.
    
    Raises:
        FileNotFoundError: If the file does not exist.
    """
    
    # 1. Check if file exists (Fail Loud)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Error: The file at '{file_path}' was not found. Please check the path.")
    
    try:
        print(f"🔄 Loading data from: {file_path}...")
        df = pd.read_csv(file_path)
        
        # 2. Identify and Convert Date Columns
        # We look for 'timestamp' or 'date' in column names (Common in Shopify/Olist)
        date_cols = [col for col in df.columns if 'timestamp' in col or 'date' in col]
        
        if date_cols:
            print(f"📅 Detected date columns: {date_cols}")
            for col in date_cols:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            print(f"✅ Successfully converted {len(date_cols)} columns to datetime objects.")
        else:
            print("⚠️ No date columns detected. Skipping date conversion.")

        print(f"🎉 Data Loaded Successfully! Shape: {df.shape}")
        return df

    except Exception as e:
        # Catch other errors (like corrupted CSVs)
        raise RuntimeError(f"❌ Critical Error loading data: {e}")

if __name__ == "__main__":
    # Test Execution
    # Using os.path.join for cross-platform compatibility
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    test_path = os.path.join(base_dir, "data", "raw", "olist_orders_dataset.csv")
    
    try:
        df = load_raw_data(test_path)
        print(df.info())
    except Exception as e:
        print(e)