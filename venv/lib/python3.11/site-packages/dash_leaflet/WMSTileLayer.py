# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class WMSTileLayer(Component):
    """A WMSTileLayer component.
Used to display WMS services as tile layers on the map.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- attribution (string; optional):
    String to be shown in the attribution control, e.g. \"©
    OpenStreetMap contributors\". It describes the layer data and is
    often a legal obligation towards copyright holders and tile
    providers.

- bounds (dict; optional):
    If set, tiles will only be loaded inside the set LatLngBounds.

    `bounds` is a dict with keys:

    - contains (required)

    - equals (required)

    - extend (required)

    - getCenter (required)

    - getEast (required)

    - getNorth (required)

    - getNorthEast (required)

    - getNorthWest (required)

    - getSouth (required)

    - getSouthEast (required)

    - getSouthWest (required)

    - getWest (required)

    - intersects (required)

    - isValid (required)

    - overlaps (required)

    - pad (required)

    - toBBoxString (required)

- className (string; optional):
    A custom class name to assign to the tile layer. Empty by default.

- crossOrigin (boolean | number | string | dict | list; optional):
    Whether the crossOrigin attribute will be added to the tiles. If a
    String is provided, all tiles will have their crossOrigin
    attribute set to the String provided. This is needed if you want
    to access tile pixel data. Refer to CORS Settings for valid String
    values.

- crs (string; optional):
    The Coordinate Reference System to use. Don't change this if
    you're not sure what it means. [DL].

- detectRetina (boolean; optional):
    If True and user is on a retina display, it will request four
    tiles of half the specified size and a bigger zoom level in place
    of one to utilize the high resolution.

- disableDefaultEventHandlers (boolean; optional):
    If set to True, default events handlers are not registered.
    [MUTABLE].

- errorTileUrl (string; optional):
    URL to the tile image to show in place of the tile that failed to
    load.

- eventHandlers (dict; optional):
    Object with keys specifying the event type and the value the
    corresponding event handlers. [MUTABLE].

- format (string; optional):
    WMS image format (use 'image/png' for layers with transparency).

- keepBuffer (number; optional):
    When panning the map, keep this many rows and columns of tiles
    before unloading them.

- layers (string; required):
    Comma-separated list of WMS layers to show.

- loading_state (dict; optional):
    Dash loading state information.

- maxNativeZoom (number; optional):
    Maximum zoom number the tile source has available. If it is
    specified, the tiles on all zoom levels higher than maxNativeZoom
    will be loaded from maxNativeZoom level and auto-scaled.

- maxZoom (number; optional):
    The maximum zoom level up to which this layer will be displayed
    (inclusive).

- minNativeZoom (number; optional):
    Minimum zoom number the tile source has available. If it is
    specified, the tiles on all zoom levels lower than minNativeZoom
    will be loaded from minNativeZoom level and auto-scaled.

- minZoom (number; optional):
    The minimum zoom level down to which this layer will be displayed
    (inclusive).

- n_loads (number; optional):
    An integer that represents the number of times that the load event
    has fired.

- noWrap (boolean; optional):
    Whether the layer is wrapped around the antimeridian. If True, the
    GridLayer will only be displayed once at low zoom levels. Has no
    effect when the map CRS doesn't wrap around. Can be used in
    combination with bounds to prevent requesting tiles outside the
    CRS limits.

- opacity (number; optional):
    The layer opacity. [MUTABLE].

- pane (string; optional):
    Map pane where the layer will be added.

- params (dict; optional):
    WMS parameters. [MUTABLE].

    `params` is a dict with keys:

    - format (string; optional)

    - height (number; optional)

    - layers (string; required)

    - request (string; optional)

    - service (string; optional)

    - styles (string; optional)

    - transparent (boolean; optional)

    - version (string; optional)

    - width (number; optional)

- referrerPolicy (boolean | number | string | dict | list; optional):
    Whether the referrerPolicy attribute will be added to the tiles.
    If a String is provided, all tiles will have their referrerPolicy
    attribute set to the String provided. This may be needed if your
    map's rendering context has a strict default but your tile
    provider expects a valid referrer (e.g. to validate an API token).
    Refer to HTMLImageElement.referrerPolicy for valid String values.

- styles (string; optional):
    Comma-separated list of WMS styles.

- subdomains (string | list of strings; optional):
    Subdomains of the tile service. Can be passed in the form of one
    string (where each letter is a subdomain name) or an array of
    strings.

- tileSize (number; optional):
    Width and height of tiles in the grid. Use a number if width and
    height are equal, or L.point(width, height) otherwise.

- tms (boolean; optional):
    If True, inverses Y axis numbering for tiles (turn this on for TMS
    services).

- transparent (boolean; optional):
    If True, the WMS service will return images with transparency.

- updateInterval (number; optional):
    Tiles will not update more than once every updateInterval
    milliseconds when panning.

- updateWhenIdle (boolean; optional):
    Load new tiles only when panning ends. True by default on mobile
    browsers, in order to avoid too many requests and keep smooth
    navigation. False otherwise in order to display new tiles during
    panning, since it is easy to pan outside the keepBuffer option in
    desktop browsers.

- updateWhenZooming (boolean; optional):
    By default, a smooth zoom animation (during a touch zoom or a
    flyTo()) will update grid layers every integer zoom level. Setting
    this option to False will update the grid layer only when the
    smooth animation ends.

- uppercase (boolean; optional):
    If True, WMS request parameter keys will be uppercase.

- url (string; required):
    The URL template.

- version (string; optional):
    Version of the WMS service to use.

- zIndex (number; optional):
    The layer zIndex. [MUTABLE].

- zoomOffset (number; optional):
    The zoom number used in tile URLs will be offset with this value.

- zoomReverse (boolean; optional):
    If set to True, the zoom number used in tile URLs will be reversed
    (maxZoom - zoom instead of zoom)."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'WMSTileLayer'
    @_explicitize_args
    def __init__(self, opacity=Component.UNDEFINED, className=Component.UNDEFINED, attribution=Component.UNDEFINED, pane=Component.UNDEFINED, url=Component.REQUIRED, format=Component.UNDEFINED, crossOrigin=Component.UNDEFINED, zIndex=Component.UNDEFINED, bounds=Component.UNDEFINED, minZoom=Component.UNDEFINED, maxZoom=Component.UNDEFINED, updateWhenIdle=Component.UNDEFINED, subdomains=Component.UNDEFINED, errorTileUrl=Component.UNDEFINED, zoomOffset=Component.UNDEFINED, tms=Component.UNDEFINED, zoomReverse=Component.UNDEFINED, detectRetina=Component.UNDEFINED, referrerPolicy=Component.UNDEFINED, tileSize=Component.UNDEFINED, updateWhenZooming=Component.UNDEFINED, updateInterval=Component.UNDEFINED, maxNativeZoom=Component.UNDEFINED, minNativeZoom=Component.UNDEFINED, noWrap=Component.UNDEFINED, keepBuffer=Component.UNDEFINED, layers=Component.REQUIRED, styles=Component.UNDEFINED, transparent=Component.UNDEFINED, version=Component.UNDEFINED, uppercase=Component.UNDEFINED, params=Component.UNDEFINED, crs=Component.UNDEFINED, id=Component.UNDEFINED, loading_state=Component.UNDEFINED, eventHandlers=Component.UNDEFINED, disableDefaultEventHandlers=Component.UNDEFINED, n_loads=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'attribution', 'bounds', 'className', 'crossOrigin', 'crs', 'detectRetina', 'disableDefaultEventHandlers', 'errorTileUrl', 'eventHandlers', 'format', 'keepBuffer', 'layers', 'loading_state', 'maxNativeZoom', 'maxZoom', 'minNativeZoom', 'minZoom', 'n_loads', 'noWrap', 'opacity', 'pane', 'params', 'referrerPolicy', 'styles', 'subdomains', 'tileSize', 'tms', 'transparent', 'updateInterval', 'updateWhenIdle', 'updateWhenZooming', 'uppercase', 'url', 'version', 'zIndex', 'zoomOffset', 'zoomReverse']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'attribution', 'bounds', 'className', 'crossOrigin', 'crs', 'detectRetina', 'disableDefaultEventHandlers', 'errorTileUrl', 'eventHandlers', 'format', 'keepBuffer', 'layers', 'loading_state', 'maxNativeZoom', 'maxZoom', 'minNativeZoom', 'minZoom', 'n_loads', 'noWrap', 'opacity', 'pane', 'params', 'referrerPolicy', 'styles', 'subdomains', 'tileSize', 'tms', 'transparent', 'updateInterval', 'updateWhenIdle', 'updateWhenZooming', 'uppercase', 'url', 'version', 'zIndex', 'zoomOffset', 'zoomReverse']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['layers', 'url']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(WMSTileLayer, self).__init__(**args)
