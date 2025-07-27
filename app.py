import os
import pandas as pd
import requests
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

def fetch_data(url="https://sms.ilmwasooli.com/temp/gettestingdata"):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "success" and "Data" in data:
            df = pd.DataFrame(data["Data"])
            df.columns = [col.lower() for col in df.columns]
            return df
        else:
            print("API response did not indicate success or was missing data.")
            return pd.DataFrame()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

@app.route('/api/filters')
def get_filters():
    df = fetch_data()
    if df.empty:
        return jsonify({"classes": [], "statuses": []})
    unique_classes = sorted(df['class'].dropna().unique().tolist())
    unique_statuses = sorted(df['status'].dropna().unique().tolist())
    return jsonify({
        "classes": unique_classes,
        "statuses": unique_statuses
    })

@app.route('/api/data')
def get_filtered_data():
    df = fetch_data()
    if df.empty:
        return jsonify([])

    search_all = request.args.get('searchAll', '').strip().lower()
    search_class = request.args.get('searchClass', '').strip().lower()
    search_status = request.args.get('searchStatus', '').strip().lower()
    search_id_name = request.args.get('searchIdName', '').strip().lower()

    filtered = df.copy()
    for col in filtered.columns:
        filtered[col] = filtered[col].astype(str)

    if search_class:
        filtered = filtered[filtered['class'].str.lower() == search_class]
    if search_status:
        filtered = filtered[filtered['status'].str.lower() == search_status]
    if search_id_name:
        filtered = filtered[
            filtered['id'].str.lower().str.contains(search_id_name, na=False) |
            filtered['name'].str.lower().str.contains(search_id_name, na=False)
        ]
    if search_all:
        filtered = filtered[filtered.apply(
            lambda row: any(search_all in str(cell).lower() for cell in row[['id', 'name', 'class', 'status']]),
            axis=1
        )]
    result = filtered.to_dict(orient='records')
    return jsonify(result)

@app.route('/')
def home():
    return render_template('index.html')

# --- Main Execution ---
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
