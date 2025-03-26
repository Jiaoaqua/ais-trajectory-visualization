from flask import Flask, request, jsonify, send_file
import psycopg2
import pandas as pd
import os

# Flask app
app = Flask(__name__)

# PostgreSQL Connection Configuration
DB_HOST = "localhost"
DB_NAME = "ais_data"
DB_USER = "group_3"
DB_PASSWORD = "12345678"

# Connect to PostgreSQL
def connect_db():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


# Debug the error: default route to avoid 404 error 
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the AIS Vessel API!"})

# Fetch all AIS vessel data
@app.route("/api/vessels", methods=["GET"])
def get_all_vessels():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ais_vessel_turku;")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        cursor.close()
        conn.close()

        vessels = [dict(zip(column_names, row)) for row in rows]
        return jsonify(vessels)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Fetch vessel data by vessel ID
@app.route("/api/vessel/<vessel_id>", methods=["GET"])
def get_vessel_by_id(vessel_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ais_vessel_turku WHERE vessel_id = %s;", (vessel_id,))
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        cursor.close()
        conn.close()

        vessels = [dict(zip(column_names, row)) for row in rows]
        return jsonify(vessels)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Download latest vessel data as CSV
@app.route("/api/download", methods=["GET"])
def download_vessel_data():
    try:
        print("Received request for /api/download")  # Debug Step 1

        conn = connect_db()
        print("Database connection successful")  # Debug Step 2

        # Query to fetch the latest data, ordered by timestamp
        query = "SELECT * FROM ais_vessel_turku ORDER BY timestamp DESC LIMIT 100;"  # Fetching 100 most recent rows from the DB
        df = pd.read_sql(query, conn)
        print(f"Query executed successfully, fetched {len(df)} rows")  # Debug step 3
        conn.close()

        file_path = "ais_vessel_data.csv"
        df.to_csv(file_path, index=False)
        print(f"File saved at {file_path}")  # Debug step 4

        if not os.path.exists(file_path):
            print("File does not exist after saving!")
            return jsonify({"error": "File creation failed"}), 500

        print("Sending file to client")
        return send_file(file_path, as_attachment=True)

    except Exception as e:
        print(f"Error occurred: {e}")  # Debug 5
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
