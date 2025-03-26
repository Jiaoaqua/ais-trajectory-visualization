# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class EditControl(Component):
    """An EditControl component.
EditControl.ts is based on https://github.com/alex3165/react-leaflet-draw/

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- action (dict; optional):
    Fires on every action.

    `action` is a dict with keys:

    - layer_type (string; required)

    - n_actions (number; required)

    - type (string; required)

- disableDefaultEventHandlers (boolean; optional):
    If set to True, default events handlers are not registered.
    [MUTABLE].

- draw (dict; optional):
    Enable/disable draw controls. See example of usage here
    https://github.com/Leaflet/Leaflet.draw#user-content-example-leafletdraw-config.

- drawToolbar (dict; optional):
    Change this prop to manipulate the drawing toolbar, i.e. to change
    modes and/or invoke actions.

    `drawToolbar` is a dict with keys:

    - action (a value equal to: 'cancel', 'finish', 'delete last point'; required)

    - mode (a value equal to: 'marker', 'polygon', 'polyline', 'rectangle', 'circle', 'circlemarker'; required)

    - n_clicks (number; required)

- edit (dict; optional):
    Enable/disable edit controls. See example of usage here
    https://github.com/Leaflet/Leaflet.draw#user-content-example-leafletdraw-config.

- editToolbar (dict; optional):
    Change this prop to manipulate the edit toolbar, i.e. to change
    modes and/or invoke actions.

    `editToolbar` is a dict with keys:

    - action (a value equal to: 'cancel', 'save', 'clear all'; required)

    - mode (a value equal to: 'edit', 'remove'; required)

    - n_clicks (number; required)

- eventHandlers (dict; optional):
    Object with keys specifying the event type and the value the
    corresponding event handlers. [MUTABLE].

- geojson (dict; optional):
    Geojson representing the current features.

    `geojson` is a dict with keys:

    - features (list of dicts; required)

- loading_state (dict; optional):
    Dash loading state information.

- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional):
    Map control position."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'EditControl'
    @_explicitize_args
    def __init__(self, position=Component.UNDEFINED, draw=Component.UNDEFINED, edit=Component.UNDEFINED, action=Component.UNDEFINED, drawToolbar=Component.UNDEFINED, editToolbar=Component.UNDEFINED, geojson=Component.UNDEFINED, eventHandlers=Component.UNDEFINED, disableDefaultEventHandlers=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'action', 'disableDefaultEventHandlers', 'draw', 'drawToolbar', 'edit', 'editToolbar', 'eventHandlers', 'geojson', 'loading_state', 'position']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'action', 'disableDefaultEventHandlers', 'draw', 'drawToolbar', 'edit', 'editToolbar', 'eventHandlers', 'geojson', 'loading_state', 'position']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(EditControl, self).__init__(**args)
