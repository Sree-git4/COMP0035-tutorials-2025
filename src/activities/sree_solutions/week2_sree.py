from pathlib import Path
from importlib import resources
import csv
from activities import data

# This script is located in the project root, so find the path to the current file and then go to the parent of that file
project_root = Path(__file__).parent.parent

# Find the .csv file relative to the project root and join to that path the data folder and then the example.csv file
csv_file = project_root.joinpath('data', 'paralympics_raw.csv')
# csv_file = project_root / 'data' / 'example.csv' # this notation would also work, even though you think the '/' is only unix/macOS

# Check if the file exists, this will print 'true' if it exists
print(csv_file.exists())

# Using importlib.resources to find the same file
paralympics_data_file_csv = resources.files(data).joinpath("paralympics_raw.csv")
if csv_file.exists():
    print(f"CSV file found: {csv_file}")
else:
    print("CSV file not found.")

#Checking by opening gile and printing a line
if __name__ == '__main__':
    data_file =  paralympics_data_file_csv = resources.files(data).joinpath("paralympics_raw.csv")
if csv_file.exists():
    print(f"CSV file found: {csv_file}")
else:
    print("CSV file not found.")

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    first_row = next(csv_reader)
    print(first_row)


