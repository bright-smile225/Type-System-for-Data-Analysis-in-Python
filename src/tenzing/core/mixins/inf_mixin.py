import numpy as np


class infMixin:
    """Mixin adding infinite value support to tenzing types

    When creating a custom Tenzing type simply inherit from infMixin to add
    automatic support for infinite values.

    >>> class tenzing_integer(infMixin, tenzing_generic):
    >>>     # Implementation

    """
    @staticmethod
    def get_series_mask(series):
        mask = np.isinf(series)
        return super().get_series_mask(series) & (~mask)

    @classmethod
    def get_series(cls, series):
        try:
            if np.issubdtype(series.dtype, np.number):
                return series[~np.isinf(series)]
            else:
                return series
        except TypeError:
            return series

    @classmethod
    def cast_op(cls, series, operation=None):
        operation = operation if operation is not None else super().cast_op
        notinf_series = cls.get_series(series)
        # TODO: copy?
        return operation(notinf_series)

    @classmethod
    def contains_op(cls, series):
        notinf_series = cls.get_series(series)
        return super().contains_op(notinf_series)

    @classmethod
    def summarization_op(cls, series):
        print('inf.summarization_op')
        idx = np.isinf(series)

        summary = super().summarization_op(series[~idx])
        summary["inf_count"] = idx.values.sum()
        summary["perc_inf"] = (
            summary["inf_count"] / series.shape[0] if series.shape[0] > 0 else 0
        )
        return summary
