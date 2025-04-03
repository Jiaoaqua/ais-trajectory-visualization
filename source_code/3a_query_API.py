from flask import Flask, request, jsonify, send_file
import psycopg2
import pandas as pd
import os
import datetime

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

# Convert epoch timestamp to human-readable format
def convert_epoch_to_datetime(epoch):
    return datetime.datetime.utcfromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')

# Debug error message - Welcome message for the API
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
        return jsonify(vessels) #Return the data to a JSON file
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

# API to fetch vessel data within a specific time interval
@app.route("/api/query", methods=["POST"])
def query_vessel_data():
    try:
        query_information = request.json

        if "begin" not in query_information or "end" not in query_information: #Check if the 'begin' and 'end' timestamps are in the request
            return jsonify({"error": "Missing 'begin' or 'end' in request"}), 400

        # Convert 'begin' and 'end' into  epoch time
        begin_epoch = int(query_information["begin"])
        end_epoch = int(query_information["end"])

        # Convert the epoch times to human readable datetime format
        begin_datetime = convert_epoch_to_datetime(begin_epoch)
        end_datetime = convert_epoch_to_datetime(end_epoch)

        conn = connect_db()
        cursor = conn.cursor()

        # query to get data for the given time interval
        query = """
            SELECT * FROM ais_vessel_turku
            WHERE timestamp > %s AND timestamp < %s;
        """
        cursor.execute(query, (begin_datetime, end_datetime))
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

        cursor.close()
        conn.close()

        vessels = [dict(zip(column_names, row)) for row in rows]
        return jsonify({
            "query_received": query_information,
            "converted_timestamps": {"begin": begin_datetime, "end": end_datetime},
            "results": vessels
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API to download queried vessel data to CSV file
@app.route("/api/download-query", methods=["POST"])
def download_query_data():
    try:
        query_information = request.json

        if "begin" not in query_information or "end" not in query_information:
            return jsonify({"error": "Missing 'begin' or 'end' in request"}), 400

        begin_epoch = int(query_information["begin"])
        end_epoch = int(query_information["end"])

        begin_datetime = convert_epoch_to_datetime(begin_epoch)
        end_datetime = convert_epoch_to_datetime(end_epoch)

        conn = connect_db()

        query = """
            SELECT * FROM ais_vessel_turku
            WHERE timestamp > %s AND timestamp < %s;
        """
        df = pd.read_sql(query, conn, params=(begin_datetime, end_datetime))
        conn.close()

        file_path = "/home/ubuntu/project/dep_proj_3/coding/ais_vessel_query.csv" ## Save the DataFrame to a CSV file
        df.to_csv(file_path, index=False)

        if not os.path.exists(file_path):
            return jsonify({"error": "File creation failed"}), 500

        return send_file(file_path, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
