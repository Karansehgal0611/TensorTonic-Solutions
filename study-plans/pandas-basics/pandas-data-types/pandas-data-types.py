import pandas as pd

def data_types_overview(data):
    """
    Returns: dict with 'dtypes', 'type_counts', 'num_columns'
    """
    df = pd.DataFrame(data)
    dtypes_dict = {col:str(dtypes) for col,dtypes in df.dtypes.items()}
    
    map_count = {}
    for col,dtypes in dtypes_dict.items():
        if dtypes in map_count.keys():
            map_count[dtypes] += 1
        else:
            map_count[dtypes] = 1
    return {
        "dtypes": dtypes_dict,
        "type_counts":map_count,
        "num_columns":len(df.columns)  
    }
    pass