from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Funnel(_BaseTraceType):
    # class properties
    # --------------------
    _parent_path_str = ""
    _path_str = "funnel"
    _valid_props = {
        "alignmentgroup",
        "cliponaxis",
        "connector",
        "constraintext",
        "customdata",
        "customdatasrc",
        "dx",
        "dy",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hovertemplate",
        "hovertemplatesrc",
        "hovertext",
        "hovertextsrc",
        "ids",
        "idssrc",
        "insidetextanchor",
        "insidetextfont",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "marker",
        "meta",
        "metasrc",
        "name",
        "offset",
        "offsetgroup",
        "opacity",
        "orientation",
        "outsidetextfont",
        "selectedpoints",
        "showlegend",
        "stream",
        "text",
        "textangle",
        "textfont",
        "textinfo",
        "textposition",
        "textpositionsrc",
        "textsrc",
        "texttemplate",
        "texttemplatesrc",
        "type",
        "uid",
        "uirevision",
        "visible",
        "width",
        "x",
        "x0",
        "xaxis",
        "xhoverformat",
        "xperiod",
        "xperiod0",
        "xperiodalignment",
        "xsrc",
        "y",
        "y0",
        "yaxis",
        "yhoverformat",
        "yperiod",
        "yperiod0",
        "yperiodalignment",
        "ysrc",
    }

    # alignmentgroup
    # --------------
    @property
    def alignmentgroup(self):
        """
        Set several traces linked to the same position axis or matching
        axes to the same alignmentgroup. This controls whether bars
        compute their positional range dependently or independently.

        The 'alignmentgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["alignmentgroup"]

    @alignmentgroup.setter
    def alignmentgroup(self, val):
        self["alignmentgroup"] = val

    # cliponaxis
    # ----------
    @property
    def cliponaxis(self):
        """
        Determines whether the text nodes are clipped about the subplot
        axes. To show the text nodes above axis lines and tick labels,
        make sure to set `xaxis.layer` and `yaxis.layer` to *below
        traces*.

        The 'cliponaxis' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["cliponaxis"]

    @cliponaxis.setter
    def cliponaxis(self, val):
        self["cliponaxis"] = val

    # connector
    # ---------
    @property
    def connector(self):
        """
        The 'connector' property is an instance of Connector
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.funnel.Connector`
          - A dict of string/value properties that will be passed
            to the Connector constructor

            Supported dict properties:

                fillcolor
                    Sets the fill color.
                line
                    :class:`plotly.graph_objects.funnel.connector.L
                    ine` instance or dict with compatible
                    properties
                visible
                    Determines if connector regions and lines are
                    drawn.

        Returns
        -------
        plotly.graph_objs.funnel.Connector
        """
        return self["connector"]

    @connector.setter
    def connector(self, val):
        self["connector"] = val

    # constraintext
    # -------------
    @property
    def constraintext(self):
        """
        Constrain the size of text inside or outside a bar to be no
        larger than the bar itself.

        The 'constraintext' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['inside', 'outside', 'both', 'none']

        Returns
        -------
        Any
        """
        return self["constraintext"]

    @constraintext.setter
    def constraintext(self, val):
        self["constraintext"] = val

    # customdata
    # ----------
    @property
    def customdata(self):
        """
        Assigns extra data each datum. This may be useful when
        listening to hover, click and selection events. Note that,
        "scatter" traces also appends customdata items in the markers
        DOM elements

        The 'customdata' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["customdata"]

    @customdata.setter
    def customdata(self, val):
        self["customdata"] = val

    # customdatasrc
    # -------------
    @property
    def customdatasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `customdata`.

        The 'customdatasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["customdatasrc"]

    @customdatasrc.setter
    def customdatasrc(self, val):
        self["customdatasrc"] = val

    # dx
    # --
    @property
    def dx(self):
        """
        Sets the x coordinate step. See `x0` for more info.

        The 'dx' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["dx"]

    @dx.setter
    def dx(self, val):
        self["dx"] = val

    # dy
    # --
    @property
    def dy(self):
        """
        Sets the y coordinate step. See `y0` for more info.

        The 'dy' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["dy"]

    @dy.setter
    def dy(self, val):
        self["dy"] = val

    # hoverinfo
    # ---------
    @property
    def hoverinfo(self):
        """
        Determines which trace information appear on hover. If `none`
        or `skip` are set, no information is displayed upon hovering.
        But, if `none` is set, click and hover events are still fired.

        The 'hoverinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['name', 'x', 'y', 'text', 'percent initial', 'percent previous', 'percent total'] joined with '+' characters
            (e.g. 'name+x')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')
          - A list or array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["hoverinfo"]

    @hoverinfo.setter
    def hoverinfo(self, val):
        self["hoverinfo"] = val

    # hoverinfosrc
    # ------------
    @property
    def hoverinfosrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hoverinfo`.

        The 'hoverinfosrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["hoverinfosrc"]

    @hoverinfosrc.setter
    def hoverinfosrc(self, val):
        self["hoverinfosrc"] = val

    # hoverlabel
    # ----------
    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.funnel.Hoverlabel`
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor

            Supported dict properties:

                align
                    Sets the horizontal alignment of the text
                    content within hover label box. Has an effect
                    only if the hover label text spans more two or
                    more lines
                alignsrc
                    Sets the source reference on Chart Studio Cloud
                    for `align`.
                bgcolor
                    Sets the background color of the hover labels
                    for this trace
                bgcolorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `bgcolor`.
                bordercolor
                    Sets the border color of the hover labels for
                    this trace.
                bordercolorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `bordercolor`.
                font
                    Sets the font used in hover labels.
                namelength
                    Sets the default length (in number of
                    characters) of the trace name in the hover
                    labels for all traces. -1 shows the whole name
                    regardless of length. 0-3 shows the first 0-3
                    characters, and an integer >3 will show the
                    whole name if it is less than that many
                    characters, but if it is longer, will truncate
                    to `namelength - 3` characters and add an
                    ellipsis.
                namelengthsrc
                    Sets the source reference on Chart Studio Cloud
                    for `namelength`.

        Returns
        -------
        plotly.graph_objs.funnel.Hoverlabel
        """
        return self["hoverlabel"]

    @hoverlabel.setter
    def hoverlabel(self, val):
        self["hoverlabel"] = val

    # hovertemplate
    # -------------
    @property
    def hovertemplate(self):
        """
        Template string used for rendering the information that appear
        on hover box. Note that this will override `hoverinfo`.
        Variables are inserted using %{variable}, for example "y: %{y}"
        as well as %{xother}, {%_xother}, {%_xother_}, {%xother_}. When
        showing info for several points, "xother" will be added to
        those with different x positions from the first point. An
        underscore before or after "(x|y)other" will add a space on
        that side, only when this field is shown. Numbers are formatted
        using d3-format's syntax %{variable:d3-format}, for example
        "Price: %{y:$.2f}".
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format for
        details on the formatting syntax. Dates are formatted using
        d3-time-format's syntax %{variable|d3-time-format}, for example
        "Day: %{2019-01-01|%A}". https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format for details on the date
        formatting syntax. The variables available in `hovertemplate`
        are the ones emitted as event data described at this link
        https://plotly.com/javascript/plotlyjs-events/#event-data.
        Additionally, every attributes that can be specified per-point
        (the ones that are `arrayOk: true`) are available. Finally, the
        template string has access to variables `percentInitial`,
        `percentPrevious` and `percentTotal`. Anything contained in tag
        `<extra>` is displayed in the secondary box, for example
        "<extra>{fullData.name}</extra>". To hide the secondary box
        completely, use an empty tag `<extra></extra>`.

        The 'hovertemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["hovertemplate"]

    @hovertemplate.setter
    def hovertemplate(self, val):
        self["hovertemplate"] = val

    # hovertemplatesrc
    # ----------------
    @property
    def hovertemplatesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hovertemplate`.

        The 'hovertemplatesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["hovertemplatesrc"]

    @hovertemplatesrc.setter
    def hovertemplatesrc(self, val):
        self["hovertemplatesrc"] = val

    # hovertext
    # ---------
    @property
    def hovertext(self):
        """
        Sets hover text elements associated with each (x,y) pair. If a
        single string, the same string appears over all the data
        points. If an array of string, the items are mapped in order to
        the this trace's (x,y) coordinates. To be seen, trace
        `hoverinfo` must contain a "text" flag.

        The 'hovertext' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["hovertext"]

    @hovertext.setter
    def hovertext(self, val):
        self["hovertext"] = val

    # hovertextsrc
    # ------------
    @property
    def hovertextsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hovertext`.

        The 'hovertextsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["hovertextsrc"]

    @hovertextsrc.setter
    def hovertextsrc(self, val):
        self["hovertextsrc"] = val

    # ids
    # ---
    @property
    def ids(self):
        """
        Assigns id labels to each datum. These ids for object constancy
        of data points during animation. Should be an array of strings,
        not numbers or any other type.

        The 'ids' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["ids"]

    @ids.setter
    def ids(self, val):
        self["ids"] = val

    # idssrc
    # ------
    @property
    def idssrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `ids`.

        The 'idssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["idssrc"]

    @idssrc.setter
    def idssrc(self, val):
        self["idssrc"] = val

    # insidetextanchor
    # ----------------
    @property
    def insidetextanchor(self):
        """
        Determines if texts are kept at center or start/end points in
        `textposition` "inside" mode.

        The 'insidetextanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['end', 'middle', 'start']

        Returns
        -------
        Any
        """
        return self["insidetextanchor"]

    @insidetextanchor.setter
    def insidetextanchor(self, val):
        self["insidetextanchor"] = val

    # insidetextfont
    # --------------
    @property
    def insidetextfont(self):
        """
        Sets the font used for `text` lying inside the bar.

        The 'insidetextfont' property is an instance of Insidetextfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.funnel.Insidetextfont`
          - A dict of string/value properties that will be passed
            to the Insidetextfont constructor

            Supported dict properties:

                color

                colorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `color`.
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The Chart Studio Cloud (at
                    https://chart-studio.plotly.com or on-premise)
                    generates images on a server, where only a
                    select number of fonts are installed and
                    supported. These include "Arial", "Balto",
                    "Courier New", "Droid Sans",, "Droid Serif",
                    "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                familysrc
                    Sets the source reference on Chart Studio Cloud
                    for `family`.
                size

                sizesrc
                    Sets the source reference on Chart Studio Cloud
                    for `size`.

        Returns
        -------
        plotly.graph_objs.funnel.Insidetextfont
        """
        return self["insidetextfont"]

    @insidetextfont.setter
    def insidetextfont(self, val):
        self["insidetextfont"] = val

    # legend
    # ------
    @property
    def legend(self):
        """
        Sets the reference to a legend to show this trace in.
        References to these legends are "legend", "legend2", "legend3",
        etc. Settings for these legends are set in the layout, under
        `layout.legend`, `layout.legend2`, etc.

        The 'legend' property is an identifier of a particular
        subplot, of type 'legend', that may be specified as the string 'legend'
        optionally followed by an integer >= 1
        (e.g. 'legend', 'legend1', 'legend2', 'legend3', etc.)

        Returns
        -------
        str
        """
        return self["legend"]

    @legend.setter
    def legend(self, val):
        self["legend"] = val

    # legendgroup
    # -----------
    @property
    def legendgroup(self):
        """
        Sets the legend group for this trace. Traces part of the same
        legend group hide/show at the same time when toggling legend
        items.

        The 'legendgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["legendgroup"]

    @legendgroup.setter
    def legendgroup(self, val):
        self["legendgroup"] = val

    # legendgrouptitle
    # ----------------
    @property
    def legendgrouptitle(self):
        """
        The 'legendgrouptitle' property is an instance of Legendgrouptitle
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.funnel.Legendgrouptitle`
          - A dict of string/value properties that will be passed
            to the Legendgrouptitle constructor

            Supported dict properties:

                font
                    Sets this legend group's title font.
                text
                    Sets the title of the legend group.

        Returns
        -------
        plotly.graph_objs.funnel.Legendgrouptitle
        """
        return self["legendgrouptitle"]

    @legendgrouptitle.setter
    def legendgrouptitle(self, val):
        self["legendgrouptitle"] = val

    # legendrank
    # ----------
    @property
    def legendrank(self):
        """
        Sets the legend rank for this trace. Items and groups with
        smaller ranks are presented on top/left side while with
        `*reversed* `legend.traceorder` they are on bottom/right side.
        The default legendrank is 1000, so that you can use ranks less
        than 1000 to place certain items before all unranked items, and
        ranks greater than 1000 to go after all unranked items.

        The 'legendrank' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["legendrank"]

    @legendrank.setter
    def legendrank(self, val):
        self["legendrank"] = val

    # legendwidth
    # -----------
    @property
    def legendwidth(self):
        """
        Sets the width (in px or fraction) of the legend for this
        trace.

        The 'legendwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["legendwidth"]

    @legendwidth.setter
    def legendwidth(self, val):
        self["legendwidth"] = val

    # marker
    # ------
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.funnel.Marker`
          - A dict of string/value properties that will be passed
            to the Marker constructor

            Supported dict properties:

                autocolorscale
                    Determines whether the colorscale is a default
                    palette (`autocolorscale: true`) or the palette
                    determined by `marker.colorscale`. Has an
                    effect only if in `marker.color` is set to a
                    numerical array. In case `colorscale` is
                    unspecified or `autocolorscale` is true, the
                    default palette will be chosen according to
                    whether numbers in the `color` array are all
                    positive, all negative or mixed.
                cauto
                    Determines whether or not the color domain is
                    computed with respect to the input data (here
                    in `marker.color`) or the bounds set in
                    `marker.cmin` and `marker.cmax` Has an effect
                    only if in `marker.color` is set to a numerical
                    array. Defaults to `false` when `marker.cmin`
                    and `marker.cmax` are set by the user.
                cmax
                    Sets the upper bound of the color domain. Has
                    an effect only if in `marker.color` is set to a
                    numerical array. Value should have the same
                    units as in `marker.color` and if set,
                    `marker.cmin` must be set as well.
                cmid
                    Sets the mid-point of the color domain by
                    scaling `marker.cmin` and/or `marker.cmax` to
                    be equidistant to this point. Has an effect
                    only if in `marker.color` is set to a numerical
                    array. Value should have the same units as in
                    `marker.color`. Has no effect when
                    `marker.cauto` is `false`.
                cmin
                    Sets the lower bound of the color domain. Has
                    an effect only if in `marker.color` is set to a
                    numerical array. Value should have the same
                    units as in `marker.color` and if set,
                    `marker.cmax` must be set as well.
                color
                    Sets the marker color. It accepts either a
                    specific color or an array of numbers that are
                    mapped to the colorscale relative to the max
                    and min values of the array or relative to
                    `marker.cmin` and `marker.cmax` if set.
                coloraxis
                    Sets a reference to a shared color axis.
                    References to these shared color axes are
                    "coloraxis", "coloraxis2", "coloraxis3", etc.
                    Settings for these shared color axes are set in
                    the layout, under `layout.coloraxis`,
                    `layout.coloraxis2`, etc. Note that multiple
                    color scales can be linked to the same color
                    axis.
                colorbar
                    :class:`plotly.graph_objects.funnel.marker.Colo
                    rBar` instance or dict with compatible
                    properties
                colorscale
                    Sets the colorscale. Has an effect only if in
                    `marker.color` is set to a numerical array. The
                    colorscale must be an array containing arrays
                    mapping a normalized value to an rgb, rgba,
                    hex, hsl, hsv, or named color string. At
                    minimum, a mapping for the lowest (0) and
                    highest (1) values are required. For example,
                    `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`.
                    To control the bounds of the colorscale in
                    color space, use `marker.cmin` and
                    `marker.cmax`. Alternatively, `colorscale` may
                    be a palette name string of the following list:
                    Blackbody,Bluered,Blues,Cividis,Earth,Electric,
                    Greens,Greys,Hot,Jet,Picnic,Portland,Rainbow,Rd
                    Bu,Reds,Viridis,YlGnBu,YlOrRd.
                colorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `color`.
                line
                    :class:`plotly.graph_objects.funnel.marker.Line
                    ` instance or dict with compatible properties
                opacity
                    Sets the opacity of the bars.
                opacitysrc
                    Sets the source reference on Chart Studio Cloud
                    for `opacity`.
                reversescale
                    Reverses the color mapping if true. Has an
                    effect only if in `marker.color` is set to a
                    numerical array. If true, `marker.cmin` will
                    correspond to the last color in the array and
                    `marker.cmax` will correspond to the first
                    color.
                showscale
                    Determines whether or not a colorbar is
                    displayed for this trace. Has an effect only if
                    in `marker.color` is set to a numerical array.

        Returns
        -------
        plotly.graph_objs.funnel.Marker
        """
        return self["marker"]

    @marker.setter
    def marker(self, val):
        self["marker"] = val

    # meta
    # ----
    @property
    def meta(self):
        """
        Assigns extra meta information associated with this trace that
        can be used in various text attributes. Attributes such as
        trace `name`, graph, axis and colorbar `title.text`, annotation
        `text` `rangeselector`, `updatemenues` and `sliders` `label`
        text all support `meta`. To access the trace `meta` values in
        an attribute in the same trace, simply use `%{meta[i]}` where
        `i` is the index or key of the `meta` item in question. To
        access trace `meta` in layout attributes, use
        `%{data[n[.meta[i]}` where `i` is the index or key of the
        `meta` and `n` is the trace index.

        The 'meta' property accepts values of any type

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["meta"]

    @meta.setter
    def meta(self, val):
        self["meta"] = val

    # metasrc
    # -------
    @property
    def metasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `meta`.

        The 'metasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["metasrc"]

    @metasrc.setter
    def metasrc(self, val):
        self["metasrc"] = val

    # name
    # ----
    @property
    def name(self):
        """
        Sets the trace name. The trace name appear as the legend item
        and on hover.

        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    # offset
    # ------
    @property
    def offset(self):
        """
        Shifts the position where the bar is drawn (in position axis
        units). In "group" barmode, traces that set "offset" will be
        excluded and drawn in "overlay" mode instead.

        The 'offset' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["offset"]

    @offset.setter
    def offset(self, val):
        self["offset"] = val

    # offsetgroup
    # -----------
    @property
    def offsetgroup(self):
        """
        Set several traces linked to the same position axis or matching
        axes to the same offsetgroup where bars of the same position
        coordinate will line up.

        The 'offsetgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["offsetgroup"]

    @offsetgroup.setter
    def offsetgroup(self, val):
        self["offsetgroup"] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the trace.

        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    # orientation
    # -----------
    @property
    def orientation(self):
        """
        Sets the orientation of the funnels. With "v" ("h"), the value
        of the each bar spans along the vertical (horizontal). By
        default funnels are tend to be oriented horizontally; unless
        only "y" array is presented or orientation is set to "v". Also
        regarding graphs including only 'horizontal' funnels,
        "autorange" on the "y-axis" are set to "reversed".

        The 'orientation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['v', 'h']

        Returns
        -------
        Any
        """
        return self["orientation"]

    @orientation.setter
    def orientation(self, val):
        self["orientation"] = val

    # outsidetextfont
    # ---------------
    @property
    def outsidetextfont(self):
        """
        Sets the font used for `text` lying outside the bar.

        The 'outsidetextfont' property is an instance of Outsidetextfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.funnel.Outsidetextfont`
          - A dict of string/value properties that will be passed
            to the Outsidetextfont constructor

            Supported dict properties:

                color

                colorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `color`.
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The Chart Studio Cloud (at
                    https://chart-studio.plotly.com or on-premise)
                    generates images on a server, where only a
                    select number of fonts are installed and
                    supported. These include "Arial", "Balto",
                    "Courier New", "Droid Sans",, "Droid Serif",
                    "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                familysrc
                    Sets the source reference on Chart Studio Cloud
                    for `family`.
                size

                sizesrc
                    Sets the source reference on Chart Studio Cloud
                    for `size`.

        Returns
        -------
        plotly.graph_objs.funnel.Outsidetextfont
        """
        return self["outsidetextfont"]

    @outsidetextfont.setter
    def outsidetextfont(self, val):
        self["outsidetextfont"] = val

    # selectedpoints
    # --------------
    @property
    def selectedpoints(self):
        """
        Array containing integer indices of selected points. Has an
        effect only for traces that support selections. Note that an
        empty array means an empty selection where the `unselected` are
        turned on for all points, whereas, any other non-array values
        means no selection all where the `selected` and `unselected`
        styles have no effect.

        The 'selectedpoints' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["selectedpoints"]

    @selectedpoints.setter
    def selectedpoints(self, val):
        self["selectedpoints"] = val

    # showlegend
    # ----------
    @property
    def showlegend(self):
        """
        Determines whether or not an item corresponding to this trace
        is shown in the legend.

        The 'showlegend' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showlegend"]

    @showlegend.setter
    def showlegend(self, val):
        self["showlegend"] = val

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.funnel.Stream`
          - A dict of string/value properties that will be passed
            to the Stream constructor

            Supported dict properties:

                maxpoints
                    Sets the maximum number of points to keep on
                    the plots from an incoming stream. If
                    `maxpoints` is set to 50, only the newest 50
                    points will be displayed on the plot.
                token
                    The stream id number links a data trace on a
                    plot with a stream. See https://chart-
                    studio.plotly.com/settings for more details.

        Returns
        -------
        plotly.graph_objs.funnel.Stream
        """
        return self["stream"]

    @stream.setter
    def stream(self, val):
        self["stream"] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets text elements associated with each (x,y) pair. If a single
        string, the same string appears over all the data points. If an
        array of string, the items are mapped in order to the this
        trace's (x,y) coordinates. If trace `hoverinfo` contains a
        "text" flag and "hovertext" is not set, these elements will be
        seen in the hover labels.

        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    # textangle
    # ---------
    @property
    def textangle(self):
        """
        Sets the angle of the tick labels with respect to the bar. For
        example, a `tickangle` of -90 draws the tick labels vertically.
        With "auto" the texts may automatically be rotated to fit with
        the maximum size in bars.

        The 'textangle' property is a angle (in degrees) that may be
        specified as a number between -180 and 180.
        Numeric values outside this range are converted to the equivalent value
        (e.g. 270 is converted to -90).

        Returns
        -------
        int|float
        """
        return self["textangle"]

    @textangle.setter
    def textangle(self, val):
        self["textangle"] = val

    # textfont
    # --------
    @property
    def textfont(self):
        """
        Sets the font used for `text`.

        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.funnel.Textfont`
          - A dict of string/value properties that will be passed
            to the Textfont constructor

            Supported dict properties:

                color

                colorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `color`.
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The Chart Studio Cloud (at
                    https://chart-studio.plotly.com or on-premise)
                    generates images on a server, where only a
                    select number of fonts are installed and
                    supported. These include "Arial", "Balto",
                    "Courier New", "Droid Sans",, "Droid Serif",
                    "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                familysrc
                    Sets the source reference on Chart Studio Cloud
                    for `family`.
                size

                sizesrc
                    Sets the source reference on Chart Studio Cloud
                    for `size`.

        Returns
        -------
        plotly.graph_objs.funnel.Textfont
        """
        return self["textfont"]

    @textfont.setter
    def textfont(self, val):
        self["textfont"] = val

    # textinfo
    # --------
    @property
    def textinfo(self):
        """
        Determines which trace information appear on the graph. In the
        case of having multiple funnels, percentages & totals are
        computed separately (per trace).

        The 'textinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['label', 'text', 'percent initial', 'percent previous', 'percent total', 'value'] joined with '+' characters
            (e.g. 'label+text')
            OR exactly one of ['none'] (e.g. 'none')

        Returns
        -------
        Any
        """
        return self["textinfo"]

    @textinfo.setter
    def textinfo(self, val):
        self["textinfo"] = val

    # textposition
    # ------------
    @property
    def textposition(self):
        """
        Specifies the location of the `text`. "inside" positions `text`
        inside, next to the bar end (rotated and scaled if needed).
        "outside" positions `text` outside, next to the bar end (scaled
        if needed), unless there is another bar stacked on this one,
        then the text gets pushed inside. "auto" tries to position
        `text` inside the bar, but if the bar is too small and no bar
        is stacked on this one the text is moved outside. If "none", no
        text appears.

        The 'textposition' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['inside', 'outside', 'auto', 'none']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["textposition"]

    @textposition.setter
    def textposition(self, val):
        self["textposition"] = val

    # textpositionsrc
    # ---------------
    @property
    def textpositionsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `textposition`.

        The 'textpositionsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["textpositionsrc"]

    @textpositionsrc.setter
    def textpositionsrc(self, val):
        self["textpositionsrc"] = val

    # textsrc
    # -------
    @property
    def textsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `text`.

        The 'textsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["textsrc"]

    @textsrc.setter
    def textsrc(self, val):
        self["textsrc"] = val

    # texttemplate
    # ------------
    @property
    def texttemplate(self):
        """
        Template string used for rendering the information text that
        appear on points. Note that this will override `textinfo`.
        Variables are inserted using %{variable}, for example "y:
        %{y}". Numbers are formatted using d3-format's syntax
        %{variable:d3-format}, for example "Price: %{y:$.2f}".
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format for
        details on the formatting syntax. Dates are formatted using
        d3-time-format's syntax %{variable|d3-time-format}, for example
        "Day: %{2019-01-01|%A}". https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format for details on the date
        formatting syntax. Every attributes that can be specified per-
        point (the ones that are `arrayOk: true`) are available.
        Finally, the template string has access to variables
        `percentInitial`, `percentPrevious`, `percentTotal`, `label`
        and `value`.

        The 'texttemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["texttemplate"]

    @texttemplate.setter
    def texttemplate(self, val):
        self["texttemplate"] = val

    # texttemplatesrc
    # ---------------
    @property
    def texttemplatesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `texttemplate`.

        The 'texttemplatesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["texttemplatesrc"]

    @texttemplatesrc.setter
    def texttemplatesrc(self, val):
        self["texttemplatesrc"] = val

    # uid
    # ---
    @property
    def uid(self):
        """
        Assign an id to this trace, Use this to provide object
        constancy between traces during animations and transitions.

        The 'uid' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["uid"]

    @uid.setter
    def uid(self, val):
        self["uid"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of some user-driven changes to the trace:
        `constraintrange` in `parcoords` traces, as well as some
        `editable: true` modifications such as `name` and
        `colorbar.title`. Defaults to `layout.uirevision`. Note that
        other user-driven trace attribute changes are controlled by
        `layout` attributes: `trace.visible` is controlled by
        `layout.legend.uirevision`, `selectedpoints` is controlled by
        `layout.selectionrevision`, and `colorbar.(x|y)` (accessible
        with `config: {editable: true}`) is controlled by
        `layout.editrevision`. Trace changes are tracked by `uid`,
        which only falls back on trace index if no `uid` is provided.
        So if your app can add/remove traces before the end of the
        `data` array, such that the same trace has a different index,
        you can still preserve user-driven changes if you give each
        trace a `uid` that stays with it as it moves.

        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this trace is visible. If
        "legendonly", the trace is not drawn, but can appear as a
        legend item (provided that the legend itself is visible).

        The 'visible' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'legendonly']

        Returns
        -------
        Any
        """
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    # width
    # -----
    @property
    def width(self):
        """
        Sets the bar width (in position axis units).

        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["width"]

    @width.setter
    def width(self, val):
        self["width"] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the x coordinates.

        The 'x' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    # x0
    # --
    @property
    def x0(self):
        """
        Alternate to `x`. Builds a linear space of x coordinates. Use
        with `dx` where `x0` is the starting coordinate and `dx` the
        step.

        The 'x0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["x0"]

    @x0.setter
    def x0(self, val):
        self["x0"] = val

    # xaxis
    # -----
    @property
    def xaxis(self):
        """
        Sets a reference between this trace's x coordinates and a 2D
        cartesian x axis. If "x" (the default value), the x coordinates
        refer to `layout.xaxis`. If "x2", the x coordinates refer to
        `layout.xaxis2`, and so on.

        The 'xaxis' property is an identifier of a particular
        subplot, of type 'x', that may be specified as the string 'x'
        optionally followed by an integer >= 1
        (e.g. 'x', 'x1', 'x2', 'x3', etc.)

        Returns
        -------
        str
        """
        return self["xaxis"]

    @xaxis.setter
    def xaxis(self, val):
        self["xaxis"] = val

    # xhoverformat
    # ------------
    @property
    def xhoverformat(self):
        """
        Sets the hover text formatting rulefor `x`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display *09~15~23.46*By default the values
        are formatted using `xaxis.hoverformat`.

        The 'xhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["xhoverformat"]

    @xhoverformat.setter
    def xhoverformat(self, val):
        self["xhoverformat"] = val

    # xperiod
    # -------
    @property
    def xperiod(self):
        """
        Only relevant when the axis `type` is "date". Sets the period
        positioning in milliseconds or "M<n>" on the x axis. Special
        values in the form of "M<n>" could be used to declare the
        number of months. In this case `n` must be a positive integer.

        The 'xperiod' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["xperiod"]

    @xperiod.setter
    def xperiod(self, val):
        self["xperiod"] = val

    # xperiod0
    # --------
    @property
    def xperiod0(self):
        """
        Only relevant when the axis `type` is "date". Sets the base for
        period positioning in milliseconds or date string on the x0
        axis. When `x0period` is round number of weeks, the `x0period0`
        by default would be on a Sunday i.e. 2000-01-02, otherwise it
        would be at 2000-01-01.

        The 'xperiod0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["xperiod0"]

    @xperiod0.setter
    def xperiod0(self, val):
        self["xperiod0"] = val

    # xperiodalignment
    # ----------------
    @property
    def xperiodalignment(self):
        """
        Only relevant when the axis `type` is "date". Sets the
        alignment of data points on the x axis.

        The 'xperiodalignment' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['start', 'middle', 'end']

        Returns
        -------
        Any
        """
        return self["xperiodalignment"]

    @xperiodalignment.setter
    def xperiodalignment(self, val):
        self["xperiodalignment"] = val

    # xsrc
    # ----
    @property
    def xsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `x`.

        The 'xsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["xsrc"]

    @xsrc.setter
    def xsrc(self, val):
        self["xsrc"] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the y coordinates.

        The 'y' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    # y0
    # --
    @property
    def y0(self):
        """
        Alternate to `y`. Builds a linear space of y coordinates. Use
        with `dy` where `y0` is the starting coordinate and `dy` the
        step.

        The 'y0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["y0"]

    @y0.setter
    def y0(self, val):
        self["y0"] = val

    # yaxis
    # -----
    @property
    def yaxis(self):
        """
        Sets a reference between this trace's y coordinates and a 2D
        cartesian y axis. If "y" (the default value), the y coordinates
        refer to `layout.yaxis`. If "y2", the y coordinates refer to
        `layout.yaxis2`, and so on.

        The 'yaxis' property is an identifier of a particular
        subplot, of type 'y', that may be specified as the string 'y'
        optionally followed by an integer >= 1
        (e.g. 'y', 'y1', 'y2', 'y3', etc.)

        Returns
        -------
        str
        """
        return self["yaxis"]

    @yaxis.setter
    def yaxis(self, val):
        self["yaxis"] = val

    # yhoverformat
    # ------------
    @property
    def yhoverformat(self):
        """
        Sets the hover text formatting rulefor `y`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display *09~15~23.46*By default the values
        are formatted using `yaxis.hoverformat`.

        The 'yhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["yhoverformat"]

    @yhoverformat.setter
    def yhoverformat(self, val):
        self["yhoverformat"] = val

    # yperiod
    # -------
    @property
    def yperiod(self):
        """
        Only relevant when the axis `type` is "date". Sets the period
        positioning in milliseconds or "M<n>" on the y axis. Special
        values in the form of "M<n>" could be used to declare the
        number of months. In this case `n` must be a positive integer.

        The 'yperiod' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["yperiod"]

    @yperiod.setter
    def yperiod(self, val):
        self["yperiod"] = val

    # yperiod0
    # --------
    @property
    def yperiod0(self):
        """
        Only relevant when the axis `type` is "date". Sets the base for
        period positioning in milliseconds or date string on the y0
        axis. When `y0period` is round number of weeks, the `y0period0`
        by default would be on a Sunday i.e. 2000-01-02, otherwise it
        would be at 2000-01-01.

        The 'yperiod0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["yperiod0"]

    @yperiod0.setter
    def yperiod0(self, val):
        self["yperiod0"] = val

    # yperiodalignment
    # ----------------
    @property
    def yperiodalignment(self):
        """
        Only relevant when the axis `type` is "date". Sets the
        alignment of data points on the y axis.

        The 'yperiodalignment' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['start', 'middle', 'end']

        Returns
        -------
        Any
        """
        return self["yperiodalignment"]

    @yperiodalignment.setter
    def yperiodalignment(self, val):
        self["yperiodalignment"] = val

    # ysrc
    # ----
    @property
    def ysrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `y`.

        The 'ysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["ysrc"]

    @ysrc.setter
    def ysrc(self, val):
        self["ysrc"] = val

    # type
    # ----
    @property
    def type(self):
        return self._props["type"]

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        cliponaxis
            Determines whether the text nodes are clipped about the
            subplot axes. To show the text nodes above axis lines
            and tick labels, make sure to set `xaxis.layer` and
            `yaxis.layer` to *below traces*.
        connector
            :class:`plotly.graph_objects.funnel.Connector` instance
            or dict with compatible properties
        constraintext
            Constrain the size of text inside or outside a bar to
            be no larger than the bar itself.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.funnel.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}" as well as %{xother}, {%_xother},
            {%_xother_}, {%xother_}. When showing info for several
            points, "xother" will be added to those with different
            x positions from the first point. An underscore before
            or after "(x|y)other" will add a space on that side,
            only when this field is shown. Numbers are formatted
            using d3-format's syntax %{variable:d3-format}, for
            example "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. Finally, the template string has access
            to variables `percentInitial`, `percentPrevious` and
            `percentTotal`. Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            `hovertext`.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            `ids`.
        insidetextanchor
            Determines if texts are kept at center or start/end
            points in `textposition` "inside" mode.
        insidetextfont
            Sets the font used for `text` lying inside the bar.
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        legendgrouptitle
            :class:`plotly.graph_objects.funnel.Legendgrouptitle`
            instance or dict with compatible properties
        legendrank
            Sets the legend rank for this trace. Items and groups
            with smaller ranks are presented on top/left side while
            with `*reversed* `legend.traceorder` they are on
            bottom/right side. The default legendrank is 1000, so
            that you can use ranks less than 1000 to place certain
            items before all unranked items, and ranks greater than
            1000 to go after all unranked items.
        legendwidth
            Sets the width (in px or fraction) of the legend for
            this trace.
        marker
            :class:`plotly.graph_objects.funnel.Marker` instance or
            dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            `meta`.
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        offset
            Shifts the position where the bar is drawn (in position
            axis units). In "group" barmode, traces that set
            "offset" will be excluded and drawn in "overlay" mode
            instead.
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the funnels. With "v" ("h"),
            the value of the each bar spans along the vertical
            (horizontal). By default funnels are tend to be
            oriented horizontally; unless only "y" array is
            presented or orientation is set to "v". Also regarding
            graphs including only 'horizontal' funnels, "autorange"
            on the "y-axis" are set to "reversed".
        outsidetextfont
            Sets the font used for `text` lying outside the bar.
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.funnel.Stream` instance or
            dict with compatible properties
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textangle
            Sets the angle of the tick labels with respect to the
            bar. For example, a `tickangle` of -90 draws the tick
            labels vertically. With "auto" the texts may
            automatically be rotated to fit with the maximum size
            in bars.
        textfont
            Sets the font used for `text`.
        textinfo
            Determines which trace information appear on the graph.
            In the case of having multiple funnels, percentages &
            totals are computed separately (per trace).
        textposition
            Specifies the location of the `text`. "inside"
            positions `text` inside, next to the bar end (rotated
            and scaled if needed). "outside" positions `text`
            outside, next to the bar end (scaled if needed), unless
            there is another bar stacked on this one, then the text
            gets pushed inside. "auto" tries to position `text`
            inside the bar, but if the bar is too small and no bar
            is stacked on this one the text is moved outside. If
            "none", no text appears.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            `textposition`.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            `text`.
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. Every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. Finally, the template string has access
            to variables `percentInitial`, `percentPrevious`,
            `percentTotal`, `label` and `value`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `texttemplate`.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the bar width (in position axis units).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xhoverformat
            Sets the hover text formatting rulefor `x`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `xaxis.hoverformat`.
        xperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the x
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        xperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the x0 axis. When `x0period` is round number
            of weeks, the `x0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        xperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the x axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        yhoverformat
            Sets the hover text formatting rulefor `y`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `yaxis.hoverformat`.
        yperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the y
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        yperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the y0 axis. When `y0period` is round number
            of weeks, the `y0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        yperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the y axis.
        ysrc
            Sets the source reference on Chart Studio Cloud for
            `y`.
        """

    def __init__(
        self,
        arg=None,
        alignmentgroup=None,
        cliponaxis=None,
        connector=None,
        constraintext=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextanchor=None,
        insidetextfont=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        offset=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        outsidetextfont=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textangle=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        width=None,
        x=None,
        x0=None,
        xaxis=None,
        xhoverformat=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        yhoverformat=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        **kwargs,
    ):
        """
        Construct a new Funnel object

        Visualize stages in a process using length-encoded bars. This
        trace can be used to show data in either a part-to-whole
        representation wherein each item appears in a single stage, or
        in a "drop-off" representation wherein each item appears in
        each stage it traversed. See also the "funnelarea" trace type
        for a different approach to visualizing funnel data.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Funnel`
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        cliponaxis
            Determines whether the text nodes are clipped about the
            subplot axes. To show the text nodes above axis lines
            and tick labels, make sure to set `xaxis.layer` and
            `yaxis.layer` to *below traces*.
        connector
            :class:`plotly.graph_objects.funnel.Connector` instance
            or dict with compatible properties
        constraintext
            Constrain the size of text inside or outside a bar to
            be no larger than the bar itself.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.funnel.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}" as well as %{xother}, {%_xother},
            {%_xother_}, {%xother_}. When showing info for several
            points, "xother" will be added to those with different
            x positions from the first point. An underscore before
            or after "(x|y)other" will add a space on that side,
            only when this field is shown. Numbers are formatted
            using d3-format's syntax %{variable:d3-format}, for
            example "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. Finally, the template string has access
            to variables `percentInitial`, `percentPrevious` and
            `percentTotal`. Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            `hovertext`.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            `ids`.
        insidetextanchor
            Determines if texts are kept at center or start/end
            points in `textposition` "inside" mode.
        insidetextfont
            Sets the font used for `text` lying inside the bar.
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        legendgrouptitle
            :class:`plotly.graph_objects.funnel.Legendgrouptitle`
            instance or dict with compatible properties
        legendrank
            Sets the legend rank for this trace. Items and groups
            with smaller ranks are presented on top/left side while
            with `*reversed* `legend.traceorder` they are on
            bottom/right side. The default legendrank is 1000, so
            that you can use ranks less than 1000 to place certain
            items before all unranked items, and ranks greater than
            1000 to go after all unranked items.
        legendwidth
            Sets the width (in px or fraction) of the legend for
            this trace.
        marker
            :class:`plotly.graph_objects.funnel.Marker` instance or
            dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            `meta`.
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        offset
            Shifts the position where the bar is drawn (in position
            axis units). In "group" barmode, traces that set
            "offset" will be excluded and drawn in "overlay" mode
            instead.
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the funnels. With "v" ("h"),
            the value of the each bar spans along the vertical
            (horizontal). By default funnels are tend to be
            oriented horizontally; unless only "y" array is
            presented or orientation is set to "v". Also regarding
            graphs including only 'horizontal' funnels, "autorange"
            on the "y-axis" are set to "reversed".
        outsidetextfont
            Sets the font used for `text` lying outside the bar.
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.funnel.Stream` instance or
            dict with compatible properties
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textangle
            Sets the angle of the tick labels with respect to the
            bar. For example, a `tickangle` of -90 draws the tick
            labels vertically. With "auto" the texts may
            automatically be rotated to fit with the maximum size
            in bars.
        textfont
            Sets the font used for `text`.
        textinfo
            Determines which trace information appear on the graph.
            In the case of having multiple funnels, percentages &
            totals are computed separately (per trace).
        textposition
            Specifies the location of the `text`. "inside"
            positions `text` inside, next to the bar end (rotated
            and scaled if needed). "outside" positions `text`
            outside, next to the bar end (scaled if needed), unless
            there is another bar stacked on this one, then the text
            gets pushed inside. "auto" tries to position `text`
            inside the bar, but if the bar is too small and no bar
            is stacked on this one the text is moved outside. If
            "none", no text appears.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            `textposition`.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            `text`.
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. Every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. Finally, the template string has access
            to variables `percentInitial`, `percentPrevious`,
            `percentTotal`, `label` and `value`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `texttemplate`.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the bar width (in position axis units).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xhoverformat
            Sets the hover text formatting rulefor `x`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `xaxis.hoverformat`.
        xperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the x
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        xperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the x0 axis. When `x0period` is round number
            of weeks, the `x0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        xperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the x axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        yhoverformat
            Sets the hover text formatting rulefor `y`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `yaxis.hoverformat`.
        yperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the y
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        yperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the y0 axis. When `y0period` is round number
            of weeks, the `y0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        yperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the y axis.
        ysrc
            Sets the source reference on Chart Studio Cloud for
            `y`.

        Returns
        -------
        Funnel
        """
        super(Funnel, self).__init__("funnel")

        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.Funnel
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Funnel`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("alignmentgroup", None)
        _v = alignmentgroup if alignmentgroup is not None else _v
        if _v is not None:
            self["alignmentgroup"] = _v
        _v = arg.pop("cliponaxis", None)
        _v = cliponaxis if cliponaxis is not None else _v
        if _v is not None:
            self["cliponaxis"] = _v
        _v = arg.pop("connector", None)
        _v = connector if connector is not None else _v
        if _v is not None:
            self["connector"] = _v
        _v = arg.pop("constraintext", None)
        _v = constraintext if constraintext is not None else _v
        if _v is not None:
            self["constraintext"] = _v
        _v = arg.pop("customdata", None)
        _v = customdata if customdata is not None else _v
        if _v is not None:
            self["customdata"] = _v
        _v = arg.pop("customdatasrc", None)
        _v = customdatasrc if customdatasrc is not None else _v
        if _v is not None:
            self["customdatasrc"] = _v
        _v = arg.pop("dx", None)
        _v = dx if dx is not None else _v
        if _v is not None:
            self["dx"] = _v
        _v = arg.pop("dy", None)
        _v = dy if dy is not None else _v
        if _v is not None:
            self["dy"] = _v
        _v = arg.pop("hoverinfo", None)
        _v = hoverinfo if hoverinfo is not None else _v
        if _v is not None:
            self["hoverinfo"] = _v
        _v = arg.pop("hoverinfosrc", None)
        _v = hoverinfosrc if hoverinfosrc is not None else _v
        if _v is not None:
            self["hoverinfosrc"] = _v
        _v = arg.pop("hoverlabel", None)
        _v = hoverlabel if hoverlabel is not None else _v
        if _v is not None:
            self["hoverlabel"] = _v
        _v = arg.pop("hovertemplate", None)
        _v = hovertemplate if hovertemplate is not None else _v
        if _v is not None:
            self["hovertemplate"] = _v
        _v = arg.pop("hovertemplatesrc", None)
        _v = hovertemplatesrc if hovertemplatesrc is not None else _v
        if _v is not None:
            self["hovertemplatesrc"] = _v
        _v = arg.pop("hovertext", None)
        _v = hovertext if hovertext is not None else _v
        if _v is not None:
            self["hovertext"] = _v
        _v = arg.pop("hovertextsrc", None)
        _v = hovertextsrc if hovertextsrc is not None else _v
        if _v is not None:
            self["hovertextsrc"] = _v
        _v = arg.pop("ids", None)
        _v = ids if ids is not None else _v
        if _v is not None:
            self["ids"] = _v
        _v = arg.pop("idssrc", None)
        _v = idssrc if idssrc is not None else _v
        if _v is not None:
            self["idssrc"] = _v
        _v = arg.pop("insidetextanchor", None)
        _v = insidetextanchor if insidetextanchor is not None else _v
        if _v is not None:
            self["insidetextanchor"] = _v
        _v = arg.pop("insidetextfont", None)
        _v = insidetextfont if insidetextfont is not None else _v
        if _v is not None:
            self["insidetextfont"] = _v
        _v = arg.pop("legend", None)
        _v = legend if legend is not None else _v
        if _v is not None:
            self["legend"] = _v
        _v = arg.pop("legendgroup", None)
        _v = legendgroup if legendgroup is not None else _v
        if _v is not None:
            self["legendgroup"] = _v
        _v = arg.pop("legendgrouptitle", None)
        _v = legendgrouptitle if legendgrouptitle is not None else _v
        if _v is not None:
            self["legendgrouptitle"] = _v
        _v = arg.pop("legendrank", None)
        _v = legendrank if legendrank is not None else _v
        if _v is not None:
            self["legendrank"] = _v
        _v = arg.pop("legendwidth", None)
        _v = legendwidth if legendwidth is not None else _v
        if _v is not None:
            self["legendwidth"] = _v
        _v = arg.pop("marker", None)
        _v = marker if marker is not None else _v
        if _v is not None:
            self["marker"] = _v
        _v = arg.pop("meta", None)
        _v = meta if meta is not None else _v
        if _v is not None:
            self["meta"] = _v
        _v = arg.pop("metasrc", None)
        _v = metasrc if metasrc is not None else _v
        if _v is not None:
            self["metasrc"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("offset", None)
        _v = offset if offset is not None else _v
        if _v is not None:
            self["offset"] = _v
        _v = arg.pop("offsetgroup", None)
        _v = offsetgroup if offsetgroup is not None else _v
        if _v is not None:
            self["offsetgroup"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("orientation", None)
        _v = orientation if orientation is not None else _v
        if _v is not None:
            self["orientation"] = _v
        _v = arg.pop("outsidetextfont", None)
        _v = outsidetextfont if outsidetextfont is not None else _v
        if _v is not None:
            self["outsidetextfont"] = _v
        _v = arg.pop("selectedpoints", None)
        _v = selectedpoints if selectedpoints is not None else _v
        if _v is not None:
            self["selectedpoints"] = _v
        _v = arg.pop("showlegend", None)
        _v = showlegend if showlegend is not None else _v
        if _v is not None:
            self["showlegend"] = _v
        _v = arg.pop("stream", None)
        _v = stream if stream is not None else _v
        if _v is not None:
            self["stream"] = _v
        _v = arg.pop("text", None)
        _v = text if text is not None else _v
        if _v is not None:
            self["text"] = _v
        _v = arg.pop("textangle", None)
        _v = textangle if textangle is not None else _v
        if _v is not None:
            self["textangle"] = _v
        _v = arg.pop("textfont", None)
        _v = textfont if textfont is not None else _v
        if _v is not None:
            self["textfont"] = _v
        _v = arg.pop("textinfo", None)
        _v = textinfo if textinfo is not None else _v
        if _v is not None:
            self["textinfo"] = _v
        _v = arg.pop("textposition", None)
        _v = textposition if textposition is not None else _v
        if _v is not None:
            self["textposition"] = _v
        _v = arg.pop("textpositionsrc", None)
        _v = textpositionsrc if textpositionsrc is not None else _v
        if _v is not None:
            self["textpositionsrc"] = _v
        _v = arg.pop("textsrc", None)
        _v = textsrc if textsrc is not None else _v
        if _v is not None:
            self["textsrc"] = _v
        _v = arg.pop("texttemplate", None)
        _v = texttemplate if texttemplate is not None else _v
        if _v is not None:
            self["texttemplate"] = _v
        _v = arg.pop("texttemplatesrc", None)
        _v = texttemplatesrc if texttemplatesrc is not None else _v
        if _v is not None:
            self["texttemplatesrc"] = _v
        _v = arg.pop("uid", None)
        _v = uid if uid is not None else _v
        if _v is not None:
            self["uid"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        _v = arg.pop("width", None)
        _v = width if width is not None else _v
        if _v is not None:
            self["width"] = _v
        _v = arg.pop("x", None)
        _v = x if x is not None else _v
        if _v is not None:
            self["x"] = _v
        _v = arg.pop("x0", None)
        _v = x0 if x0 is not None else _v
        if _v is not None:
            self["x0"] = _v
        _v = arg.pop("xaxis", None)
        _v = xaxis if xaxis is not None else _v
        if _v is not None:
            self["xaxis"] = _v
        _v = arg.pop("xhoverformat", None)
        _v = xhoverformat if xhoverformat is not None else _v
        if _v is not None:
            self["xhoverformat"] = _v
        _v = arg.pop("xperiod", None)
        _v = xperiod if xperiod is not None else _v
        if _v is not None:
            self["xperiod"] = _v
        _v = arg.pop("xperiod0", None)
        _v = xperiod0 if xperiod0 is not None else _v
        if _v is not None:
            self["xperiod0"] = _v
        _v = arg.pop("xperiodalignment", None)
        _v = xperiodalignment if xperiodalignment is not None else _v
        if _v is not None:
            self["xperiodalignment"] = _v
        _v = arg.pop("xsrc", None)
        _v = xsrc if xsrc is not None else _v
        if _v is not None:
            self["xsrc"] = _v
        _v = arg.pop("y", None)
        _v = y if y is not None else _v
        if _v is not None:
            self["y"] = _v
        _v = arg.pop("y0", None)
        _v = y0 if y0 is not None else _v
        if _v is not None:
            self["y0"] = _v
        _v = arg.pop("yaxis", None)
        _v = yaxis if yaxis is not None else _v
        if _v is not None:
            self["yaxis"] = _v
        _v = arg.pop("yhoverformat", None)
        _v = yhoverformat if yhoverformat is not None else _v
        if _v is not None:
            self["yhoverformat"] = _v
        _v = arg.pop("yperiod", None)
        _v = yperiod if yperiod is not None else _v
        if _v is not None:
            self["yperiod"] = _v
        _v = arg.pop("yperiod0", None)
        _v = yperiod0 if yperiod0 is not None else _v
        if _v is not None:
            self["yperiod0"] = _v
        _v = arg.pop("yperiodalignment", None)
        _v = yperiodalignment if yperiodalignment is not None else _v
        if _v is not None:
            self["yperiodalignment"] = _v
        _v = arg.pop("ysrc", None)
        _v = ysrc if ysrc is not None else _v
        if _v is not None:
            self["ysrc"] = _v

        # Read-only literals
        # ------------------

        self._props["type"] = "funnel"
        arg.pop("type", None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
