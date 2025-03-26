# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FeatureGroup(Component):
    """A FeatureGroup component.
A class for drawing FeatureGroup overlays on a map.

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

- clickData (dict; optional):
    An object holding data related to the click event. Typing is
    indicative.

    `clickData` is a dict with keys:

    - containerPoint (list of numbers; required)

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

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

- interactive (boolean; optional):
    If False, the layer will not emit mouse events and will act as a
    part of the underlying map.

- loading_state (dict; optional):
    Dash loading state information.

- n_clicks (number; optional):
    An integer that represents the number of times that this element
    has been clicked on.

- n_dblclicks (number; optional):
    An integer that represents the number of times that this element
    has been double-clicked on.

- pane (string; optional):
    Map pane where the layer will be added."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'FeatureGroup'
    @_explicitize_args
    def __init__(self, children=None, interactive=Component.UNDEFINED, bubblingMouseEvents=Component.UNDEFINED, attribution=Component.UNDEFINED, pane=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, eventHandlers=Component.UNDEFINED, disableDefaultEventHandlers=Component.UNDEFINED, n_clicks=Component.UNDEFINED, clickData=Component.UNDEFINED, n_dblclicks=Component.UNDEFINED, dblclickData=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'attribution', 'bubblingMouseEvents', 'clickData', 'dblclickData', 'disableDefaultEventHandlers', 'eventHandlers', 'interactive', 'loading_state', 'n_clicks', 'n_dblclicks', 'pane']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'attribution', 'bubblingMouseEvents', 'clickData', 'dblclickData', 'disableDefaultEventHandlers', 'eventHandlers', 'interactive', 'loading_state', 'n_clicks', 'n_dblclicks', 'pane']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FeatureGroup, self).__init__(children=children, **args)
