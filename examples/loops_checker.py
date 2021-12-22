import ast
from base_checker import BaseChecker

class TooManyForLoopChecker(BaseChecker):
    def __init__(self, filename):
        super().__init__(filename)

    msg = "too many nested for loops"
    def visit_For(self, node, parent=True):
        if parent:
            self.current_loop_depth = 1
        elif type(node) == ast.For:
            self.current_loop_depth += 1
        

        if self.current_loop_depth < 3: 
            for child in node.body:
                if type(child) != ast.Assign:
                    self.visit_For(child, parent=False)

        if parent and self.current_loop_depth >= 3:
            self.violations.append((self.filename, node.lineno, self.msg))
            self.current_loop_depth = 0 

if __name__ == "__main__":
    loops_checker = TooManyForLoopChecker("../scripts/loops_used.py")
    loops_checker.check()
    loops_checker.report()