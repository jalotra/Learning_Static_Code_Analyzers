# Checks list() usage instead of []
import ast
from base_checker import BaseChecker

class ListChecker(BaseChecker):
    def __init__(self, filemame):
        super().__init__(filemame)

    msg = "list() found instead of []"
    def visit_Call(self, node):
        function_id = getattr(node.func, 'id', None)
        if function_id is not None and function_id == 'list' and not node.args:
            self.violations.append((filemame, node.lineno, self.msg))

if __name__ == '__main__':
    filemame = "../scripts/list_used.py"
    list_checker = ListChecker(filemame)
    list_checker.check()
    list_checker.report()