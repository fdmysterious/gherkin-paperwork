from gherkin.parser                 import Parser
from gherkin_paperwork.feature_file import Scenario, Step

from pprint                         import pprint

def parse_featf(fpath):
    parser = Parser()

    feature_file = parser.parse(fpath)
    scenario_0   = feature_file["feature"]["children"][0]["scenario"]

    sc_obj       = Scenario.from_dict(scenario_0)

    pprint(sc_obj)

if __name__ == "__main__":
    parse_featf("test.feature")
    parse_featf("test_fr.feature")
