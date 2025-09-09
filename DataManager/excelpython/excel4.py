import pandas as pd
import os

# Paths
input_file = r"C:\Users\Henkka\Desktop\PythonCourse\excelpython\excel_arranged.xlsx"
output_file = r"C:\Users\Henkka\Desktop\pythonCourse\excelpython\employees_above_35_after_2008.xlsx"

# Read the Excel file
df = pd.read_excel(input_file, sheet_name="Employees")

# Filter: age > 35 AND hired after 2008
df_filtered = df[(df["Ålder"] > 35) & (df["Anställningsår"] > 2008)]

# Sort the filtered DataFrame by age
df_filtered_sorted = df_filtered.sort_values(by="Anställningsår", ascending=True)

# Save the filtered and sorted DataFrame to a new Excel file
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    df_filtered_sorted.to_excel(writer, sheet_name="Employees_Above_35_After_2008", index=False)

print(f"✅ Filtered and age-sorted Excel file saved as {output_file}")