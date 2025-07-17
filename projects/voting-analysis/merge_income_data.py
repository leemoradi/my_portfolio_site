import os
import pandas as pd

# Correct full paths to your folders
income_folder = "/Users/leahmoradi/Desktop/Income"
education_folder = "/Users/leahmoradi/Desktop/Education"

def merge_csvs_from_folder(folder_path):
    merged_df = pd.DataFrame()
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv") and "Data" in filename:
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path, skiprows=1)
            year = filename.split(".")[0][-4:]  # Extract year from filename
            df["Year"] = year
            merged_df = pd.concat([merged_df, df], ignore_index=True)
    return merged_df

income_df = merge_csvs_from_folder(income_folder)
education_df = merge_csvs_from_folder(education_folder)

# Save merged files
income_df.to_csv("merged_income.csv", index=False)
education_df.to_csv("merged_education.csv", index=False)

print("✅ Merged CSVs created: merged_income.csv and merged_education.csv")

