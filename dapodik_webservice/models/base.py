from typing import Any, Dict, Optional, List, Type, TypeVar

from dapodik_webservice.typing import Row, Rows

KLS = TypeVar("KLS", bound="BaseModel")


class BaseModel(object):
    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @classmethod
    def from_list(cls: Type[KLS], data: Optional[List[Dict[str, Any]]]) -> List[KLS]:
        results: List[KLS] = list()
        if not data:
            return results
        for dat in data:
            results.append(cls(**dat))
        return results

    @classmethod
    def from_result(cls: Type[KLS], data: dict) -> KLS:
        rows: Row = data["rows"]
        return cls(**rows)

    @classmethod
    def from_results(cls: Type[KLS], data: dict) -> List[KLS]:
        rows: Rows = data["rows"]
        return cls.from_list(rows)
