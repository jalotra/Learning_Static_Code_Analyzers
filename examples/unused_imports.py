import ast

from collections import defaultdict
from base_checker import BaseChecker

class UnusedImportChecker(BaseChecker):
    def __init__(self, filename):
        super().__init__(filename)

        self.import_map = defaultdict(set)
        self.name_map = defaultdict(set)

    def _add_imports(self, node):
        for import_name in node.names:
            # Store only top-level module name ("os.path" -> "os").
            # We can't easily detect when "os.path" is used.
            name = import_name.name.partition(".")[0]
            self.import_map[self.filename].add((name, node.lineno))

    def visit_Import(self, node):
        self._add_imports(node)

    def visit_ImportFrom(self, node):
        self._add_imports(node)

    def visit_Name(self, node):
        # We only add those nodes for which a value is being read from.
        if isinstance(node.ctx, ast.Load):
            self.name_map[self.filename].add(node.id)

    def report(self):
        for path, imports in self.import_map.items():
            for name, line in imports:
                if name not in self.name_map[path]:
                    print(f"{path}:{line}: unused import '{name}'")

if __name__ == '__main__':
    unused_import_checker = UnusedImportChecker("../scripts/unused_imports.py")
    unused_import_checker.check()
    unused_import_checker.report()