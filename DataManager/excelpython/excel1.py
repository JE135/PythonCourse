import pandas as pd

input_file = r"C:\Users\User\Desktop\PythonCourse\excelpython\excel_unarranged.xlsx"
output_file = r"C:\Users\User\Desktop\PythonCourse\excelpython\excel_arranged.xlsx"

df_raw = pd.read_excel(input_file, header=None)
lines = df_raw[0].dropna().astype(str).tolist()
data = [line.split(",") for line in lines]

headers = ["ID", "Namn", "Avdelning", "Lön (Euro-mån)", "Ålder", "Anställningsår"]
df = pd.DataFrame(data[1:], columns=headers)

df["Lön (Euro-mån)"] = pd.to_numeric(df["Lön (Euro-mån)"], errors="coerce")
df["Ålder"] = pd.to_numeric(df["Ålder"], errors="coerce")
df["Anställningsår"] = pd.to_numeric(df["Anställningsår"], errors="coerce")

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Employees", index=False)

print(f"✅ Cleaned Excel file saved as {output_file}")