import pandas as pd
import os

# Paths
input_file = r"C:\Users\Henkka\Desktop\PythonCourse\excelpython\excel_arranged.xlsx"
output_folder = os.path.dirname(input_file)  # Same folder as input file

# Read the cleaned Excel file
df = pd.read_excel(input_file, sheet_name="Employees")

# Columns to sort by
columns_to_sort = [
    "ID",
    "Namn",
    "Avdelning",
    "Lön (Euro-mån)",
    "Ålder",
    "Anställningsår"
]

# Loop over columns and create sorted files
for col in columns_to_sort:
    df_sorted = df.sort_values(by=col, ascending=True)
    output_file = os.path.join(output_folder, f"employees_arranged_by_{col}.xlsx")
    
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        df_sorted.to_excel(writer, sheet_name="Employees", index=False)
    
    print(f"✅ Created: {output_file} (sorted by {col})")