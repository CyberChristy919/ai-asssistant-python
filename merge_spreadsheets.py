import pandas as pd

file1 = input("Enter the name of the first Excel file: ")
file2 = input("Enter the name of the second Excel file: ")

df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

print("\nColumns in first file:")
print(list(df1.columns))

print("\nColumns in second file:")
print(list(df2.columns))

column1 = input("\nEnter the column from the first file to merge on: ")
column2 = input("Enter the column from the second file to merge on: ")

merged_df = pd.merge(df1, df2, left_on=column1, right_on=column2)

merged_df.to_excel("merged_output.xlsx", index=False)

print("\nMerged spreadsheet saved as merged_output.xlsx")
