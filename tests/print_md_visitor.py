"""
┌──────────────────────────────────┐
│ Print markdown using NodeVisitor │
└──────────────────────────────────┘

 Florian Dupeyron
 May 2022
"""

from gherkin.dialect                import Dialect
from gherkin.parser                 import Parser

from gherkin_paperwork.node_visitor import NodeVisitor
from gherkin_paperwork.feature_file import (
    Feature,
    Scenario,
    Step,
    Example
)

from gherkin_paperwork.markdown     import Markdown_NodeVisitor

from io                             import (StringIO)
from tabulate                       import tabulate


# ┌────────────────────────────────────────┐
# │ Markdown node visitor                  │
# └────────────────────────────────────────┘

#class MD_NodeVisitor(NodeVisitor):
#    def __init__(self, io):
#        super().__init__()
#        self.io = io
#
#    # ┌────────────────────────────────────────┐
#    # │ Process nodes stuff                    │
#    # └────────────────────────────────────────┘
#    
#    def _process_feature(self, ft: Feature, **kwargs):
#        print(f"{ft.name}", file=self.io)
#        print("=" * len(ft.name), file=self.io)
#
#        if ft.description:
#            print("", file=self.io)
#            print(ft.description, file=self.io)
#
#
#    def _process_scenario(self, sc: Scenario, **kwargs):
#        print("", file=self.io)
#        print(f"## _{sc.keyword.strip()}_: {sc.name}", file=self.io)
#        if sc.description:
#            print("", file=self.io)
#            print(sc.description, file=self.io)
#        print("", file=self.io)
#        print("_Procedure_: ", file=self.io)
#        print("", file=self.io)
#
#
#    def _process_step(self, st: Step, **kwargs):
#        # Process step text
#        st_text = st.text.replace("<", "`<").replace(">", ">`")
#
#        # Print step text
#        if st.keyword in ("*", *kwargs["dialect"].and_keywords):
#            print(f"\t- _{kwargs['dialect'].and_keywords[1]}_ {st_text}", file=self.io)
#        else:
#            print(f"- _{st.keyword.strip()}_ {st_text}", file=self.io)
#
#        # Print step datatable
#        if st.dataTable:
#            print("", file=self.io)
#            data = st.dataTable.simplify()
#            print(tabulate(data, tablefmt="grid"), file=self.io)
#            print("", file=self.io)
#
#    def _process_example(self, ex: Example, **kwargs):
#        print("", file=self.io)
#        print(f"### _{ex.keyword}_: {ex.name}", file=self.io)
#        if ex.description:
#            print("", file=self.io)
#            print(ex.description, file=self.io)
#        print("", file=self.io)
#        print(tabulate(
#            tuple(map(lambda x: x.simplify(), ex.tableBody)),
#            ex.tableHeader.simplify(),
#            tablefmt="grid"
#        ), file=self.io)


# ┌────────────────────────────────────────┐
# │ Test program                           │
# └────────────────────────────────────────┘

if __name__ == "__main__":
    feature_file = Parser().parse("test.feature")["feature"]
    feature      = Feature.from_dict(feature_file)

    with open("output.md", "w") as fhandle:
        nv = Markdown_NodeVisitor(fhandle)
        nv.visit(feature)
