# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class LocateControl(Component):
    """A LocateControl component.
A useful control to geolocate the user with many options. Official Leaflet and MapBox plugin.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- cacheLocation (boolean; optional):
    Keep a cache of the location after the user deactivates the
    control. If set to False, the user has to wait until the locate
    API returns a new location before they see where they are again.

- circlePadding (list of numbers; optional):
    Padding around the accuracy circle.

- circleStyle (dict; optional):
    Accuracy circle style properties.

    `circleStyle` is a dict with keys:

    - attribution (string; optional):
        String to be shown in the attribution control, e.g. \"©
        OpenStreetMap contributors\". It describes the layer data and
        is often a legal obligation towards copyright holders and tile
        providers.

    - bubblingMouseEvents (boolean; optional):
        When True, a mouse event on this layer will trigger the same
        event on the map (unless L.DomEvent.stopPropagation is used).

    - className (string; optional):
        Custom class name set on an element. Only for SVG renderer.

    - color (string; optional):
        Stroke color.

    - dashArray (string; optional):
        A string that defines the stroke dash pattern. Doesn't work on
        Canvas-powered layers in some old browsers.

    - dashOffset (string; optional):
        A string that defines the distance into the dash pattern to
        start the dash. Doesn't work on Canvas-powered layers in some
        old browsers.

    - fill (boolean; optional):
        Whether to fill the path with color. Set it to False to
        disable filling on polygons or circles.

    - fillColor (string; optional):
        Fill color. Defaults to the value of the color option.

    - fillOpacity (number; optional):
        Fill opacity.

    - fillRule (a value equal to: 'inherit', 'nonzero', 'evenodd'; optional):
        A string that defines how the inside of a shape is determined.

    - interactive (boolean; optional):
        If False, the layer will not emit mouse events and will act as
        a part of the underlying map.

    - lineCap (a value equal to: 'butt', 'round', 'square', 'inherit'; optional):
        A string that defines shape to be used at the end of the
        stroke.

    - lineJoin (a value equal to: 'round', 'inherit', 'miter', 'bevel'; optional):
        A string that defines shape to be used at the corners of the
        stroke.

    - opacity (number; optional):
        Stroke opacity.

    - pane (string; optional):
        Map pane where the layer will be added.

    - stroke (boolean; optional):
        Whether to draw stroke along the path. Set False to disable
        borders on polygons or circles.

    - weight (number; optional):
        Stroke width in pixels.

- clickBehavior (dict; optional):
    What to do when the user clicks on the control. Has three options
    inView, inViewNotFollowing and outOfView. Possible values are stop
    and setView, or the name of a behaviour to inherit from.

- compassStyle (dict; optional):
    Triangle compass heading marker style properties. Only works if
    your marker class supports setStyle.

    `compassStyle` is a dict with keys:

    - attribution (string; optional):
        String to be shown in the attribution control, e.g. \"©
        OpenStreetMap contributors\". It describes the layer data and
        is often a legal obligation towards copyright holders and tile
        providers.

    - bubblingMouseEvents (boolean; optional):
        When True, a mouse event on this layer will trigger the same
        event on the map (unless L.DomEvent.stopPropagation is used).

    - className (string; optional):
        Custom class name set on an element. Only for SVG renderer.

    - color (string; optional):
        Stroke color.

    - dashArray (string; optional):
        A string that defines the stroke dash pattern. Doesn't work on
        Canvas-powered layers in some old browsers.

    - dashOffset (string; optional):
        A string that defines the distance into the dash pattern to
        start the dash. Doesn't work on Canvas-powered layers in some
        old browsers.

    - fill (boolean; optional):
        Whether to fill the path with color. Set it to False to
        disable filling on polygons or circles.

    - fillColor (string; optional):
        Fill color. Defaults to the value of the color option.

    - fillOpacity (number; optional):
        Fill opacity.

    - fillRule (a value equal to: 'inherit', 'nonzero', 'evenodd'; optional):
        A string that defines how the inside of a shape is determined.

    - interactive (boolean; optional):
        If False, the layer will not emit mouse events and will act as
        a part of the underlying map.

    - lineCap (a value equal to: 'butt', 'round', 'square', 'inherit'; optional):
        A string that defines shape to be used at the end of the
        stroke.

    - lineJoin (a value equal to: 'round', 'inherit', 'miter', 'bevel'; optional):
        A string that defines shape to be used at the corners of the
        stroke.

    - opacity (number; optional):
        Stroke opacity.

    - pane (string; optional):
        Map pane where the layer will be added.

    - stroke (boolean; optional):
        Whether to draw stroke along the path. Set False to disable
        borders on polygons or circles.

    - weight (number; optional):
        Stroke width in pixels.

- drawCircle (boolean; optional):
    If set, a circle that shows the location accuracy is drawn.

- drawMarker (boolean; optional):
    If set, the marker at the users' location is drawn.

- flyTo (boolean; optional):
    Smooth pan and zoom to the location of the marker. Only works in
    Leaflet 1.0+.

- followCircleStyle (dict; optional):
    Changes to the accuracy circle while following. Only need to
    provide changes.

    `followCircleStyle` is a dict with keys:

    - attribution (string; optional):
        String to be shown in the attribution control, e.g. \"©
        OpenStreetMap contributors\". It describes the layer data and
        is often a legal obligation towards copyright holders and tile
        providers.

    - bubblingMouseEvents (boolean; optional):
        When True, a mouse event on this layer will trigger the same
        event on the map (unless L.DomEvent.stopPropagation is used).

    - className (string; optional):
        Custom class name set on an element. Only for SVG renderer.

    - color (string; optional):
        Stroke color.

    - dashArray (string; optional):
        A string that defines the stroke dash pattern. Doesn't work on
        Canvas-powered layers in some old browsers.

    - dashOffset (string; optional):
        A string that defines the distance into the dash pattern to
        start the dash. Doesn't work on Canvas-powered layers in some
        old browsers.

    - fill (boolean; optional):
        Whether to fill the path with color. Set it to False to
        disable filling on polygons or circles.

    - fillColor (string; optional):
        Fill color. Defaults to the value of the color option.

    - fillOpacity (number; optional):
        Fill opacity.

    - fillRule (a value equal to: 'inherit', 'nonzero', 'evenodd'; optional):
        A string that defines how the inside of a shape is determined.

    - interactive (boolean; optional):
        If False, the layer will not emit mouse events and will act as
        a part of the underlying map.

    - lineCap (a value equal to: 'butt', 'round', 'square', 'inherit'; optional):
        A string that defines shape to be used at the end of the
        stroke.

    - lineJoin (a value equal to: 'round', 'inherit', 'miter', 'bevel'; optional):
        A string that defines shape to be used at the corners of the
        stroke.

    - opacity (number; optional):
        Stroke opacity.

    - pane (string; optional):
        Map pane where the layer will be added.

    - stroke (boolean; optional):
        Whether to draw stroke along the path. Set False to disable
        borders on polygons or circles.

    - weight (number; optional):
        Stroke width in pixels.

- followCompassStyle (dict; optional):
    Changes to the compass marker while following. Only need to
    provide changes.

    `followCompassStyle` is a dict with keys:

    - attribution (string; optional):
        String to be shown in the attribution control, e.g. \"©
        OpenStreetMap contributors\". It describes the layer data and
        is often a legal obligation towards copyright holders and tile
        providers.

    - bubblingMouseEvents (boolean; optional):
        When True, a mouse event on this layer will trigger the same
        event on the map (unless L.DomEvent.stopPropagation is used).

    - className (string; optional):
        Custom class name set on an element. Only for SVG renderer.

    - color (string; optional):
        Stroke color.

    - dashArray (string; optional):
        A string that defines the stroke dash pattern. Doesn't work on
        Canvas-powered layers in some old browsers.

    - dashOffset (string; optional):
        A string that defines the distance into the dash pattern to
        start the dash. Doesn't work on Canvas-powered layers in some
        old browsers.

    - fill (boolean; optional):
        Whether to fill the path with color. Set it to False to
        disable filling on polygons or circles.

    - fillColor (string; optional):
        Fill color. Defaults to the value of the color option.

    - fillOpacity (number; optional):
        Fill opacity.

    - fillRule (a value equal to: 'inherit', 'nonzero', 'evenodd'; optional):
        A string that defines how the inside of a shape is determined.

    - interactive (boolean; optional):
        If False, the layer will not emit mouse events and will act as
        a part of the underlying map.

    - lineCap (a value equal to: 'butt', 'round', 'square', 'inherit'; optional):
        A string that defines shape to be used at the end of the
        stroke.

    - lineJoin (a value equal to: 'round', 'inherit', 'miter', 'bevel'; optional):
        A string that defines shape to be used at the corners of the
        stroke.

    - opacity (number; optional):
        Stroke opacity.

    - pane (string; optional):
        Map pane where the layer will be added.

    - stroke (boolean; optional):
        Whether to draw stroke along the path. Set False to disable
        borders on polygons or circles.

    - weight (number; optional):
        Stroke width in pixels.

- followMarkerStyle (dict; optional):
    Changes to the inner marker while following. Only need to provide
    changes.

    `followMarkerStyle` is a dict with keys:

    - attribution (string; optional):
        String to be shown in the attribution control, e.g. \"©
        OpenStreetMap contributors\". It describes the layer data and
        is often a legal obligation towards copyright holders and tile
        providers.

    - bubblingMouseEvents (boolean; optional):
        When True, a mouse event on this layer will trigger the same
        event on the map (unless L.DomEvent.stopPropagation is used).

    - className (string; optional):
        Custom class name set on an element. Only for SVG renderer.

    - color (string; optional):
        Stroke color.

    - dashArray (string; optional):
        A string that defines the stroke dash pattern. Doesn't work on
        Canvas-powered layers in some old browsers.

    - dashOffset (string; optional):
        A string that defines the distance into the dash pattern to
        start the dash. Doesn't work on Canvas-powered layers in some
        old browsers.

    - fill (boolean; optional):
        Whether to fill the path with color. Set it to False to
        disable filling on polygons or circles.

    - fillColor (string; optional):
        Fill color. Defaults to the value of the color option.

    - fillOpacity (number; optional):
        Fill opacity.

    - fillRule (a value equal to: 'inherit', 'nonzero', 'evenodd'; optional):
        A string that defines how the inside of a shape is determined.

    - interactive (boolean; optional):
        If False, the layer will not emit mouse events and will act as
        a part of the underlying map.

    - lineCap (a value equal to: 'butt', 'round', 'square', 'inherit'; optional):
        A string that defines shape to be used at the end of the
        stroke.

    - lineJoin (a value equal to: 'round', 'inherit', 'miter', 'bevel'; optional):
        A string that defines shape to be used at the corners of the
        stroke.

    - opacity (number; optional):
        Stroke opacity.

    - pane (string; optional):
        Map pane where the layer will be added.

    - stroke (boolean; optional):
        Whether to draw stroke along the path. Set False to disable
        borders on polygons or circles.

    - weight (number; optional):
        Stroke width in pixels.

- icon (string; optional):
    The CSS class for the icon.

- iconElementTag (string; optional):
    The element to be created for icons.

- iconLoading (string; optional):
    The CSS class for the icon while loading.

- initialZoomLevel (number; optional):
    After activating the plugin by clicking on the icon, zoom to the
    selected zoom level, even when keepCurrentZoomLevel is True. Set
    to False to disable this feature.

- keepCurrentZoomLevel (boolean; optional):
    Only pan when setting the view.

- loading_state (dict; optional):
    Dash loading state information.

- locateOptions (dict; optional):
    The default options passed to leaflets locate method.

    `locateOptions` is a dict with keys:

    - enableHighAccuracy (boolean; optional)

    - maxZoom (number; optional)

    - maximumAge (number; optional)

    - setView (boolean; optional)

    - timeout (number; optional)

    - watch (boolean; optional)

- markerStyle (dict; optional):
    Inner marker style properties. Only works if your marker class
    supports setStyle.

    `markerStyle` is a dict with keys:

    - attribution (string; optional):
        String to be shown in the attribution control, e.g. \"©
        OpenStreetMap contributors\". It describes the layer data and
        is often a legal obligation towards copyright holders and tile
        providers.

    - bubblingMouseEvents (boolean; optional):
        When True, a mouse event on this layer will trigger the same
        event on the map (unless L.DomEvent.stopPropagation is used).

    - className (string; optional):
        Custom class name set on an element. Only for SVG renderer.

    - color (string; optional):
        Stroke color.

    - dashArray (string; optional):
        A string that defines the stroke dash pattern. Doesn't work on
        Canvas-powered layers in some old browsers.

    - dashOffset (string; optional):
        A string that defines the distance into the dash pattern to
        start the dash. Doesn't work on Canvas-powered layers in some
        old browsers.

    - fill (boolean; optional):
        Whether to fill the path with color. Set it to False to
        disable filling on polygons or circles.

    - fillColor (string; optional):
        Fill color. Defaults to the value of the color option.

    - fillOpacity (number; optional):
        Fill opacity.

    - fillRule (a value equal to: 'inherit', 'nonzero', 'evenodd'; optional):
        A string that defines how the inside of a shape is determined.

    - interactive (boolean; optional):
        If False, the layer will not emit mouse events and will act as
        a part of the underlying map.

    - lineCap (a value equal to: 'butt', 'round', 'square', 'inherit'; optional):
        A string that defines shape to be used at the end of the
        stroke.

    - lineJoin (a value equal to: 'round', 'inherit', 'miter', 'bevel'; optional):
        A string that defines shape to be used at the corners of the
        stroke.

    - opacity (number; optional):
        Stroke opacity.

    - pane (string; optional):
        Map pane where the layer will be added.

    - stroke (boolean; optional):
        Whether to draw stroke along the path. Set False to disable
        borders on polygons or circles.

    - weight (number; optional):
        Stroke width in pixels.

- metric (boolean; optional):
    Use metric units.

- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional):
    Map control position.

- returnToPrevBounds (boolean; optional):
    If set, save the map bounds just before centering to the user's
    location. When control is disabled, set the view back to the
    bounds that were saved.

- setView (boolean | number | string | dict | list; optional):
    Set the map view (zoom and pan) to the user's location as it
    updates.

- showCompass (boolean; optional):
    Show the compass bearing on top of the location marker.

- showPopup (boolean; optional):
    Display a pop-up when the user click on the inner marker.

- strings (dict; optional):
    Strings used in the control. Options are title, text, metersUnit,
    feetUnit, popup and outsideMapBoundsMsg.

    `strings` is a dict with keys:

    - feetUnit (string; optional)

    - metersUnit (string; optional)

    - outsideMapBoundsMsg (string; optional)

    - popup (string; optional)

    - title (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'LocateControl'
    @_explicitize_args
    def __init__(self, position=Component.UNDEFINED, icon=Component.UNDEFINED, setView=Component.UNDEFINED, flyTo=Component.UNDEFINED, keepCurrentZoomLevel=Component.UNDEFINED, initialZoomLevel=Component.UNDEFINED, clickBehavior=Component.UNDEFINED, returnToPrevBounds=Component.UNDEFINED, cacheLocation=Component.UNDEFINED, showCompass=Component.UNDEFINED, drawCircle=Component.UNDEFINED, drawMarker=Component.UNDEFINED, circleStyle=Component.UNDEFINED, markerStyle=Component.UNDEFINED, compassStyle=Component.UNDEFINED, followCircleStyle=Component.UNDEFINED, followMarkerStyle=Component.UNDEFINED, followCompassStyle=Component.UNDEFINED, iconLoading=Component.UNDEFINED, iconElementTag=Component.UNDEFINED, circlePadding=Component.UNDEFINED, metric=Component.UNDEFINED, showPopup=Component.UNDEFINED, strings=Component.UNDEFINED, locateOptions=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'cacheLocation', 'circlePadding', 'circleStyle', 'clickBehavior', 'compassStyle', 'drawCircle', 'drawMarker', 'flyTo', 'followCircleStyle', 'followCompassStyle', 'followMarkerStyle', 'icon', 'iconElementTag', 'iconLoading', 'initialZoomLevel', 'keepCurrentZoomLevel', 'loading_state', 'locateOptions', 'markerStyle', 'metric', 'position', 'returnToPrevBounds', 'setView', 'showCompass', 'showPopup', 'strings']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'cacheLocation', 'circlePadding', 'circleStyle', 'clickBehavior', 'compassStyle', 'drawCircle', 'drawMarker', 'flyTo', 'followCircleStyle', 'followCompassStyle', 'followMarkerStyle', 'icon', 'iconElementTag', 'iconLoading', 'initialZoomLevel', 'keepCurrentZoomLevel', 'loading_state', 'locateOptions', 'markerStyle', 'metric', 'position', 'returnToPrevBounds', 'setView', 'showCompass', 'showPopup', 'strings']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(LocateControl, self).__init__(**args)
