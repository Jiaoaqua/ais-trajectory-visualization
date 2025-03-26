# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Overlay(Component):
    """An Overlay component.
Overlay is a wrapper of LayersControl.Overlay in react-leaflet. It takes similar properties to its react-leaflet counterpart.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children [MUTABLE].

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- checked (boolean; optional):
    If True, the layer is shown, otherwise it's hidden. [MUTABLE].

- loading_state (dict; optional):
    Dash loading state information.

- name (boolean; required):
    Name of the layer, used for the label in the LayersControl."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'Overlay'
    @_explicitize_args
    def __init__(self, children=None, name=Component.REQUIRED, checked=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'checked', 'loading_state', 'name']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'checked', 'loading_state', 'name']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['name']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Overlay, self).__init__(children=children, **args)
