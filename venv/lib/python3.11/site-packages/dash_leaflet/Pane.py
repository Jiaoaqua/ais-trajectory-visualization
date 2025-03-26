# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Pane(Component):
    """A Pane component.
Panes are DOM elements used to control the ordering of layers on the map.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children [MUTABLE].

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    CSS class(es).

- loading_state (dict; optional):
    Dash loading state information.

- name (string; required):
    The name must be unique to the pane and different from the default
    Leaflet pane names.

- pane (string; optional):
    Map pane where the layer will be added.

- style (dict; optional):
    Component style, e.g. { zIndex: 500 } to specify the pane zIndex."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'Pane'
    @_explicitize_args
    def __init__(self, children=None, name=Component.REQUIRED, className=Component.UNDEFINED, pane=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'loading_state', 'name', 'pane', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'loading_state', 'name', 'pane', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['name']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Pane, self).__init__(children=children, **args)
