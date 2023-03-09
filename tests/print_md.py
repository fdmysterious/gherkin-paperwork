"""
┌────────────────────────────────────────────┐
│ Generate simple markdown from feature file │
└────────────────────────────────────────────┘

 Florian Dupeyron
 May 2022
"""

from gherkin.parser                 import Parser
from gherkin.dialect                import Dialect

from gherkin_paperwork.feature_file import Feature, Scenario

from tabulate                       import tabulate

if __name__ == "__main__":
    # Parse feature file
    parser_output = Parser().parse("test.feature")

    # Generate structured view from parser output
    feature = Feature.from_dict(parser_output["feature"])
    
    # Load dialect for feature
    dialect = Dialect.for_name(feature.language)

    # Generate markdown text:
    print(f"{feature.name}")
    print("=" * len(feature.name))

    if feature.description:
        print("")
        print(feature.description)

    for sc in feature.children:
        if isinstance(sc, Scenario):
            print("")
            print(f"## **{sc.keyword.strip()}**: {sc.name}")
            if sc.description:
                print("")
                print(sc.description)
            print("")
            # TODO # print examples
            
            print("_Procedure_:")
            print()

            ilvl = 0
            for st in sc.steps:
                if st.keyword.strip() in ("*", *dialect.and_keywords):
                    print(f"    - {dialect.and_keywords[1]} {st.text}")
                else:
                    print(f"- _{st.keyword.strip()}_ {st.text}")

                if st.dataTable:
                    print()
                    data = st.dataTable.simplify()
                    print(tabulate(data, tablefmt="simple"))
                    print()

            if sc.examples:
                for ex in sc.examples:
                    print()
                    print(f"### **{ex.keyword}**: {ex.name}")
                    if ex.description:
                        print()
                        print(ex.description)
                    print()
                    print(tabulate((
                        tuple(ex.tableHeader.simplify()),
                        *tuple(map(lambda x: x.simplify(), ex.tableBody))
                    )))
