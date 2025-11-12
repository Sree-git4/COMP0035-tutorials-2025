from pathlib import Path
import pandas as pd


def describe_dataframe(df: pd.DataFrame):
    """Describes summary statistics of the DataFrame.
    
    Parameters: df: pd.DataFrame (the DataFrame to describe)
    
    Returns: None
    """
    
    print("\nThe number of rows and columns\n", df.shape)
    pd.set_option("display.max_columns", None)
    print("\nThe first 5 rows\n", df.head(5))
    print("\nThe last 5 rows\n", df.tail(5))
    print("\nThe column labels\n", df.columns)
    print("\nThe column datatypes\n", df.dtypes)
    print("\nInfo\n", df.info())
    print("\nDescribe\n", df.describe())


if __name__ == '__main__':
    # Load the CSV file first
    paralympics_csv = Path(__file__).parent.parent.parent.joinpath('data', 'paralympics_raw.csv')
    # Read data from file to pandas dataframe
    events_csv_df = pd.read_csv(paralympics_csv)
    # Now describe the DataFrame
    describe_dataframe(events_csv_df)
