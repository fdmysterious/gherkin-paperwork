from gherkin.parser        import Parser
from pprint                import pprint


def print_parsed_file(fpath):
        parser        = Parser()
        feature_file  = parser.parse(str(fpath))

        pprint(feature_file)

if __name__ == "__main__":
    print_parsed_file("test.feature")
    print_parsed_file("test_fr.feature")
