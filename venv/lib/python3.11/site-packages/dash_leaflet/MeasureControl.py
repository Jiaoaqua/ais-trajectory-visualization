# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MeasureControl(Component):
    """A MeasureControl component.
Coordinate, linear, and area measure control for Leaflet maps.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- activeColor (string; optional):
    The color to use for map features rendered while actively
    performing a measurement.

- captureZIndex (number; optional):
    The Z-index of the marker used to capture measure clicks.

- completedColor (string; optional):
    The color to use for features generated from a completed
    measurement.

- decPoint (string; optional):
    The decimal point separator used when displaying measurements.

- loading_state (dict; optional):
    Dash loading state information.

- popupOptions (dict; optional):
    The options applied to the popup of the resulting measure feature.

    `popupOptions` is a dict with keys:

    - autoClose (boolean; optional)

    - autoPan (boolean; optional)

    - autoPanPadding (boolean | number | string | dict | list; optional)

    - autoPanPaddingBottomRight (boolean | number | string | dict | list; optional)

    - autoPanPaddingTopLeft (boolean | number | string | dict | list; optional)

    - className (string; optional)

    - closeButton (boolean; optional)

    - closeOnClick (boolean; optional)

    - closeOnEscapeKey (boolean; optional)

    - content (string; optional)

    - interactive (boolean; optional)

    - keepInView (boolean; optional)

    - maxHeight (number; optional)

    - maxWidth (number; optional)

    - minWidth (number; optional)

    - offset (boolean | number | string | dict | list; optional)

    - pane (string; optional)

- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional):
    Map control position.

- primaryAreaUnit (string; optional):
    The primary units used to display area results.

- primaryLengthUnit (string; optional):
    The primary units used to display length results.

- secondaryAreaUnit (string; optional):
    The secondary units used to display area results.

- secondaryLengthUnit (string; optional):
    The secondary units used to display length results.

- thousandsSep (string; optional):
    The thousands separator used when displaying measurements.

- units (dict; optional):
    Custom units to make available to the measurement calculator.
    Packaged units are feet, meters, miles, and kilometers for length
    and acres, hectares, sqfeet, sqmeters, and sqmiles for areas.
    Additional unit definitions can be added to the packaged units
    using this option.

    `units` is a dict with keys:

    - string (dict; required)

        `string` is a dict with keys:

        - decimals (number; required)

        - display (string; required)

        - factor (number; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'MeasureControl'
    @_explicitize_args
    def __init__(self, position=Component.UNDEFINED, primaryLengthUnit=Component.UNDEFINED, secondaryLengthUnit=Component.UNDEFINED, primaryAreaUnit=Component.UNDEFINED, secondaryAreaUnit=Component.UNDEFINED, activeColor=Component.UNDEFINED, completedColor=Component.UNDEFINED, popupOptions=Component.UNDEFINED, units=Component.UNDEFINED, captureZIndex=Component.UNDEFINED, decPoint=Component.UNDEFINED, thousandsSep=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'activeColor', 'captureZIndex', 'completedColor', 'decPoint', 'loading_state', 'popupOptions', 'position', 'primaryAreaUnit', 'primaryLengthUnit', 'secondaryAreaUnit', 'secondaryLengthUnit', 'thousandsSep', 'units']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'activeColor', 'captureZIndex', 'completedColor', 'decPoint', 'loading_state', 'popupOptions', 'position', 'primaryAreaUnit', 'primaryLengthUnit', 'secondaryAreaUnit', 'secondaryLengthUnit', 'thousandsSep', 'units']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MeasureControl, self).__init__(**args)
