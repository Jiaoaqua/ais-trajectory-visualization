# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Colorbar(Component):
    """A Colorbar component.
Color bar control component for Leaflet. Most of the functionality is
delegated to chroma-js (see the docs for that module). For creating your
own color schemes for maps, have a look at http://colorbrewer2.org.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    Any CSS classes to appy.

- classes (number | list of numbers; optional):
    The number or positions of discrete classes in the colorbar. If
    not set the colorbar will be continuous, which is the default.

- colorscale (string | list of strings; optional):
    Chroma-js colorscale. Either a colorscale name, e.g. \"Viridis\",
    or a list of colors, e.g. [\"black\", \"#fdd49e\",
    \"rgba(255,0,0,0.35)\"]. The predefined colorscales are listed
    here:
    https://github.com/gka/chroma.js/blob/master/src/colors/colorbrewer.js.

- height (number; optional):
    Height in pixels.

- loading_state (dict; optional):
    Dash loading state information.

- max (number; optional):
    Domain maximum of the colorbar. Translates to the last color of
    the colorscale.

- min (number; optional):
    Domain minimum of the colorbar. Translates to the first color of
    the colorscale.

- nTicks (number; optional):
    Number of ticks on the colorbar.

- opacity (number; optional):
    Opacity of the colorbar. Use it to match the perceived colors from
    an overlay with opacity.

- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional):
    Map control position.

- style (dict; optional):
    HTML style object to add to the colorbar entity, e.g. to set font
    color.

- tickDecimals (number; optional):
    If set, fixes the tick decimal points to the given number.

- tickText (list of numbers; optional):
    If set, this text will be used instead of the data values.

- tickValues (list of numbers; optional):
    If set, these values are used for ticks (rather than the ones
    genrated based on nTicks).

- tooltip (boolean; optional):
    If True, the value will be shown as tooltip on hover.

- unit (string; optional):
    Optional text to append to the colorbar ticks.

- width (number; optional):
    Width in pixels."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'Colorbar'
    @_explicitize_args
    def __init__(self, position=Component.UNDEFINED, opacity=Component.UNDEFINED, className=Component.UNDEFINED, colorscale=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, min=Component.UNDEFINED, max=Component.UNDEFINED, classes=Component.UNDEFINED, unit=Component.UNDEFINED, nTicks=Component.UNDEFINED, tickDecimals=Component.UNDEFINED, tickValues=Component.UNDEFINED, tickText=Component.UNDEFINED, tooltip=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'classes', 'colorscale', 'height', 'loading_state', 'max', 'min', 'nTicks', 'opacity', 'position', 'style', 'tickDecimals', 'tickText', 'tickValues', 'tooltip', 'unit', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'classes', 'colorscale', 'height', 'loading_state', 'max', 'min', 'nTicks', 'opacity', 'position', 'style', 'tickDecimals', 'tickText', 'tickValues', 'tooltip', 'unit', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Colorbar, self).__init__(**args)
