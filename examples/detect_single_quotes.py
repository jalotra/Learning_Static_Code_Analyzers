import sys
import tokenize


class DoubleQuotesChecker:
    msg = "single quotes detected, use double quotes instead"
    def __init__(self):
        self.violations = []

    def find_violations(self, filename, tokens):
        for token_tuple in tokens:
            # print(token_type, token, line, col)
            token_type = token_tuple.type
            token = token_tuple.string
            (line, col) = token_tuple.start
            if (
                token_type == tokenize.STRING
                and (
                    token.startswith("'''")
                    or token.startswith("'")
                )
            ):
                print(token_tuple)
                self.violations.append((filename, line, col))

    def check(self, files):
        for filename in files:
            with tokenize.open(filename) as fd:
                tokens = tokenize.generate_tokens(fd.readline)
                self.find_violations(filename, tokens)

    def report(self):
        for violation in self.violations:
            filename, line, col = violation
            print(f"{filename}:{line}:{col}: {self.msg}")


if __name__ == '__main__':
    files = sys.argv[1:]
    checker = DoubleQuotesChecker()
    checker.check(files)
    checker.report()