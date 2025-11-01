"""Module to demonstrate different approaches to locate the paralympics_raw.csv file."""

from pathlib import Path
from importlib import resources
from activities import data
import csv

# Approach 1: Using pathlib
# First, find the path to activities directory (two levels up from current file)
project_root = Path(__file__).parent.parent

# Find the .csv file relative to the activities directory
data_file_pathlib = project_root.joinpath('data', 'paralympics_raw.csv')

# Alternative pathlib syntax using '/' operator
data_file_pathlib_alt = project_root / 'data' / 'paralympics_raw.csv'

# Approach 2: Using importlib.resources (Python 10+ approach)
data_file_importlib = resources.files(data).joinpath('paralympics_raw.csv')

if __name__ == '__main__':
    # Verify pathlib approach
    print("\nVerifying pathlib approach:")
    if data_file_pathlib.exists():
        print(f"CSV file found at: {data_file_pathlib}")
        with open(data_file_pathlib) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            print(f"First row of data: {first_row}")
    else:
        print("CSV file not found using pathlib approach.")

    # Verify importlib approach
    print("\nVerifying importlib approach:")
    if data_file_importlib.exists():
        print(f"CSV file found at: {data_file_importlib}")
        with open(data_file_importlib) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            print(f"First row of data: {first_row}")
    else:
        print("CSV file not found using importlib approach.")
