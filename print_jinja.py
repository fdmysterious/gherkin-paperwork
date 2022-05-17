"""
┌─────────────────────────────────────────────────┐
│ Test generate stuff using Jinja template engine │
└─────────────────────────────────────────────────┘

 Florian Dupeyron
 May 2022
"""

from jinja2  import Template, Environment
from pathlib import Path

from tabulate import tabulate

from gherkin_paperwork.feature_file import (
    Feature,
    Scenario,
    Background,
    Example,
    Step
)

from gherkin_paperwork import feature_file

from gherkin_paperwork.node_visitor import NodeVisitor

# ┌────────────────────────────────────────┐
# │ Special filters for jinja template     │
# └────────────────────────────────────────┘

def is_scenario(sc):
    return isinstance(sc, Scenario)

def is_background(sc):
    return isinstance(sc, Background)

def examples_tabulate(tableHeader, tableBody):
    return tabulate(map(lambda x: x.simplify(), tableBody), tableHeader.simplify(), tablefmt="html")


# ┌────────────────────────────────────────┐
# │ Main program                           │
# └────────────────────────────────────────┘

if __name__ == "__main__":
    # Create jinja environment
    env = Environment()
    env.filters["is_scenario"]       = is_scenario
    env.filters["is_background"]     = is_background
    env.filters["examples_tabulate"] = examples_tabulate

    # Load template
    #template = Template(Path("template.jinja").read_text(), undefined=StrictUndefined)
    template = env.from_string(Path("template.jinja").read_text())

    # Load feature data
    feature = feature_file.from_file("test.feature")

    # Reformat parsed data using NodeVisitor

    # Print template
    print(template.render({"feature": feature}))
