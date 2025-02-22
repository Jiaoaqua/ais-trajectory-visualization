import uuid
import paho.mqtt.client as mqtt
import psycopg2
import json

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

# Store vessel metadata in Python memory
vessel_metadata = {}


# Connect to PostgreSQL
def connect_db():
    try:
        print("Connecting to PostgreSQL database")
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


# Create AIS Data Table
def create_table():
    print("Creating table if not exists")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ais_vessel_turku (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT NOW(),
            vessel_id TEXT,
            latitude DOUBLE PRECISION,
            longitude DOUBLE PRECISION,
            velocity DOUBLE PRECISION,
            heading DOUBLE PRECISION,
            cog DOUBLE PRECISION
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table setup complete.")


# Count distinct vessels
def count_vessels():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(DISTINCT vessel_id) FROM ais_vessel_turku;")
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        print(f"Total distinct vessels recorded: {count}")
    except Exception as e:
        print(f"Error in counting vessels: {e}")


# Define Turku region bounding box
LAT_MIN = 59.0
LAT_MAX = 62.0
LON_MIN = 19.5
LON_MAX = 25.0


# MQTT Message Callback
def on_message(client, userdata, message):
    msg_str = str(message.payload.decode('utf-8'))
    print('AIS-message received:\n', msg_str)
    message_topic = message.topic.split("/")
    
    if len(message_topic) > 2:
        vessel_id = message_topic[1]
        message_type = message_topic[2]

        if message_type == "location":
            location_msg = json.loads(msg_str)
            lat = location_msg['lat']
            lon = location_msg['lon']
            sog = location_msg.get('sog')
            heading = location_msg.get('heading')
            cog = location_msg.get('cog')

            # Only insert if vessel is inside Turku area
            if LAT_MIN <= lat <= LAT_MAX and LON_MIN <= lon <= LON_MAX:
                try:
                    conn = connect_db()
                    cursor = conn.cursor()
                    cursor.execute("""
                        INSERT INTO ais_vessel_turku (vessel_id, latitude, longitude, velocity, heading, cog) 
                        VALUES (%s, %s, %s, %s, %s, %s);
                    """, (vessel_id, lat, lon, sog, heading, cog))
                    conn.commit()
                    cursor.close()
                    conn.close()
                    print(f"Inserted into DB: {vessel_id}, {lat}, {lon}, {sog}, {heading}, {cog}")
                except Exception as e:
                    print(f"Error inserting into DB: {e}")

        elif message_type == "metadata":
            metadata_msg = json.loads(msg_str)
            vessel_name = metadata_msg.get('name', "Unknown")
            vessel_destination = metadata_msg.get('destination', "Unknown")

            # Store metadata in Python memory
            if vessel_id not in vessel_metadata:
                vessel_metadata[vessel_id] = {}

            vessel_metadata[vessel_id]['name'] = vessel_name
            vessel_metadata[vessel_id]['destination'] = vessel_destination

            print(f"Added metadata for vessel {vessel_id}: Name = {vessel_name}, Destination = {vessel_destination}")
            print("Added name and destination:", vessel_metadata[vessel_id])


# Retrieve stored metadata
def get_vessel_metadata():
    return vessel_metadata


# MQTT Connection Callback
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT.", MQTT_BROKER, ":", MQTT_PORT)
        client.subscribe(MQTT_TOPIC)
        print(f"Subscribed to topic: {MQTT_TOPIC}")
    else:
        print('Connection to', MQTT_BROKER, ":", MQTT_PORT, 'failed with return code:', rc)


# MQTT Client
print("Initializing MQTT client...")
client_name = f"{APP_NAME}; {uuid.uuid4()}"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_name, transport="websockets")

client.on_connect = on_connect
client.on_message = on_message

client.tls_set()
print("Connecting to MQTT broker...")
client.connect(MQTT_BROKER, MQTT_PORT)

print("MQTT broker connection initiated.")

# Run Script
if __name__ == "__main__":
    print("Starting script")
    create_table()  # Ensure table exists
    count_vessels()  # Show vessel count
    print("Listening for AIS data...")
    client.loop_forever()  # Keep listening
