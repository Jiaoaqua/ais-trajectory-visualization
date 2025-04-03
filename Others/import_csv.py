import csv
import psycopg2

# PostgreSQL Connection Configuration
DB_HOST = "localhost"
DB_NAME = "ais_data"
DB_USER = "group_3"
DB_PASSWORD = "12345678"


def connect_db():
    """Connect to PostgreSQL and return the connection object."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None


def export_to_csv(filename="ais_vessel_data.csv"):
    """Export the latest 1 million rows from ais_vessel_turku table to a CSV file."""
    conn = connect_db()
    if conn is None:
        print("Failed to connect to database. Exiting.")
        return

    try:
        cursor = conn.cursor()
        query = """
        SELECT * FROM ais_vessel_turku
        ORDER BY timestamp DESC
        LIMIT 1000000;
        """
        cursor.execute(query)

        # Get column names
        columns = [desc[0] for desc in cursor.description]

        # Fetch all rows
        rows = cursor.fetchall()

        # Write data to CSV file
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(columns)  # Write header
            writer.writerows(rows)  # Write data rows

        cursor.close()
        conn.close()
        print(f"Latest 1 million rows successfully exported to {filename}")

    except Exception as e:
        print(f"Error exporting data to CSV: {e}")


if __name__ == "__main__":
    export_to_csv()
