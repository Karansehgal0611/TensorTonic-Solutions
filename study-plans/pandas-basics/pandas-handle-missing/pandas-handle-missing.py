import pandas as pd

def handle_missing(data, fill_value):
    """
    Returns: dict with 'null_counts' (dict) and 'cleaned_data' (dict)
    """
    df = pd.DataFrame(data)
    null_countsdf = {k: int(v) for k, v in df.isnull().sum().items()}
    df_cleaned = df.fillna(fill_value)
    return {
        "null_counts" : null_countsdf,
        "cleaned_data" : df_cleaned.to_dict('list')
    }
    
    pass