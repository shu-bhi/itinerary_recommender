import pandas as pd

def load_user_data(file_path):
    """
    Load user data from the  CSV file.
    """
    return pd.read_csv(file_path)

def preprocess_data(df):
    """
    Basic preprocessing: handle missing values, text processing for reviews, etc.
    """
    # Fill missing values for vibe with 'Unknown'
    df['vibe'] = df['vibe'].fillna('Unknown')
    # Fill missing expenses with the mean of the column
    df['expenses'] = df['expenses'].fillna(df['expenses'].mean())
    return df

if __name__ == "__main__":
    # Load data from the CSV file
    user_data = load_user_data("../data/users.csv")
    # Preprocess the data
    cleaned_data = preprocess_data(user_data)
    print(cleaned_data)
