import _plotly_utils.basevalidators


class TextcaseValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="textcase",
        parent_name="scattermap.legendgrouptitle.font",
        **kwargs,
    ):
        super(TextcaseValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            values=kwargs.pop("values", ["normal", "word caps", "upper", "lower"]),
            **kwargs,
        )
