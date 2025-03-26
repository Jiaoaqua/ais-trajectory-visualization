import json
import os
import uuid
import time
import threading
import paho.mqtt.client as mqtt

latest_vessels = {}

def save_to_json_loop(interval=3, filename="realtime_data/latest_vessels.json"):
    while True:
        try:
            with open(filename, "w") as f:
                json.dump(latest_vessels, f, indent=2)
            print(f"Saved {len(latest_vessels)} vessels to {filename}")
        except Exception as e:
            print(f"Error saving JSON: {e}")
        time.sleep(interval)


def on_message(client, userdata, msg):
    print("Received raw MQTT message.")
    print("Topic:", msg.topic)
    print("Payload:", msg.payload.decode("utf-8"))
    try:
        payload = json.loads(msg.payload.decode("utf-8"))
        if "position" in payload and "mmsi" in payload:
            pos = payload["position"]
            mmsi = str(payload["mmsi"])

            vessel_data = {
                "latitude": pos.get("latitude"),
                "longitude": pos.get("longitude"),
                "velocity": pos.get("speedOverGround"),
                "heading": pos.get("trueHeading"),
                "cog": pos.get("courseOverGround"),
                "vessel_name": payload.get("name", "Unknown")
            }

            if vessel_data["latitude"] and vessel_data["longitude"]:
                latest_vessels[mmsi] = vessel_data
                print(f"[📡] Got vessel: {mmsi}, {vessel_data}")
    except Exception as e:
        print(f"[❌] Error parsing message: {e}")


MQTT_BROKER = "meri.digitraffic.fi"
MQTT_PORT = 443
MQTT_TOPIC = "vessels-v2/positions/#"
APP_NAME = f"AIS_Listener_{uuid.uuid4()}"


client = mqtt.Client(client_id=APP_NAME, transport="websockets")
client.tls_set()
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT)
client.subscribe(MQTT_TOPIC)
print(f"Subscribed to topic: {MQTT_TOPIC}")
print("MQTT connected. Listening for real-time AIS data...")


threading.Thread(target=save_to_json_loop, daemon=True).start()
client.loop_forever()


