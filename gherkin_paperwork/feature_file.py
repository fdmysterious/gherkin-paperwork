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


@dataclass
class Tag:
    id: int
    location: Location
    name: str

    @classmethod
    def from_dict(cls, data):
        dd2 = data.copy()
        del dd2["location"]

        location = Location(**data["location"])
        return cls(**dd2, location=location)


# ┌────────────────────────────────────────┐
# │ Data table                             │
# └────────────────────────────────────────┘

@dataclass
class DataTable_Cell:
    location: Location
    value: any

    @classmethod
    def from_dict(cls, data):
        dd2 = data.copy()
        del dd2["location"]

        return cls(**dd2,
            location = Location(**data["location"])
        )

@dataclass
class DataTable_Row:
    id: int
    location: Location
    cells: List[DataTable_Cell]

    @classmethod
    def from_dict(cls, data):
        dd2 = data.copy()
        del dd2["location"]
        del dd2["cells"   ]

        return cls(**dd2,
            location = Location(**data["location"]),
            cells    = [DataTable_Cell.from_dict(x) for x in data["cells"]]
        )

    def simplify(self):
        """
        Helper function that iterates through the row data
        """

        return (map(lambda x: x.value, self.cells))

@dataclass
class DataTable:
    location: Location
    rows: List[DataTable_Row]

    @classmethod
    def from_dict(cls, data):
        dd2 = data.copy()
        del dd2["location"]
        del dd2["rows"    ]

        return cls(**dd2,
            location = Location(**data["location"]),
            rows     = [DataTable_Row.from_dict(x) for x in data["rows"]]
        )

    def simplify(self):
        """
        Helper function that returns the table data as tuples.
        """

        return tuple(map(lambda x: x.simplify(), self.rows))


# ┌────────────────────────────────────────┐
# │ Steps                                  │
# └────────────────────────────────────────┘

@dataclass
class Step:
    id: int
    keyword: str
    location: Location
    text: str
    dataTable: List[any] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict):
        # Copy data, parse location
        dd2 = data.copy()
        del dd2["location"]

        location  = Location(**data["location"])
        dataTable = None

        if "dataTable" in data:
            del dd2["dataTable"]
            dataTable = DataTable.from_dict(data["dataTable"])

        return cls(**dd2,
            location  = location,
            dataTable = dataTable
        )


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
        # Copy data and remove processed fields
        dd2   = data.copy()
        del dd2["steps"   ]
        del dd2["location"]
        del dd2["tags"    ]

        # Process specific data fields
        location = Location(**data["location"])
        steps    = [Step.from_dict(step_desc) for step_desc in data["steps"]]
        tags     = [Tag.from_dict(tag_desc)   for tag_desc  in data["tags" ]]

        # Create Scenario object
        return cls(**dd2, location=location, steps=steps, tags=tags)


# ┌────────────────────────────────────────┐
# │ Feature                                │
# └────────────────────────────────────────┘

@dataclass
class Feature:
    keyword: str
    location: Location
    name: str
    description: str
    language: str
    tags: List[Tag]

    children: List[any]

    @classmethod
    def from_dict(cls, data):
        # Copy data and remove processed fields
        dd2 = data.copy()
        del dd2["children"]
        del dd2["location"]
        del dd2["tags"    ]

        # Process tags and location
        location = Location(**data["location"])
        tags     = [Tag.from_dict(tag_desc) for tag_desc in data["tags"]]

        # Process children
        def __process_child(c):
            if "scenario" in c:
                return Scenario.from_dict(c["scenario"])

        children = [__process_child(c) for c in data["children"]]

        # Return final item
        return cls(**dd2, location=location, tags=tags, children=children)
