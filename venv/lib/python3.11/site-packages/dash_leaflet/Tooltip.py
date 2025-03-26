# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Tooltip(Component):
    """A Tooltip component.
Used to display small texts on top of map layers.

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

- className (string; optional):
    A custom CSS class name to assign to the overlay.

- clickData (dict; optional):
    An object holding data related to the click event. Typing is
    indicative.

    `clickData` is a dict with keys:

    - containerPoint (list of numbers; required)

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

- content (string; optional):
    Sets the HTML content of the overlay while initializing. If a
    function is passed the source layer will be passed to the
    function. The function should return a String or HTMLElement to be
    used in the overlay.

- dblclickData (dict; optional):
    An object holding data related to the double click event. Typing
    is indicative.

    `dblclickData` is a dict with keys:

    - containerPoint (list of numbers; required)

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

- direction (a value equal to: 'center', 'right', 'left', 'top', 'bottom', 'auto'; optional):
    Direction where to open the tooltip. Possible values are: right,
    left, top, bottom, center, auto. auto will dynamically switch
    between right and left according to the tooltip position on the
    map.

- disableDefaultEventHandlers (boolean; optional):
    If set to True, default events handlers are not registered.
    [MUTABLE].

- eventHandlers (dict; optional):
    Object with keys specifying the event type and the value the
    corresponding event handlers. [MUTABLE].

- interactive (boolean; optional):
    If True, the popup/tooltip will listen to the mouse events.

- loading_state (dict; optional):
    Dash loading state information.

- n_clicks (number; optional):
    An integer that represents the number of times that this element
    has been clicked on.

- n_dblclicks (number; optional):
    An integer that represents the number of times that this element
    has been double-clicked on.

- offset (dict; optional):
    The offset of the popup position.

    `offset` is a dict with keys:

    - add (required)

    - ceil (required)

    - clone (required)

    - contains (required)

    - distanceTo (required)

    - divideBy (required)

    - equals (required)

    - floor (required)

    - multiplyBy (required)

    - round (required)

    - scaleBy (required)

    - subtract (required)

    - toString (optional)

    - trunc (required)

    - unscaleBy (required)

    - x (number; required)

    - y (number; required)

- opacity (number; optional):
    Tooltip container opacity.

- pane (string; optional):
    Map pane where the layer will be added.

- permanent (boolean; optional):
    Whether to open the tooltip permanently or only on mouseover.

- position (dict; optional):
    A geographical point in (lat, lon) format. [MUTABLE].

    `position` is a dict with keys:

    - alt (number; optional)

    - clone (required)

    - distanceTo (required)

    - equals (required)

    - lat (number; required)

    - lng (number; required)

    - toBounds (required)

    - toString (optional)

    - wrap (required)

- sticky (boolean; optional):
    If True, the tooltip will follow the mouse instead of being fixed
    at the feature center."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'Tooltip'
    @_explicitize_args
    def __init__(self, children=None, position=Component.UNDEFINED, opacity=Component.UNDEFINED, className=Component.UNDEFINED, interactive=Component.UNDEFINED, bubblingMouseEvents=Component.UNDEFINED, attribution=Component.UNDEFINED, pane=Component.UNDEFINED, content=Component.UNDEFINED, offset=Component.UNDEFINED, direction=Component.UNDEFINED, permanent=Component.UNDEFINED, sticky=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, eventHandlers=Component.UNDEFINED, disableDefaultEventHandlers=Component.UNDEFINED, n_clicks=Component.UNDEFINED, clickData=Component.UNDEFINED, n_dblclicks=Component.UNDEFINED, dblclickData=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'attribution', 'bubblingMouseEvents', 'className', 'clickData', 'content', 'dblclickData', 'direction', 'disableDefaultEventHandlers', 'eventHandlers', 'interactive', 'loading_state', 'n_clicks', 'n_dblclicks', 'offset', 'opacity', 'pane', 'permanent', 'position', 'sticky']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'attribution', 'bubblingMouseEvents', 'className', 'clickData', 'content', 'dblclickData', 'direction', 'disableDefaultEventHandlers', 'eventHandlers', 'interactive', 'loading_state', 'n_clicks', 'n_dblclicks', 'offset', 'opacity', 'pane', 'permanent', 'position', 'sticky']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Tooltip, self).__init__(children=children, **args)
