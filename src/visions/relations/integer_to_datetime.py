from typing import Callable, Dict, TypeVar
import functools
import pandas as pd

from visions.relations import InferenceRelation
from visions.relations.string_to_datetime import to_datetime_year_month_day
from visions.types import Integer
from visions.utils.coercion import test_utils


T = TypeVar("T")


def redirect_state(func: Callable[[pd.Series], T]) -> Callable[[pd.Series, Dict], T]:
    @functools.wraps(func)
    def inner(series: pd.Series, state: Dict) -> T:
        return func(series)

    return inner


def to_datetime(series: pd.Series, state: dict) -> pd.Series:
    return pd.to_datetime(series)


def _to_datetime(cls, func: Callable[[pd.Series], pd.Series]) -> InferenceRelation:
    return InferenceRelation(
        relationship=redirect_state(
            test_utils.coercion_test(lambda s: func(s.astype(str)))
        ),
        transformer=to_datetime,
        type=cls,
        related_type=Integer,
    )


# TODO: do only convert obvious dates (20191003000000)
def integer_to_datetime(cls):
    return _to_datetime(cls, to_datetime)


def integer_to_datetime_year_month_day(cls) -> InferenceRelation:
    return _to_datetime(cls, to_datetime_year_month_day)
