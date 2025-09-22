from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

# ---------------- CONFIG ---------------- #
DATA_FILE = "data.xlsx"
UPLOAD_FOLDER = os.path.join("static", "images")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------------- INIT EXCEL ---------------- #
def init_excel():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=[
            "ID", "Date", "Item Type", "Description",
            "Photo Path", "Status", "Returned To"
        ])
        df.to_excel(DATA_FILE, index=False, engine="openpyxl")

init_excel()

# ---------------- ROUTES ---------------- #

@app.route('/')
def homepage_en():
    return render_template('index.html')


# --- VIEW ITEMS --- #
@app.route('/find')
def find_item():
    df = pd.read_excel(DATA_FILE, engine="openpyxl")

    # Replace NaN in "Returned To" with empty string
    df["Returned To"] = df["Returned To"].fillna("")

    items = df.to_dict(orient="records")
    claim_id = request.args.get('claim')  # Show input for claiming specific item
    return render_template("find_item.html", items=items, claim_id=claim_id)


# --- SUBMIT ITEM --- #
@app.route('/submit', methods=["GET", "POST"])
def submit_item():
    if request.method == "POST":
        item_type = request.form.get("item_type")
        description = request.form.get("description")
        status = "Unclaimed"
        returned_to = ""

        # --- Handle uploaded photo ---
        photo = request.files.get("photo")
        photo_path = ""  # default empty if no photo

        if photo and photo.filename != "":
            # Save file to static/images/
            save_path = os.path.join(UPLOAD_FOLDER, photo.filename)
            photo.save(save_path)

            # Save relative path for Flask
            photo_path = f"images/{photo.filename}"

        # --- Load Excel ---
        df = pd.read_excel(DATA_FILE, engine="openpyxl")

        # --- Generate new ID ---
        new_id = f"#{len(df) + 1}"

        # --- Append new row ---
        new_row = {
            "ID": new_id,
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Item Type": item_type,
            "Description": description,
            "Photo Path": photo_path,
            "Status": status,
            "Returned To": returned_to
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_excel(DATA_FILE, index=False, engine="openpyxl")

        return redirect(url_for("find_item"))

    # GET request just renders the form
    return render_template("submit_item.html")


# --- CLAIM ITEM --- #
@app.route('/claim/<item_id>', methods=["POST"])
def claim_item(item_id):
    returned_to = request.form.get("returned_to", "")
    df = pd.read_excel(DATA_FILE, engine="openpyxl")

    if item_id in df["ID"].astype(str).values:
        df.loc[df["ID"].astype(str) == item_id, "Status"] = "Claimed"
        df.loc[df["ID"].astype(str) == item_id, "Returned To"] = returned_to
        df.to_excel(DATA_FILE, index=False, engine="openpyxl")

    return redirect(url_for("find_item"))

# --- UNCLAIM ITEM --- #
@app.route('/unclaim/<item_id>', methods=["POST"])
def unclaim_item(item_id):
    df = pd.read_excel(DATA_FILE, engine="openpyxl")

    if item_id in df["ID"].astype(str).values:
        df.loc[df["ID"].astype(str) == item_id, "Status"] = "Unclaimed"
        df.loc[df["ID"].astype(str) == item_id, "Returned To"] = ""
        df.to_excel(DATA_FILE, index=False, engine="openpyxl")

    return redirect(url_for("find_item"))


if __name__ == "__main__":
    app.run(debug=True)
