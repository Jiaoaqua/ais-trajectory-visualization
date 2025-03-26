# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CircleMarker(Component):
    """A CircleMarker component.
A circle of a fixed size with radius specified in pixels.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children [MUTABLE].

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- attribution (string; optional):
    String to be shown in the attribution control, e.g. \"©
    OpenStreetMap contributors\". It describes the layer data and is
    often a legal obligation towards copyright holders and tile
    providers. [MUTABLE].

- bubblingMouseEvents (boolean; optional):
    When True, a mouse event on this layer will trigger the same event
    on the map (unless L.DomEvent.stopPropagation is used).

- center (boolean | number | string | dict | list; required):
    A geographical point in (lat, lon) format. [MUTABLE].

- className (string; optional):
    Custom class name set on an element. Only for SVG renderer.

- clickData (dict; optional):
    An object holding data related to the click event. Typing is
    indicative.

    `clickData` is a dict with keys:

    - containerPoint (list of numbers; required)

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

- color (string; optional):
    Stroke color.

- dashArray (string; optional):
    A string that defines the stroke dash pattern. Doesn't work on
    Canvas-powered layers in some old browsers.

- dashOffset (string; optional):
    A string that defines the distance into the dash pattern to start
    the dash. Doesn't work on Canvas-powered layers in some old
    browsers.

- dblclickData (dict; optional):
    An object holding data related to the double click event. Typing
    is indicative.

    `dblclickData` is a dict with keys:

    - containerPoint (list of numbers; required)

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

- disableDefaultEventHandlers (boolean; optional):
    If set to True, default events handlers are not registered.
    [MUTABLE].

- eventHandlers (dict; optional):
    Object with keys specifying the event type and the value the
    corresponding event handlers. [MUTABLE].

- fill (boolean; optional):
    Whether to fill the path with color. Set it to False to disable
    filling on polygons or circles.

- fillColor (string; optional):
    Fill color. Defaults to the value of the color option.

- fillOpacity (number; optional):
    Fill opacity.

- fillRule (a value equal to: 'inherit', 'nonzero', 'evenodd'; optional):
    A string that defines how the inside of a shape is determined.

- interactive (boolean; optional):
    If False, the layer will not emit mouse events and will act as a
    part of the underlying map.

- lineCap (a value equal to: 'butt', 'round', 'square', 'inherit'; optional):
    A string that defines shape to be used at the end of the stroke.

- lineJoin (a value equal to: 'round', 'inherit', 'miter', 'bevel'; optional):
    A string that defines shape to be used at the corners of the
    stroke.

- loading_state (dict; optional):
    Dash loading state information.

- n_clicks (number; optional):
    An integer that represents the number of times that this element
    has been clicked on.

- n_dblclicks (number; optional):
    An integer that represents the number of times that this element
    has been double-clicked on.

- opacity (number; optional):
    Stroke opacity.

- pane (string; optional):
    Map pane where the layer will be added.

- pathOptions (dict; optional):
    Path options. Use this prop, if you want to modify path options
    through callbacks. [MUTABLE].

    `pathOptions` is a dict with keys:

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

- radius (number; required):
    Radius of the circle, in pixels.

- stroke (boolean; optional):
    Whether to draw stroke along the path. Set False to disable
    borders on polygons or circles.

- weight (number; optional):
    Stroke width in pixels."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'CircleMarker'
    @_explicitize_args
    def __init__(self, children=None, radius=Component.REQUIRED, stroke=Component.UNDEFINED, color=Component.UNDEFINED, weight=Component.UNDEFINED, opacity=Component.UNDEFINED, lineCap=Component.UNDEFINED, lineJoin=Component.UNDEFINED, dashArray=Component.UNDEFINED, dashOffset=Component.UNDEFINED, fill=Component.UNDEFINED, fillColor=Component.UNDEFINED, fillOpacity=Component.UNDEFINED, fillRule=Component.UNDEFINED, className=Component.UNDEFINED, interactive=Component.UNDEFINED, bubblingMouseEvents=Component.UNDEFINED, attribution=Component.UNDEFINED, pane=Component.UNDEFINED, center=Component.REQUIRED, pathOptions=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, eventHandlers=Component.UNDEFINED, disableDefaultEventHandlers=Component.UNDEFINED, n_clicks=Component.UNDEFINED, clickData=Component.UNDEFINED, n_dblclicks=Component.UNDEFINED, dblclickData=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'attribution', 'bubblingMouseEvents', 'center', 'className', 'clickData', 'color', 'dashArray', 'dashOffset', 'dblclickData', 'disableDefaultEventHandlers', 'eventHandlers', 'fill', 'fillColor', 'fillOpacity', 'fillRule', 'interactive', 'lineCap', 'lineJoin', 'loading_state', 'n_clicks', 'n_dblclicks', 'opacity', 'pane', 'pathOptions', 'radius', 'stroke', 'weight']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'attribution', 'bubblingMouseEvents', 'center', 'className', 'clickData', 'color', 'dashArray', 'dashOffset', 'dblclickData', 'disableDefaultEventHandlers', 'eventHandlers', 'fill', 'fillColor', 'fillOpacity', 'fillRule', 'interactive', 'lineCap', 'lineJoin', 'loading_state', 'n_clicks', 'n_dblclicks', 'opacity', 'pane', 'pathOptions', 'radius', 'stroke', 'weight']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['center', 'radius']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(CircleMarker, self).__init__(children=children, **args)
