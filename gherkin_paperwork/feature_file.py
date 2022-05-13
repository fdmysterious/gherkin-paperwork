"""
┌───────────────────────────────────────────────┐
│ Represent Gherkin feature file as dataclasses │
└───────────────────────────────────────────────┘

 Florian Dupeyron
 May 2022
"""

from dataclasses import dataclass, field
from typing      import List

# ┌────────────────────────────────────────┐
# │ Generic dataclasses                    │
# └────────────────────────────────────────┘

@dataclass
class Location:
    column: int
    line: int


# ┌────────────────────────────────────────┐
# │ Steps                                  │
# └────────────────────────────────────────┘

@dataclass
class Step:
    id: int
    keyword: str
    location: Location
    text: str

    @classmethod
    def from_dict(cls, data: dict):
        # Copy data, parse location
        dd2 = data.copy()
        del dd2["location"]

        location = Location(**data["location"])

        return cls(**dd2, location=location)


# ┌────────────────────────────────────────┐
# │ Scenario                               │
# └────────────────────────────────────────┘

@dataclass
class Scenario:
    id: int
    keyword: str
    location: Location
    name: str
    description: str
    examples: List[any] # TODO #
    steps: List[Step]
    tags: List[str]

    @classmethod
    def from_dict(cls, data: dict):
        # Copy steps field, remove from dict
        dd2   = data.copy()
        del dd2["steps"]
        del dd2["location"]

        # Parse location and steps
        location = Location(**data["location"])
        steps    = [Step.from_dict(step_desc) for step_desc in data["steps"]]

        # Create Scenario object
        return cls(**dd2, location=location, steps=steps)
