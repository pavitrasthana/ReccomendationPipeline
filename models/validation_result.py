from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class ValidationResult:
    """
    Represents the result of a single validation rule.
    """

    rule: str
    status: str
    severity: str
    message: str
    details: Dict[str, Any]

    def to_dict(self):
        return asdict(self)