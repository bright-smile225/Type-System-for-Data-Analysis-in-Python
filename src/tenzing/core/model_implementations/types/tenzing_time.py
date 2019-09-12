import pandas.api.types as pdt
import pandas as pd

from tenzing.core.model_implementations.types.tenzing_datetime import tenzing_datetime


class tenzing_time(tenzing_datetime):
    """**Time** implementation of :class:`tenzing.core.models.tenzing_model`.

    >>> x = pd.Series([pd.datetime(2017, 3, 5), pd.datetime(2019, 12, 4)])
    >>> x in tenzing_time
    True
    """

    @classmethod
    def contains_op(self, series):
        return pdt.is_datetime64_any_dtype(series) and series.eq(
            series.replace(day=1, month=1, year=1970)
        )

    @classmethod
    def cast_op(self, series, operation=None):
        return pd.to_datetime(series)

    @classmethod
    def summarization_op(self, series):
        summary = super().summarization_op(series)
        # TODO: specify format
        return summary
