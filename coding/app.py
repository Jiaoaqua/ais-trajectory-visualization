import dash
from dash import dcc, html, Input, Output
import dash_leaflet as dl
import plotly.express as px
import pandas as pd
import math

# Load and preprocess data
df = pd.read_csv("coding/ais_vessel_data.csv", dtype={"destination": str}, low_memory=False)
df = df.head(15000)
df = df.dropna(subset=["latitude", "longitude", "cog"])  # make sure there is a cog
df["cog"] = pd.to_numeric(df["cog"], errors="coerce")  

df = df.head(15000)
df = df.dropna(subset=["latitude", "longitude"])

vessel_types = df["vessel_name"].unique()
destinations = df["destination"].dropna().unique()

app = dash.Dash(__name__)

speed_options = [
    {"label": "All Speeds", "value": "all"},
    {"label": "Low Speed (≤ 5 knots)", "value": "low"},
    {"label": "Medium Speed (5 - 15 knots)", "value": "medium"},
    {"label": "High Speed (> 15 knots)", "value": "high"}
]

def get_marker_icon(speed):
    if speed > 15:
        return "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png"
    elif speed > 5:
        return "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-orange.png"
    else:
        return "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-blue.png"

def predict_trajectory(lat, lon, cog, speed, minutes=5):
    points = [[lat, lon]]
    earth_radius_nm = 3440
    for i in range(1, minutes + 1):
        distance = speed * i / 60
        angle_rad = math.radians(float(cog))
        delta_lat = (distance / earth_radius_nm) * math.cos(angle_rad)
        delta_lon = (distance / (earth_radius_nm * math.cos(math.radians(lat)))) * math.sin(angle_rad)
        new_lat = lat + delta_lat
        new_lon = lon + delta_lon
        points.append([new_lat, new_lon])
    return points

def calculate_arrow_points(lat, lon, heading, distance=0.02, arrow_width=0.007):
    angle_rad = math.radians(heading)
    end_lat = lat + distance * math.cos(angle_rad)
    end_lon = lon + distance * math.sin(angle_rad)
    left_angle = angle_rad + math.radians(150)
    right_angle = angle_rad - math.radians(150)
    left_lat = end_lat + arrow_width * math.cos(left_angle)
    left_lon = end_lon + arrow_width * math.sin(left_angle)
    right_lat = end_lat + arrow_width * math.cos(right_angle)
    right_lon = end_lon + arrow_width * math.sin(right_angle)
    return [[lat, lon], [end_lat, end_lon], [left_lat, left_lon], [right_lat, right_lon], [end_lat, end_lon]]

app.layout = html.Div([
    html.H1("Turku Vessel Data Visualization"),
    html.Div([
        dcc.Dropdown(id="vessel-type-dropdown",
                     options=[{"label": v, "value": v} for v in vessel_types],
                     placeholder="Select Vessel Type", multi=True,
                     style={"width": "250px", "fontSize": "16px"}),
        dcc.Dropdown(id="speed-dropdown",
                     options=speed_options, value="all",
                     style={"width": "200px", "fontSize": "16px"}),
        dcc.Dropdown(id="destination-dropdown",
                     options=[{"label": d, "value": d} for d in destinations],
                     placeholder="Select Destination", multi=True,
                     style={"width": "250px", "fontSize": "16px"})
    ], style={"display": "flex", "gap": "15px", "marginBottom": "20px", "alignItems": "center"}),
    dl.Map(id="map", center=[60.17, 24.94], zoom=7, style={'height': '500px'}),
    dcc.Graph(id="speed-histogram")
])

@app.callback(
    Output("map", "children"),
    [Input("vessel-type-dropdown", "value"),
     Input("speed-dropdown", "value"),
     Input("destination-dropdown", "value")]
)
def update_map(selected_types, selected_speed, selected_destinations):
    filtered_df = df
    if selected_types:
        filtered_df = filtered_df[filtered_df["vessel_name"].isin(selected_types)]
    if selected_speed == "low":
        filtered_df = filtered_df[filtered_df["velocity"] <= 5]
    elif selected_speed == "medium":
        filtered_df = filtered_df[(filtered_df["velocity"] > 5) & (filtered_df["velocity"] <= 15)]
    elif selected_speed == "high":
        filtered_df = filtered_df[filtered_df["velocity"] > 15]
    if selected_destinations:
        filtered_df = filtered_df[filtered_df["destination"].isin(selected_destinations)]

    map_layers = [dl.TileLayer()]
    for _, row in filtered_df.iterrows():
        marker = dl.Marker(
            position=[row["latitude"], row["longitude"]],
            icon=dict(iconUrl=get_marker_icon(row["velocity"]), iconSize=[25, 41], iconAnchor=[12, 41]),
            children=dl.Popup(f"{row['vessel_name']}<br>Speed: {row['velocity']} knots<br>Heading: {row['heading']}")
        )
        arrow = dl.Polygon(
            positions=calculate_arrow_points(row["latitude"], row["longitude"], row["heading"]),
            color="darkred", fill=True, fillOpacity=0.8
        )
        if not pd.isna(row["cog"]) and not pd.isna(row["velocity"]):
            trajectory = dl.Polyline(
                positions=predict_trajectory(row["latitude"], row["longitude"], row["cog"], row["velocity"]),
                color="black", weight=4, opacity=1
            )
            map_layers.append(trajectory)
        map_layers.extend([marker, arrow])
    return map_layers

@app.callback(
    Output("speed-histogram", "figure"),
    [Input("vessel-type-dropdown", "value"),
     Input("speed-dropdown", "value"),
     Input("destination-dropdown", "value")]
)
def update_speed_histogram(selected_types, selected_speed, selected_destinations):
    filtered_df = df
    if selected_types:
        filtered_df = filtered_df[filtered_df["vessel_name"].isin(selected_types)]
    if selected_speed == "low":
        filtered_df = filtered_df[filtered_df["velocity"] <= 5]
    elif selected_speed == "medium":
        filtered_df = filtered_df[(filtered_df["velocity"] > 5) & (filtered_df["velocity"] <= 15)]
    elif selected_speed == "high":
        filtered_df = filtered_df[filtered_df["velocity"] > 15]
    if selected_destinations:
        filtered_df = filtered_df[filtered_df["destination"].isin(selected_destinations)]
    return px.histogram(filtered_df, x="velocity", nbins=20, title="Filtered Vessel Speed Distribution")

if __name__ == '__main__':
    app.run_server(debug=True)

