import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    df = pd.DataFrame(data)
    df_selected = df[column]
    return {
        "values" : df_selected.values.tolist(),
        "length" : len(df_selected)
    }
    pass