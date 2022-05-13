from gherkin.parser                 import Parser
from gherkin_paperwork.feature_file import Scenario, Step


if __name__ == "__main__":
    parser = Parser()

    feature_file = parser.parse("test.feature")
    scenario_0   = feature_file["feature"]["children"][0]["scenario"]

    sc_obj       = Scenario.from_dict(scenario_0)

    print(sc_obj)
