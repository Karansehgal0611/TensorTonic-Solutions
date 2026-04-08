import pandas as pd

def select_column(data, column):
    df = pd.DataFrame(data)
    col_required = df[column]
    result = {
        "values" : col_required.tolist(),
        "length" : len(col_required)
    }
    return result
    pass