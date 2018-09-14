import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.DataArrayValidator):

    def __init__(self, plotly_name='y', parent_name='heatmap', **kwargs):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc+clearAxisTypes',
            implied_edits={'ytype': 'array'},
            role='data',
            **kwargs
        )