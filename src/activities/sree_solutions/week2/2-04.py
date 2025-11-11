import pandas as pd
from pathlib import Path

def check_dataframe(df: pd.DataFrame):
    """Check and print basic information about the DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to check.

    Returns
    -------
    None
    """
    print("DataFrame is NA values:", df.isna(), end="\n\n")
    print("DataFrame is Null values:", df.isnull())

def missing_dataframe(df:  pd.DataFrame):
    """Check and print missing values information about the DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to check.

    Returns
    -------
    None
    """
    missing_rows = df[df.isna().any(axis=1)]
    print("Rows with missing values:\n", missing_rows)

    missing_columns = df.columns[df.isna().any(axis=0)]
    print("Columns with missing values:\n", missing_columns)

if __name__ == '__main__':
    # Load the CSV file first
    project_root = Path(__file__).parent.parent.parent
    paralympics_csv = project_root.joinpath('data',
                                            'paralympics_raw.csv')
    # Read data from file to pandas dataframe
    events_csv_df = pd.read_csv(paralympics_csv)
    
    # Now describe the DataFrame
    check_dataframe(events_csv_df)

    print()
    missing_dataframe(events_csv_df)