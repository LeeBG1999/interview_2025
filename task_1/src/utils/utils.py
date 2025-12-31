import pandas as pd

def calculate_statistics(df: pd.DataFrame) -> dict:
    
    result = {}
    for col in df.select_dtypes(include=['number']).columns:
        result[col] = {}
        result[col]['min_value'] = round(df[col].min(), 2)
        result[col]['max_value'] = round(df[col].max(), 2)
        result[col]['std_value'] = round(df[col].std(), 2)
        if len(df) <4:
            result[col]['kurtosis'] = None
        else:
            result[col]['kurtosis'] = round(df[col].kurtosis())
    
    return result