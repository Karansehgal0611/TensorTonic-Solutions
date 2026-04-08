import pandas as pd

def head_tail(data, n):
    """
    Returns: dict with 'head' and 'tail' (both dicts of column -> list)
    """
    df = pd.DataFrame(data)
    head_df = df.head(n)
    tail_df = df.tail(n)
    return {
        "head":head_df.to_dict('list'),
        "tail":tail_df.to_dict('list')
    }
    pass