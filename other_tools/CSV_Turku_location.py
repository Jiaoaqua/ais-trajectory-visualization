import pandas as pd
import psycopg2

# PostgreSQL Connection Configuration
DB_HOST = "localhost"
DB_NAME = "ais_data"
DB_USER = "group_3"
DB_PASSWORD = "12345678"

# MQTT Configuration
MQTT_BROKER = "meri.digitraffic.fi"
MQTT_PORT = 443
MQTT_TOPIC = "vessels-v2/#"
APP_NAME = "AIS_Traffic_Turku"

#  Function to connect to PostgreSQL
def connect_db():
    try:
        print("Connecting to PostgreSQL database...")
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("Connected to PostgreSQL successfully.")
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise

try:
    # Establish database connection
    conn = connect_db()

    # Query to get vessel data in Turku region (which is able to be adjusted)
    query = """
    SELECT vessel_id, latitude, longitude
    FROM ais_vessel_turku
    WHERE latitude BETWEEN 59.0 AND 62.0
    AND longitude BETWEEN 19.5 AND 25.0;
    """

    # Load data into Pandas with read sql
    df = pd.read_sql(query, conn)

    # Save to CSV file
    df.to_csv("turku_ais_data.csv", index=False)
    print("CSV file created: turku_ais_data.csv")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close connection
    if 'conn' in locals() and conn is not None:
        conn.close()
        print("Database connection closed.")
