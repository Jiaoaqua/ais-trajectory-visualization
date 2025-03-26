# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Popup(Component):
    """A Popup component.
Used to open popups in certain places of the map.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children [MUTABLE].

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- attribution (string; optional):
    String to be shown in the attribution control, e.g. \"©
    OpenStreetMap contributors\". It describes the layer data and is
    often a legal obligation towards copyright holders and tile
    providers. [MUTABLE].

- autoClose (boolean; optional):
    Set it to False if you want to override the default behavior of
    the popup closing when another popup is opened.

- autoPan (boolean; optional):
    Set it to False if you don't want the map to do panning animation
    to fit the opened popup.

- autoPanPadding (dict; optional):
    Equivalent of setting both top left and bottom right autopan
    padding to the same value.

    `autoPanPadding` is a dict with keys:

    - add (required)

    - ceil (required)

    - clone (required)

    - contains (required)

    - distanceTo (required)

    - divideBy (required)

    - equals (required)

    - floor (required)

    - multiplyBy (required)

    - round (required)

    - scaleBy (required)

    - subtract (required)

    - toString (optional)

    - trunc (required)

    - unscaleBy (required)

    - x (number; required)

    - y (number; required)

- autoPanPaddingBottomRight (dict; optional):
    The margin between the popup and the bottom right corner of the
    map view after autopanning was performed.

    `autoPanPaddingBottomRight` is a dict with keys:

    - add (required)

    - ceil (required)

    - clone (required)

    - contains (required)

    - distanceTo (required)

    - divideBy (required)

    - equals (required)

    - floor (required)

    - multiplyBy (required)

    - round (required)

    - scaleBy (required)

    - subtract (required)

    - toString (optional)

    - trunc (required)

    - unscaleBy (required)

    - x (number; required)

    - y (number; required)

- autoPanPaddingTopLeft (dict; optional):
    The margin between the popup and the top left corner of the map
    view after autopanning was performed.

    `autoPanPaddingTopLeft` is a dict with keys:

    - add (required)

    - ceil (required)

    - clone (required)

    - contains (required)

    - distanceTo (required)

    - divideBy (required)

    - equals (required)

    - floor (required)

    - multiplyBy (required)

    - round (required)

    - scaleBy (required)

    - subtract (required)

    - toString (optional)

    - trunc (required)

    - unscaleBy (required)

    - x (number; required)

    - y (number; required)

- bubblingMouseEvents (boolean; optional):
    When True, a mouse event on this layer will trigger the same event
    on the map (unless L.DomEvent.stopPropagation is used).

- className (string; optional):
    A custom CSS class name to assign to the popup.

- clickData (dict; optional):
    An object holding data related to the click event. Typing is
    indicative.

    `clickData` is a dict with keys:

    - containerPoint (list of numbers; required)

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

- closeButton (boolean; optional):
    Controls the presence of a close button in the popup.

- closeOnClick (boolean; optional):
    Set it if you want to override the default behavior of the popup
    closing when user clicks on the map. Defaults to the map's
    closePopupOnClick option.

- closeOnEscapeKey (boolean; optional):
    Set it to False if you want to override the default behavior of
    the ESC key for closing of the popup.

- content (string; optional):
    Sets the HTML content of the overlay while initializing. If a
    function is passed the source layer will be passed to the
    function. The function should return a String or HTMLElement to be
    used in the overlay.

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

- interactive (boolean; optional):
    If True, the popup/tooltip will listen to the mouse events.

- keepInView (boolean; optional):
    Set it to True if you want to prevent users from panning the popup
    off of the screen while it is open.

- loading_state (dict; optional):
    Dash loading state information.

- maxHeight (number; optional):
    If set, creates a scrollable container of the given height inside
    a popup if its content exceeds it. The scrollable container can be
    styled using the leaflet-popup-scrolled CSS class selector.

- maxWidth (number; optional):
    Max width of the popup, in pixels.

- minWidth (number; optional):
    Min width of the popup, in pixels.

- n_clicks (number; optional):
    An integer that represents the number of times that this element
    has been clicked on.

- n_dblclicks (number; optional):
    An integer that represents the number of times that this element
    has been double-clicked on.

- offset (dict; optional):
    The offset of the popup position.

    `offset` is a dict with keys:

    - add (required)

    - ceil (required)

    - clone (required)

    - contains (required)

    - distanceTo (required)

    - divideBy (required)

    - equals (required)

    - floor (required)

    - multiplyBy (required)

    - round (required)

    - scaleBy (required)

    - subtract (required)

    - toString (optional)

    - trunc (required)

    - unscaleBy (required)

    - x (number; required)

    - y (number; required)

- pane (string; optional):
    Map pane where the layer will be added.

- position (dict; optional):
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

    - wrap (required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'Popup'
    @_explicitize_args
    def __init__(self, children=None, position=Component.UNDEFINED, className=Component.UNDEFINED, interactive=Component.UNDEFINED, bubblingMouseEvents=Component.UNDEFINED, attribution=Component.UNDEFINED, pane=Component.UNDEFINED, autoPan=Component.UNDEFINED, autoPanPadding=Component.UNDEFINED, content=Component.UNDEFINED, offset=Component.UNDEFINED, maxWidth=Component.UNDEFINED, minWidth=Component.UNDEFINED, maxHeight=Component.UNDEFINED, autoPanPaddingTopLeft=Component.UNDEFINED, autoPanPaddingBottomRight=Component.UNDEFINED, keepInView=Component.UNDEFINED, closeButton=Component.UNDEFINED, autoClose=Component.UNDEFINED, closeOnEscapeKey=Component.UNDEFINED, closeOnClick=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, eventHandlers=Component.UNDEFINED, disableDefaultEventHandlers=Component.UNDEFINED, n_clicks=Component.UNDEFINED, clickData=Component.UNDEFINED, n_dblclicks=Component.UNDEFINED, dblclickData=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'attribution', 'autoClose', 'autoPan', 'autoPanPadding', 'autoPanPaddingBottomRight', 'autoPanPaddingTopLeft', 'bubblingMouseEvents', 'className', 'clickData', 'closeButton', 'closeOnClick', 'closeOnEscapeKey', 'content', 'dblclickData', 'disableDefaultEventHandlers', 'eventHandlers', 'interactive', 'keepInView', 'loading_state', 'maxHeight', 'maxWidth', 'minWidth', 'n_clicks', 'n_dblclicks', 'offset', 'pane', 'position']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'attribution', 'autoClose', 'autoPan', 'autoPanPadding', 'autoPanPaddingBottomRight', 'autoPanPaddingTopLeft', 'bubblingMouseEvents', 'className', 'clickData', 'closeButton', 'closeOnClick', 'closeOnEscapeKey', 'content', 'dblclickData', 'disableDefaultEventHandlers', 'eventHandlers', 'interactive', 'keepInView', 'loading_state', 'maxHeight', 'maxWidth', 'minWidth', 'n_clicks', 'n_dblclicks', 'offset', 'pane', 'position']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Popup, self).__init__(children=children, **args)
