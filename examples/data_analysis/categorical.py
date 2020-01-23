import pandas.api.types as pdt
import pandas as pd
import numpy as np
from typing import Sequence, List

from visions import visions_string, visions_integer, visions_object
from visions.core.model.relations import IdentityRelation, InferenceRelation
from visions.core.model import TypeRelation
from visions.core.model.type import VisionsBaseType
from visions.utils.coercion.test_utils import coercion_map_test, coercion_map


def to_category(series: pd.Series) -> pd.Series:
    if series.isin({True, False}).all():
        return series.astype(bool)
    elif series.isin({True, False, None, np.nan}).all():
        return series.astype("Bool")
    else:
        unsupported_values = series[~series.isin({True, False, None, np.nan})].unique()
        raise ValueError(
            "Values not supported {unsupported_values}".format(
                unsupported_values=unsupported_values
            )
        )


def _get_relations(cls) -> List[TypeRelation]:
    from visions.core.implementations.types import visions_generic

    relations = [
        IdentityRelation(cls, visions_generic),
        InferenceRelation(
            cls,
            visions_string,
            relationship=lambda s: coercion_map_test(cls.string_coercions)(
                s.str.lower()
            ),
            transformer=lambda s: to_category(
                coercion_map(cls.string_coercions)(s.str.lower())
            ),
        ),
        InferenceRelation(
            cls,
            visions_integer,
            relationship=lambda s: s.isin({0, 1, np.nan}).all(),
            transformer=to_category,
        ),
        InferenceRelation(
            cls,
            visions_object,
            relationship=lambda s: s.apply(type).isin([type(None), bool]).all(),
            transformer=to_category,
        ),
    ]
    return relations


class visions_category(VisionsBaseType):
    """**Categorical** implementation of :class:`visions.core.model.type.VisionsBaseType`.

    Examples:
        >>> x = pd.Series([True, False, 1], dtype='category')
        >>> x in visions_category
        True
    """

    @classmethod
    def get_relations(cls) -> Sequence[TypeRelation]:
        return _get_relations(cls)

    @classmethod
    def contains_op(cls, series: pd.Series) -> bool:
        return pdt.is_categorical_dtype(series) or pdt.is_bool_dtype(series)
