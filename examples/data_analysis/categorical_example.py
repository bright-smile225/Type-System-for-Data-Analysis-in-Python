import pandas as pd

from visions.functional import detect_series_type
from visions.typesets import StandardSet
from visions.types import Categorical, Boolean

from examples.data_analysis.categorical import Category

ts = StandardSet()
ts -= Boolean
ts -= Categorical
ts += Category

s1 = pd.Series(["A", "B", "C"] * 1000, dtype="category")
print(s1 in Category)
print(detect_series_type(s1, ts))

s2 = pd.Series([True, False] * 1000)
print(s2 in Category)
print(detect_series_type(s2, ts))
