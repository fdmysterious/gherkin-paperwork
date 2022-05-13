"""
┌────────────────────────────────────────────┐
│ Generate simple markdown from feature file │
└────────────────────────────────────────────┘

 Florian Dupeyron
 May 2022
"""

from gherkin.parser                 import Parser
from gherkin_paperwork.feature_file import Feature, Scenario

from tabulate                       import tabulate
from textwrap                       import dedent

if __name__ == "__main__":
    # Parse feature file
    parser_output = Parser().parse("test.feature")

    # Generate structured view from parser output
    feature = Feature.from_dict(parser_output["feature"])

    # Generate markdown text:
    print(f"{feature.name}")
    print("=" * len(feature.name))

    if feature.description:
        print("")
        print(dedent(feature.description).strip())

    for sc in feature.children:
        if isinstance(sc, Scenario):
            print("")
            print(f"## **{sc.keyword.strip()}**: {sc.name}")
            if sc.description:
                print("")
                print(dedent(sc.description).strip())
            print("")
            # TODO # print examples
            
            print("_Procedure_:")
            print()
            for st in sc.steps:
                print(f"- _{st.keyword.strip()}_ {st.text}")
                if st.dataTable:
                    print()
                    data = st.dataTable.simplify()
                    print(tabulate(data, tablefmt="simple"))
                    print()
