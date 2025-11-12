from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

def data_histogram( df: pd.DataFrame):
    """Plot histogram from the DataFrame.
    
    Parameters: df: pd.DataFrame (the DataFrame to plot)
    
    Returns: matplotlib.axes.Axes (the plot axes)
    """
    columns=["participants_m", "participants_f"]
    ax = df[columns].hist()

    plt.savefig("data_histogram.png")

    plt.show()

if __name__ == '__main__':
   
    # Load the CSV file first
    paralympics_csv = Path(__file__).parent.parent.parent.joinpath('data', 'paralympics_raw.csv')
    # Read data from file to pandas dataframe
    events_csv_df = pd.read_csv(paralympics_csv)
    # Now plot the DataFrame
    data_histogram(events_csv_df)