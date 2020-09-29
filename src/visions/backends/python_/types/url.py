from typing import Iterable, Sequence
from urllib.parse import ParseResult, urlparse

from visions.types.string import String
from visions.types.url import URL


@URL.contains_op.register
def url_contains(sequence: Sequence, state: dict) -> bool:
    return all(isinstance(sequence, ParseResult) for value in sequence)


@URL.register_transformer(String, Sequence)
def string_to_url(sequence: Iterable, state: dict) -> Iterable:
    return map(urlparse, sequence)


@URL.register_relationship(String, Sequence)
def string_is_url(sequence: Iterable, state: dict) -> bool:
    try:
        _ = all(isinstance(urlparse(value), ParseResult) for value in sequence)
        return True
    except:
        return False
