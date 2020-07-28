from visions.types import (
    Generic,
    Boolean,
    Categorical,
    Complex,
    DateTime,
    Float,
    Integer,
    Object,
    String,
    TimeDelta,
)
from visions.typesets.typeset import VisionsTypeset


class StandardSet(VisionsTypeset):
    """The standard visions typesets

    Includes support for the following types:

    - Float
    - Integer
    - Boolean
    - Object
    - String
    - Complex
    - Categorical
    - DateTime
    - TimeDelta

    """

    def __init__(self):
        types = {
            Generic,
            Boolean,
            Float,
            Object,
            Complex,
            Categorical,
            DateTime,
            TimeDelta,
            Integer,
            String,
        }
        super().__init__(types)
