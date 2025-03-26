# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SVGOverlay(Component):
    """A SVGOverlay component.
Used to load, display and provide DOM access to an SVG file over specific bounds of the map.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children [MUTABLE].

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- alt (string; optional):
    Text for the alt attribute of the image (useful for
    accessibility).

- attributes (dict with strings as keys and values of type string; required):
    The attributes must be valid SVGSVGElement properties.

- attribution (string; optional):
    String to be shown in the attribution control, e.g. \"©
    OpenStreetMap contributors\". It describes the layer data and is
    often a legal obligation towards copyright holders and tile
    providers. [MUTABLE].

- bounds (dict; required):
    The geographical bounds that the overlay is tied to. [MUTABLE].

    `bounds` is a dict with keys:

    - contains (required)

    - equals (required)

    - extend (required)

    - getCenter (required)

    - getEast (required)

    - getNorth (required)

    - getNorthEast (required)

    - getNorthWest (required)

    - getSouth (required)

    - getSouthEast (required)

    - getSouthWest (required)

    - getWest (required)

    - intersects (required)

    - isValid (required)

    - overlaps (required)

    - pad (required)

    - toBBoxString (required)

- bubblingMouseEvents (boolean; optional):
    When True, a mouse event on this layer will trigger the same event
    on the map (unless L.DomEvent.stopPropagation is used).

- className (string; optional):
    A custom class name to assign to the image. Empty by default.

- clickData (dict; optional):
    An object holding data related to the click event. Typing is
    indicative.

    `clickData` is a dict with keys:

    - containerPoint (list of numbers; required)

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

- crossOrigin (boolean | number | string | dict | list; optional):
    Whether the crossOrigin attribute will be added to the image. If a
    String is provided, the image will have its crossOrigin attribute
    set to the String provided. This is needed if you want to access
    image pixel data. Refer to CORS Settings for valid String values.

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

- errorOverlayUrl (string; optional):
    URL to the overlay image to show in place of the overlay that
    failed to load.

- eventHandlers (dict; optional):
    Object with keys specifying the event type and the value the
    corresponding event handlers. [MUTABLE].

- interactive (boolean; optional):
    If True, the image overlay will emit mouse events when clicked or
    hovered.

- loading_state (dict; optional):
    Dash loading state information.

- n_clicks (number; optional):
    An integer that represents the number of times that this element
    has been clicked on.

- n_dblclicks (number; optional):
    An integer that represents the number of times that this element
    has been double-clicked on.

- opacity (number; optional):
    The overlay opacity. [MUTABLE].

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

- zIndex (number; optional):
    The overlay zIndex. [MUTABLE]."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'SVGOverlay'
    @_explicitize_args
    def __init__(self, children=None, opacity=Component.UNDEFINED, className=Component.UNDEFINED, interactive=Component.UNDEFINED, bubblingMouseEvents=Component.UNDEFINED, attribution=Component.UNDEFINED, pane=Component.UNDEFINED, pathOptions=Component.UNDEFINED, alt=Component.UNDEFINED, crossOrigin=Component.UNDEFINED, errorOverlayUrl=Component.UNDEFINED, zIndex=Component.UNDEFINED, bounds=Component.REQUIRED, attributes=Component.REQUIRED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, eventHandlers=Component.UNDEFINED, disableDefaultEventHandlers=Component.UNDEFINED, n_clicks=Component.UNDEFINED, clickData=Component.UNDEFINED, n_dblclicks=Component.UNDEFINED, dblclickData=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'alt', 'attributes', 'attribution', 'bounds', 'bubblingMouseEvents', 'className', 'clickData', 'crossOrigin', 'dblclickData', 'disableDefaultEventHandlers', 'errorOverlayUrl', 'eventHandlers', 'interactive', 'loading_state', 'n_clicks', 'n_dblclicks', 'opacity', 'pane', 'pathOptions', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'alt', 'attributes', 'attribution', 'bounds', 'bubblingMouseEvents', 'className', 'clickData', 'crossOrigin', 'dblclickData', 'disableDefaultEventHandlers', 'errorOverlayUrl', 'eventHandlers', 'interactive', 'loading_state', 'n_clicks', 'n_dblclicks', 'opacity', 'pane', 'pathOptions', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['attributes', 'bounds']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(SVGOverlay, self).__init__(children=children, **args)
