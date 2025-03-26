# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ScaleControl(Component):
    """A ScaleControl component.
A simple scale control that shows the scale of the current center of screen in metric (m/km) and imperial (mi/ft) systems.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- imperial (boolean; optional):
    Whether to show the imperial scale line (mi/ft).

- loading_state (dict; optional):
    Dash loading state information.

- maxWidth (number; optional):
    Maximum width of the control in pixels. The width is set
    dynamically to show round values (e.g. 100, 200, 500).

- metric (boolean; optional):
    Whether to show the metric scale line (m/km).

- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional):
    Map control position. [MUTABLE].

- updateWhenIdle (boolean; optional):
    If True, the control is updated on moveend, otherwise it's always
    up-to-date (updated on move)."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'ScaleControl'
    @_explicitize_args
    def __init__(self, position=Component.UNDEFINED, metric=Component.UNDEFINED, maxWidth=Component.UNDEFINED, imperial=Component.UNDEFINED, updateWhenIdle=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'imperial', 'loading_state', 'maxWidth', 'metric', 'position', 'updateWhenIdle']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'imperial', 'loading_state', 'maxWidth', 'metric', 'position', 'updateWhenIdle']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ScaleControl, self).__init__(**args)
