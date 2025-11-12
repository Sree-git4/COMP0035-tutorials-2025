from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

def data_plot (df: pd.DataFrame):
    """Plot data from the DataFrame.
    
    Parameters: df: pd.DataFrame (the DataFrame to plot)
    
    Returns: matplotlib.axes.Axes (the plot axes)
    """

    ax = df.plot(title='Events Plot', xlabel='X-axis Label', ylabel='Y-axis Label')

    plt.savefig("sample_plot.png")

    plt.show()

if __name__ == '__main__':
    # Load the CSV file first
    paralympics_csv = Path(__file__).parent.parent.parent.joinpath('data', 'paralympics_raw.csv')
    # Read data from file to pandas dataframe
    events_csv_df = pd.read_csv(paralympics_csv)
    # Now plot the DataFrame
    data_plot(events_csv_df)

""" 

Noted that I can think of various countries 
and their sports stuff as a time series plot


"""