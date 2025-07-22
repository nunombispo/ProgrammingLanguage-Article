from tokenizer import tokenize
from parser import Number, Identifier, BinaryOp, LetStatement, Parser, PrintStatement
from pprint import pprint

class Environment:
    def __init__(self):
        self.vars = {}

    def set_var(self, name, value):
        self.vars[name] = value

    def get_var(self, name):
        if name in self.vars:
            return self.vars[name]
        raise NameError(f"Variable '{name}' not defined")
    
class Interpreter:
    def __init__(self):
        self.env = Environment()

    def eval(self, node):
        if isinstance(node, Number):
            return node.value

        elif isinstance(node, Identifier):
            return self.env.get_var(node.name)

        elif isinstance(node, BinaryOp):
            left = self.eval(node.left)
            right = self.eval(node.right)
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                return left // right  # integer division
            else:
                raise RuntimeError(f"Unknown operator: {node.op}")

        elif isinstance(node, LetStatement):
            value = self.eval(node.value)
            self.env.set_var(node.name, value)

        elif isinstance(node, PrintStatement):
            value = self.eval(node.expr)
            print(value)

        else:
            raise RuntimeError(f"Unknown node: {node}")

if __name__ == "__main__":
    code = """
    let a = 10;
    let b = a + 20 * 2;
    print(b);
    """

    tokens = tokenize(code)
    pprint(tokens)
    parser = Parser(tokens)
    ast = parser.parse()
    pprint(ast)

    interpreter = Interpreter()
    for stmt in ast:
        interpreter.eval(stmt)