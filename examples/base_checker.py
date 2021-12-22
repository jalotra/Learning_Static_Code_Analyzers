import sys
import tokenize
import ast
import os

class BaseChecker(ast.NodeVisitor):
    def __init__(self, filename : str):
        self.violations = []
        self.filename = filename
    
    def read_file(self, filename):
    # Simple Assertion 
        assert os.path.exists(filename) 
        with tokenize.open(filename) as fd:
            return fd.read()

    def check(self):
        tree = ast.parse(self.read_file(self.filename))
        self.visit(tree)

    def report(self):
        for violation in self.violations:
            filename, lineno, msg = violation
            print(f"{filename}:{lineno}: {msg}")

if __name__ == '__main__':
    files = sys.argv[1:]
    # checker = <CHECKER_NAME>()
    # checker.check(files)
    # checker.report()