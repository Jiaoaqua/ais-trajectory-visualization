import dash
from dash import dcc, html, Input, Output
import dash_leaflet as dl
import plotly.express as px
import pandas as pd
import math

# load data
df = pd.read_csv("coding/ais_vessel_data.csv", dtype={"cog": str, "destination": str}, low_memory=False)
df = df.head(15000)  #limit the data amout, koska with all the data the website can report failure
df = df.dropna(subset=["latitude", "longitude"])  # fliter no existing data

# list the vessel type and destinations
vessel_types = df["vessel_name"].unique()
destinations = df["destination"].dropna().unique()

# initialize the app
app = dash.Dash(__name__)

# classify the speed options
speed_options = [
    {"label": "All Speeds", "value": "all"},
    {"label": "Low Speed (≤ 5 knots)", "value": "low"},
    {"label": "Medium Speed (5 - 15 knots)", "value": "medium"},
    {"label": "High Speed (> 15 knots)", "value": "high"}
]

def get_marker_icon(speed):
    """ return different color url according to the speed """
    if speed > 15:
        return "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png"
    elif speed > 5:
        return "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-orange.png"
    else:
        return "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-blue.png"

app.layout = html.Div([
    html.H1("Turku Vessel Data Visualization"),

    # audience selection dropdown boxes
    html.Div([
        dcc.Dropdown(
            id="vessel-type-dropdown",
            options=[{"label": v, "value": v} for v in vessel_types],
            placeholder="Select Vessel Type",
            multi=True,
            style={"width": "250px", "fontSize": "16px"}  
        ),
        dcc.Dropdown(
            id="speed-dropdown",
            options=speed_options,
            value="all",
            style={"width": "200px", "fontSize": "16px"}  
        ),
        dcc.Dropdown(
            id="destination-dropdown",
            options=[{"label": d, "value": d} for d in destinations],
            placeholder="Select Destination",
            multi=True,
            style={"width": "250px", "fontSize": "16px"}  
        )
    ], style={"display": "flex", "gap": "15px", "marginBottom": "20px", "alignItems": "center"}),  

    # show the map
    dl.Map(id="map", center=[60.17, 24.94], zoom=7, style={'height': '500px'}),

    # the histogram of the speed distribution
    dcc.Graph(id="speed-histogram")
])


# calculate the angle of the direction
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

# update the map
@app.callback(
    Output("map", "children"),
    [Input("vessel-type-dropdown", "value"),
     Input("speed-dropdown", "value"),
     Input("destination-dropdown", "value")]
)
def update_map(selected_types, selected_speed, selected_destinations):
    filtered_df = df

    # filter the vessel type
    if selected_types:
        filtered_df = filtered_df[filtered_df["vessel_name"].isin(selected_types)]

    # filter the vessel speed
    if selected_speed == "low":
        filtered_df = filtered_df[filtered_df["velocity"] <= 5]
    elif selected_speed == "medium":
        filtered_df = filtered_df[(filtered_df["velocity"] > 5) & (filtered_df["velocity"] <= 15)]
    elif selected_speed == "high":
        filtered_df = filtered_df[filtered_df["velocity"] > 15]

    # filter the destination
    if selected_destinations:
        filtered_df = filtered_df[filtered_df["destination"].isin(selected_destinations)]

    # generate the map mark
    map_layers = [dl.TileLayer()]
    for _, row in filtered_df.iterrows():
        start_pos = [row["latitude"], row["longitude"]]
        arrow_points = calculate_arrow_points(row["latitude"], row["longitude"], row["heading"])

        marker = dl.Marker(
            position=[row["latitude"], row["longitude"]],
            icon=dict(iconUrl=get_marker_icon(row["velocity"]), iconSize=[25, 41], iconAnchor=[12, 41]),  # 设置自定义图标
            children=dl.Popup(f"{row['vessel_name']} - Speed: {row['velocity']} knots")
        )

        arrow = dl.Polygon(
            positions=arrow_points,
            color="darkred",
            fill=True,
            fillOpacity=0.8
        )

        map_layers.append(marker)
        map_layers.append(arrow)

    return map_layers

# update the speed histogram
@app.callback(
    Output("speed-histogram", "figure"),
    [Input("vessel-type-dropdown", "value"),
     Input("speed-dropdown", "value"),
     Input("destination-dropdown", "value")]
)
def update_speed_histogram(selected_types, selected_speed, selected_destinations):
    filtered_df = df

    # filter the vessel type
    if selected_types:
        filtered_df = filtered_df[filtered_df["vessel_name"].isin(selected_types)]

    # filter the speed
    if selected_speed == "low":
        filtered_df = filtered_df[filtered_df["velocity"] <= 5]
    elif selected_speed == "medium":
        filtered_df = filtered_df[(filtered_df["velocity"] > 5) & (filtered_df["velocity"] <= 15)]
    elif selected_speed == "high":
        filtered_df = filtered_df[filtered_df["velocity"] > 15]

    # filter the destination
    if selected_destinations:
        filtered_df = filtered_df[filtered_df["destination"].isin(selected_destinations)]

    # draw the histogram of speed distribution
    fig = px.histogram(filtered_df, x="velocity", nbins=20, title="Filtered Vessel Speed Distribution")
    return fig

# run the dash 
if __name__ == '__main__':
    app.run_server(debug=True)
