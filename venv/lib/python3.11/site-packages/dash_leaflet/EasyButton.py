# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class EasyButton(Component):
    """An EasyButton component.
The easiest way to add buttons with Leaflet.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

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

- icon (string; required):
    The icon to show, e.g. 'fa-globe' from
    \"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css\".

- loading_state (dict; optional):
    Dash loading state information.

- n_clicks (number; optional):
    An integer that represents the number of times that this element
    has been clicked on.

- n_dblclicks (number; optional):
    An integer that represents the number of times that this element
    has been double-clicked on.

- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional):
    Map control position.

- title (string; optional):
    Title on the button."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'EasyButton'
    @_explicitize_args
    def __init__(self, position=Component.UNDEFINED, title=Component.UNDEFINED, icon=Component.REQUIRED, n_clicks=Component.UNDEFINED, clickData=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, eventHandlers=Component.UNDEFINED, disableDefaultEventHandlers=Component.UNDEFINED, n_dblclicks=Component.UNDEFINED, dblclickData=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'clickData', 'dblclickData', 'disableDefaultEventHandlers', 'eventHandlers', 'icon', 'loading_state', 'n_clicks', 'n_dblclicks', 'position', 'title']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'clickData', 'dblclickData', 'disableDefaultEventHandlers', 'eventHandlers', 'icon', 'loading_state', 'n_clicks', 'n_dblclicks', 'position', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['icon']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(EasyButton, self).__init__(**args)
