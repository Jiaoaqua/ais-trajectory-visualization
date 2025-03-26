# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FullScreenControl(Component):
    """A FullScreenControl component.
A basic FullScreen control with two buttons (FullScreen in and FullScreen out). It is put on the map by default unless you set its FullScreenControl option to false.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- content (string; optional):
    Content of the button, can be HTML, default 'None'.

- forcePseudoFullscreen (boolean; optional):
    Force use of pseudo full screen even if full screen API is
    available, default 'False'.

- forceSeparateButton (boolean; optional):
    Force separate button to detach from zoom buttons, default
    'False'.

- fullscreenElement (boolean | number | string | dict | list; optional):
    Dom element to render in full screen, False by default, fallback
    to 'map._container'.

- loading_state (dict; optional):
    Dash loading state information.

- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional):
    Map control position.

- title (string; optional):
    Title of the button, default 'Full Screen'.

- titleCancel (string; optional):
    Title of the button when fullscreen is on, default 'Exit Full
    Screen'."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'FullScreenControl'
    @_explicitize_args
    def __init__(self, position=Component.UNDEFINED, title=Component.UNDEFINED, content=Component.UNDEFINED, titleCancel=Component.UNDEFINED, forceSeparateButton=Component.UNDEFINED, forcePseudoFullscreen=Component.UNDEFINED, fullscreenElement=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'content', 'forcePseudoFullscreen', 'forceSeparateButton', 'fullscreenElement', 'loading_state', 'position', 'title', 'titleCancel']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'content', 'forcePseudoFullscreen', 'forceSeparateButton', 'fullscreenElement', 'loading_state', 'position', 'title', 'titleCancel']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FullScreenControl, self).__init__(**args)
