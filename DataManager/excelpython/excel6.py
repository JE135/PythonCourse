import pandas as pd
import os

# Paths
input_file = r"C:\Users\User\Desktop\PythonCourse\excelpython\excel_arranged.xlsx"
output_file = r"C:\Users\User\Desktop\pythonCourse\excelpython\employees_above_35_after_2008_and_salary_above_3250_in_IT.xlsx"

# Read the Excel file
df = pd.read_excel(input_file, sheet_name="Employees")

# Strip column names to avoid accidental spaces
df.columns = df.columns.str.strip()

# Filter: age > 35 AND hired after 2008 AND salary > 3250 AND department is IT
df_filtered = df[
    (df["Ålder"] > 35) &
    (df["Anställningsår"] > 2008) &
    (df["Lön (Euro-mån)"] > 3250) &
    (df["Avdelning"] == "IT")
]

# Sort the filtered DataFrame by salary
df_filtered_sorted = df_filtered.sort_values(by="Lön (Euro-mån)", ascending=True)

# Save the filtered and sorted DataFrame to a new Excel file
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    df_filtered_sorted.to_excel(
        writer,
        sheet_name="Above_35_After_2008_Salary_Above_3250_in_T",
        index=False
    )

print(f"✅ Filtered Excel file saved as {output_file}")