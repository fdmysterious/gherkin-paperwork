from gherkin.token_scanner import TokenScanner
from gherkin.token_matcher import TokenMatcher

from gherkin.parser        import Parser
from gherkin.errors        import ParserError

from pathlib               import Path


def print_parsed_file(fpath):
        parser        = Parser()
        feature_file  = parser.parse(str(fpath))

        print(feature_file)
        print(type(feature_file))

if __name__ == "__main__":
    print_parsed_file("test.feature")
    print_parsed_file("test_fr.feature")

