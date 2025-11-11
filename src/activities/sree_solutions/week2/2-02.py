"""Read Paralympic data into pandas DataFrames.

This module follows the activity instructions:
- use pandas.read_csv for the CSV file
- use pandas.read_excel for the Excel file (both sheets)

It returns three DataFrames from the functions below. The script
does not print anything when it succeeds (per instructions).
"""

from importlib import resources
from activities import data
import pandas as pd


def load_paralympics_data():
    """Load the paralympics CSV and Excel sheets and return DataFrames.

    Returns
    -------
    tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]
        (paralympics_df, paralympics_excel_df, medals_df)
    """
    # Locate files inside the activities.data package
    csv_file = resources.files(data).joinpath('paralympics_raw.csv')
    excel_file = resources.files(data).joinpath('paralympics_all_raw.xlsx')

    # Read files using pandas
    paralympics_df = pd.read_csv(csv_file)
    paralympics_excel_df = pd.read_excel(excel_file, sheet_name=0)
    medals_df = pd.read_excel(excel_file, sheet_name=1)

    return paralympics_df, paralympics_excel_df, medals_df


if __name__ == '__main__':
    # Load data to verify there are no runtime errors. No output on success.
    _ = load_paralympics_data()
