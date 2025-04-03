import psycopg2

def connect_db():
    return psycopg2.connect(
        host="localhost",
        dbname="ais_data",
        user="group_3",
        password="12345678"
    )

import dash
from dash import dcc, html, Input, Output
import dash_leaflet as dl
import pandas as pd
import numpy as np
import math
import joblib
import os

# === Load Model ===
model = joblib.load("source_code/trajectory_rf_model.pkl")

# === Dash App Initialization ===
app = dash.Dash(__name__)
app.title = "Turku Vessel Real-Time Prediction"

# === Utility Functions ===
def calculate_arrow_points(lat, lon, heading, distance=0.02, arrow_width=0.007):
    angle_rad = math.radians(heading)
    end_lat = lat + distance * math.cos(angle_rad)
    end_lon = lon + distance * math.sin(angle_rad)
    left_angle = angle_rad + math.radians(150)
    right_angle = angle_rad - math.radians(150)
    left_lat = end_lat + arrow_width * math.cos(left_angle)
    left_lon = end_lon + arrow_width * math.sin(left_angle)
    right_lat = end_lat + arrow_width * math.cos(right_angle)
    right_lon = end_lon + arrow_width * math.cos(right_angle)
    return [[lat, lon], [end_lat, end_lon], [left_lat, left_lon], [right_lat, right_lon], [end_lat, end_lon]]

def get_latest_vessels():
    conn = connect_db()
    query = """
        SELECT DISTINCT ON (vessel_id)
            vessel_id, latitude, longitude, velocity AS sog, heading, cog,
            vessel_name, destination, type, timestamp
        FROM ais_vessel_turku
        WHERE latitude IS NOT NULL AND longitude IS NOT NULL
        ORDER BY vessel_id, timestamp DESC
        LIMIT 50;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def get_marker_icon(speed):
    if speed > 15:
        return "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png"
    elif speed > 5:
        return "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-orange.png"
    else:
        return "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-blue.png"

# === App Layout ===
app.layout = html.Div([
    html.H1("Turku Vessel Data Visualization (Real-time + Prediction)", style={"textAlign": "center"}),
    html.Div([
        dcc.Dropdown(id="vessel-type-dropdown", placeholder="Select Vessel", multi=True, style={"width": "250px"}),
        dcc.Interval(id="interval", interval=10*1000, n_intervals=0)
    ], style={"display": "flex", "gap": "15px", "marginBottom": "20px", "alignItems": "center"}),

    dl.Map(id="map", center=[60.44, 22.25], zoom=7, style={'height': '600px'}),

    html.Div([
        html.Div("🟥 >15 knots", style={"color": "red"}),
        html.Div("🟧 5–15 knots", style={"color": "orange"}),
        html.Div("🟦 <5 knots", style={"color": "blue"}),
        html.Div("🟢 Prediction (5min)", style={"color": "green"})
    ], style={
        "position": "absolute", "top": "10px", "right": "10px",
        "backgroundColor": "white", "padding": "10px", "borderRadius": "8px",
        "boxShadow": "0px 0px 5px rgba(0,0,0,0.3)", "zIndex": "999"
    })
])

# === Callback ===
@app.callback(
    Output("map", "children"),
    Output("vessel-type-dropdown", "options"),
    Input("interval", "n_intervals"),
    Input("vessel-type-dropdown", "value")
)
def update_map(n_intervals, selected_vessels):
    df = get_latest_vessels()

    if df.empty:
        return [dl.TileLayer()], []

    df["vessel_name"] = df["vessel_name"].fillna("Unknown")
    vessel_options = [{"label": name, "value": name} for name in df["vessel_name"].unique()]
    if selected_vessels:
        df = df[df["vessel_name"].isin(selected_vessels)]

    map_layers = [dl.TileLayer()]

    for _, row in df.iterrows():
        lat, lon = row["latitude"], row["longitude"]
        heading, cog, speed = row["heading"], row["cog"], row["sog"]
        name = row["vessel_name"]
        dest = row["destination"]
        vtype = row["type"]
        ts = row["timestamp"]

        marker = dl.Marker(
            position=[lat, lon],
            icon=dict(iconUrl=get_marker_icon(speed), iconSize=[25, 41], iconAnchor=[12, 41]),
            children=[
                dl.Tooltip(f"{name}"),
                dl.Popup(f"⛴️ {name}<br>🏁 {dest}<br>⚙️ Type: {vtype}<br>🕒 {ts}<br>🚀 Speed: {speed}")
            ]
        )

        arrow = dl.Polygon(
            positions=calculate_arrow_points(lat, lon, heading),
            color="darkred", fill=True, fillOpacity=0.9
        )

        try:
            if np.isnan(speed) or np.isnan(cog) or np.isnan(heading):
                raise ValueError("Missing speed / heading / cog, skipping prediction")

            pred_lat, pred_lon = model.predict([[lat, lon, speed, heading, cog]])[0]

            predicted_point = dl.Marker(
                position=[pred_lat, pred_lon],
                icon=dict(iconUrl="https://maps.gstatic.com/mapfiles/ms2/micons/green-dot.png"),
                children=dl.Popup(f"[Prediction] {name}")
            )

            direction_line = dl.Polyline(
                positions=[[lat, lon], [pred_lat, pred_lon]],
                color="darkred",
                weight=2,
                dashArray='6,4'
            )

            arrow_icon = dl.Marker(
                position=[pred_lat, pred_lon],
                icon=dict(
                    iconUrl="https://cdn-icons-png.flaticon.com/512/545/545682.png",
                    iconSize=[16, 16],
                    iconAnchor=[8, 8]
                )
            )

            map_layers.extend([marker, arrow, predicted_point, direction_line, arrow_icon])
        except Exception as e:
            print(f"[skip prediction] {name}: {e}")
            map_layers.extend([marker, arrow])

    return map_layers, vessel_options

# === Run App ===
if __name__ == '__main__':
    app.run_server(debug=True)

