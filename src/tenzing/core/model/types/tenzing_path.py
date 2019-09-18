from pathlib import Path, PureWindowsPath, PurePosixPath, PurePath

import pandas as pd

from tenzing.core.model.types.tenzing_object import tenzing_object


class tenzing_path(tenzing_object):
    """**Path** implementation of :class:`tenzing.core.models.tenzing_model`.

    Examples:
        >>> x = pd.Series([Path('/home/user/file.txt'), Path('/home/user/test2.txt')])
        >>> x in tenzing_path
        True
    """

    @classmethod
    def mask(cls, series: pd.Series) -> pd.Series:
        super_mask = super().mask(series)

        if not super_mask.any():
            return super_mask

        return super_mask & series[super_mask].apply(
            lambda x: isinstance(x, PurePath) and x.is_absolute()
        )

    @classmethod
    def cast_op(cls, series: pd.Series, operation=None) -> pd.Series:
        return series.apply(PurePath)
