#aligning samples, filtering genes, median-splits expression
def clean_expression(df):
    #this function converts all values to numeric and drops rows with any NaNs
    df = df.apply(pd.to_numeric, errors="coerce")
    df = df.dropna(axis=0, how="any")
    return df

def clean_clinical(df):
    #this function lowercases all column names to standardise
    df = df.rename(columns=str.lower)
    return df
