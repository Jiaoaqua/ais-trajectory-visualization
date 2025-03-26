# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class LayersControl(Component):
    """A LayersControl component.
The layers control gives users the ability to switch between different base layers and switch overlays on/off.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children [MUTABLE].

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- autoZIndex (boolean; optional):
    If True, the control will assign zIndexes in increasing order to
    all of its layers so that the order is preserved when switching
    them on/off.

- baseLayer (string; optional):
    Name of the currently selected base layer. [DL].

- collapsed (boolean; optional):
    If True, the control will be collapsed into an icon and expanded
    on mouse hover, touch, or keyboard activation. [MUTABLE].

- hideSingleBase (boolean; optional):
    If True, the base layers in the control will be hidden when there
    is only one.

- loading_state (dict; optional):
    Dash loading state information.

- overlays (list of strings; optional):
    Names of the currently selected overlays. [DL].

- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional):
    Map control position. [MUTABLE].

- sortLayers (boolean; optional):
    Whether to sort the layers. When False, layers will keep the order
    in which they were added to the control."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'LayersControl'
    @_explicitize_args
    def __init__(self, children=None, position=Component.UNDEFINED, collapsed=Component.UNDEFINED, autoZIndex=Component.UNDEFINED, hideSingleBase=Component.UNDEFINED, sortLayers=Component.UNDEFINED, baseLayer=Component.UNDEFINED, overlays=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'autoZIndex', 'baseLayer', 'collapsed', 'hideSingleBase', 'loading_state', 'overlays', 'position', 'sortLayers']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'autoZIndex', 'baseLayer', 'collapsed', 'hideSingleBase', 'loading_state', 'overlays', 'position', 'sortLayers']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(LayersControl, self).__init__(children=children, **args)
