import pandas as pd
from urllib.parse import urlparse, ParseResult

from tenzing.core.model.types.tenzing_object import tenzing_object


class tenzing_url(tenzing_object):
    """**Url** implementation of :class:`tenzing.core.models.tenzing_model`.

    Examples:
        >>> from urllib.parse import urlparse
        >>> x = pd.Series([urlparse('http://www.cwi.nl:80/%7Eguido/Python.html'), urlparse('https://github.com/pandas-profiling/pandas-profiling')])
        >>> x in tenzing_url
        True
    """

    @classmethod
    def mask(cls, series: pd.Series) -> pd.Series:
        return series.apply(lambda x: isinstance(x, ParseResult))

    @classmethod
    def cast_op(cls, series: pd.Series, operation=None) -> pd.Series:
        return series.apply(urlparse)
