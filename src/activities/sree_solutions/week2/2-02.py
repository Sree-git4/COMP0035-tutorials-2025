import pandas as pd
from pathlib import Path

def main():
    # Get the path to the data files
    project_root = Path(__file__).parent.parent.parent  # Navigate up to activities folder
    csv_file = project_root.joinpath('data', 'paralympics_raw.csv')    
    excel_file = project_root.joinpath('data', 'paralympics_all_raw.csv')    

    paralympics_csv_df = pd.read_csv(csv_file)

    print("CSV file read successfully!")
    
    # Read both sheets from Excel file
    print("\nTrying to read Excel sheets...")
    int name_of_sheet = 0
    while name_of_sheet <2:
        print((name_of_sheet) "Excel sheet read successfully!")
        paralympics_excel_df = pd.read_excel(excel_file, sheet_name="name_of_sheet")
        name_of_sheet += 1
    break 

main()