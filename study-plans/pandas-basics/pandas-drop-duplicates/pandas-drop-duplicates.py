import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    df = pd.DataFrame(data)
    rows = list(df.shape)[0]
    df = df.drop_duplicates()
    rows_after = list(df.shape)[0]
    return [rows , rows_after , df.to_dict('list')]
    pass