import pandas as pd
import os

# Paths
input_file = r"C:\Users\Henkka\Desktop\PythonCourse\excelpython\excel_arranged.xlsx"
output_file = r"C:\Users\Henkka\Desktop\pythonCourse\excelpython\employees_above_35.xlsx"

# Read the Excel file
df = pd.read_excel(input_file, sheet_name="Employees")

# Filter for employees older than 35
df_above_35 = df[df["Ålder"] > 35]

# Save the filtered DataFrame to a new Excel file
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    df_above_35.to_excel(writer, sheet_name="Employees_Above_35", index=False)

print(f"✅ Filtered Excel file saved as {output_file} (employees older than 35)")