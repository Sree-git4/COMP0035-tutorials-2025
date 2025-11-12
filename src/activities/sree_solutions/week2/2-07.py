from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

def data_timeseries( df: pd.DataFrame):
    fig, axes = plt.subplots(ncols=2)

    df.plot(x="start", y="participants_m", ax=axes[0], title="Male participants")
    df.plot(x="start", y="participants_f", ax=axes[1], title="Female participants")

    axes[0].set_ylabel("Participants")
    plt.savefig("data_timeseries_split_columns.jpg")
    plt.show()

if __name__ == '__main__':
   
    # Load the CSV file first
    paralympics_csv = Path(__file__).parent.parent.parent.joinpath('data', 'paralympics_raw.csv')
    # Read data from file to pandas dataframe
    events_csv_df = pd.read_csv(paralympics_csv)
    # Now plot the DataFrame
    data_timeseries(events_csv_df)