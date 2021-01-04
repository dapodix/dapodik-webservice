from attr import attrs
from functools import partial

dataclass = partial(
    attrs,
    auto_attribs=True,
    slots=True,
)
