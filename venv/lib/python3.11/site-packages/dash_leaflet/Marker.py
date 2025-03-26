# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Marker(Component):
    """A Marker component.
Marker is used to display clickable/draggable icons on the map. Extends Layer.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children [MUTABLE].

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- alt (string; optional):
    Text for the alt attribute of the icon image. Useful for
    accessibility.

- attribution (string; optional):
    String to be shown in the attribution control, e.g. \"©
    OpenStreetMap contributors\". It describes the layer data and is
    often a legal obligation towards copyright holders and tile
    providers. [MUTABLE].

- autoPan (boolean; optional):
    Whether to pan the map when dragging this marker near its edge or
    not.

- autoPanOnFocus (boolean; optional):
    When True, the map will pan whenever the marker is focused (via
    e.g. pressing tab on the keyboard) to ensure the marker is visible
    within the map's bounds.

- autoPanPadding (list of numbers; optional):
    Distance (in pixels to the left/right and to the top/bottom) of
    the map edge to start panning the map.

- autoPanSpeed (number; optional):
    Number of pixels the map should pan by.

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

- draggable (boolean; optional):
    Whether the marker is draggable with mouse/touch or not.
    [MUTABLE].

- eventHandlers (dict; optional):
    Object with keys specifying the event type and the value the
    corresponding event handlers. [MUTABLE].

- icon (dict; optional):
    Options passed to L.icon constructor. See
    https://leafletjs.com/reference.html#icon for details on how to
    customize the marker icon. [DL].

    `icon` is a dict with keys:

    - attribution (string; optional)

    - className (string; optional)

    - crossOrigin (boolean | number | string | dict | list; optional)

    - iconAnchor (boolean | number | string | dict | list; optional)

    - iconRetinaUrl (string; optional)

    - iconSize (boolean | number | string | dict | list; optional)

    - iconUrl (string; required)

    - pane (string; optional)

    - popupAnchor (boolean | number | string | dict | list; optional)

    - shadowAnchor (boolean | number | string | dict | list; optional)

    - shadowRetinaUrl (string; optional)

    - shadowSize (boolean | number | string | dict | list; optional)

    - shadowUrl (string; optional)

    - tooltipAnchor (boolean | number | string | dict | list; optional)

- interactive (boolean; optional):
    If False, the layer will not emit mouse events and will act as a
    part of the underlying map.

- keyboard (boolean; optional):
    Whether the marker can be tabbed to with a keyboard and clicked by
    pressing enter.

- loading_state (dict; optional):
    Dash loading state information.

- n_clicks (number; optional):
    An integer that represents the number of times that this element
    has been clicked on.

- n_dblclicks (number; optional):
    An integer that represents the number of times that this element
    has been double-clicked on.

- opacity (number; optional):
    The opacity of the marker. [MUTABLE].

- pane (string; optional):
    Map pane where the layer will be added.

- position (dict; required):
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

- riseOffset (number; optional):
    The z-index offset used for the riseOnHover feature.

- riseOnHover (boolean; optional):
    If True, the marker will get on top of others when you hover the
    mouse over it.

- shadowPane (string; optional):
    Map pane where the markers shadow will be added.

- title (string; optional):
    Text for the browser tooltip that appear on marker hover (no
    tooltip by default).

- zIndexOffset (number; optional):
    By default, marker images zIndex is set automatically based on its
    latitude. Use this option if you want to put the marker on top of
    all others (or below), specifying a high value like 1000 (or high
    negative value, respectively). [MUTABLE]."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'Marker'
    @_explicitize_args
    def __init__(self, children=None, position=Component.REQUIRED, opacity=Component.UNDEFINED, interactive=Component.UNDEFINED, bubblingMouseEvents=Component.UNDEFINED, attribution=Component.UNDEFINED, pane=Component.UNDEFINED, keyboard=Component.UNDEFINED, title=Component.UNDEFINED, alt=Component.UNDEFINED, zIndexOffset=Component.UNDEFINED, riseOnHover=Component.UNDEFINED, riseOffset=Component.UNDEFINED, shadowPane=Component.UNDEFINED, autoPanOnFocus=Component.UNDEFINED, draggable=Component.UNDEFINED, autoPan=Component.UNDEFINED, autoPanPadding=Component.UNDEFINED, autoPanSpeed=Component.UNDEFINED, icon=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, eventHandlers=Component.UNDEFINED, disableDefaultEventHandlers=Component.UNDEFINED, n_clicks=Component.UNDEFINED, clickData=Component.UNDEFINED, n_dblclicks=Component.UNDEFINED, dblclickData=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'alt', 'attribution', 'autoPan', 'autoPanOnFocus', 'autoPanPadding', 'autoPanSpeed', 'bubblingMouseEvents', 'clickData', 'dblclickData', 'disableDefaultEventHandlers', 'draggable', 'eventHandlers', 'icon', 'interactive', 'keyboard', 'loading_state', 'n_clicks', 'n_dblclicks', 'opacity', 'pane', 'position', 'riseOffset', 'riseOnHover', 'shadowPane', 'title', 'zIndexOffset']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'alt', 'attribution', 'autoPan', 'autoPanOnFocus', 'autoPanPadding', 'autoPanSpeed', 'bubblingMouseEvents', 'clickData', 'dblclickData', 'disableDefaultEventHandlers', 'draggable', 'eventHandlers', 'icon', 'interactive', 'keyboard', 'loading_state', 'n_clicks', 'n_dblclicks', 'opacity', 'pane', 'position', 'riseOffset', 'riseOnHover', 'shadowPane', 'title', 'zIndexOffset']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['position']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Marker, self).__init__(children=children, **args)
