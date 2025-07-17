import os
import pandas as pd

# Path to the folder containing the CSV files
folder_path = '/Users/leahmoradi/Desktop/Education'
merged_data = pd.DataFrame()

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('Data.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        df['SourceFile'] = filename  # Optional: Add a column to track source
        merged_data = pd.concat([merged_data, df], ignore_index=True)

# Save the merged data to a new CSV
output_path = os.path.join(folder_path, 'merged_education_data.csv')
merged_data.to_csv(output_path, index=False)

print(f"Merged {len(merged_data)} rows into {output_path}")
