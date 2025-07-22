from pprint import pprint
from tokenizer import tokenize

class Number:
    def __init__(self, value):
        self.value = int(value)

    def __repr__(self):
        return f"Number(value={self.value})"

class Identifier:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Identifier(name={self.name})"

class BinaryOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinaryOp(left={self.left}, op={self.op}, right={self.right})"

class LetStatement:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"LetStatement(name={self.name}, value={self.value})"

class PrintStatement:
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"PrintStatement(expr={self.expr})"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '')

    def eat(self, token_type):
        if self.current()[0] == token_type:
            self.pos += 1
        else:
            raise SyntaxError(f'Expected {token_type}, got {self.current()}')

    def parse(self):
        statements = []
        while self.current()[0] != 'EOF':
            if self.current()[0] == 'LET':
                statements.append(self.parse_let())
            elif self.current()[0] == 'PRINT':
                statements.append(self.parse_print())
            else:
                raise SyntaxError(f'Unexpected token: {self.current()}')
        return statements
    
    def parse_let(self):
        self.eat('LET')
        name = self.current()[1]
        self.eat('IDENT')
        self.eat('EQUALS')
        expr = self.parse_expression()
        self.eat('SEMICOLON')
        return LetStatement(name, expr)

    def parse_print(self):
        self.eat('PRINT')
        self.eat('LPAREN')
        expr = self.parse_expression()
        self.eat('RPAREN')
        self.eat('SEMICOLON')
        return PrintStatement(expr)
    
    def parse_expression(self):
        node = self.parse_term()
        while self.current()[0] in ('PLUS', 'MINUS'):
            op = self.current()[1]
            self.eat(self.current()[0])
            right = self.parse_term()
            node = BinaryOp(node, op, right)
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.current()[0] in ('TIMES', 'DIVIDE'):
            op = self.current()[1]
            self.eat(self.current()[0])
            right = self.parse_factor()
            node = BinaryOp(node, op, right)
        return node

    def parse_factor(self):
        token_type, token_value = self.current()
        if token_type == 'NUMBER':
            self.eat('NUMBER')
            return Number(token_value)
        elif token_type == 'IDENT':
            self.eat('IDENT')
            return Identifier(token_value)
        elif token_type == 'LPAREN':
            self.eat('LPAREN')
            expr = self.parse_expression()
            self.eat('RPAREN')
            return expr
        else:
            raise SyntaxError(f'Unexpected factor: {self.current()}')
        
if __name__ == "__main__":
    code = """
    let x = 5 + 2;
    print(x);
    """

    tokens = tokenize(code)
    parser = Parser(tokens)
    ast = parser.parse()

    pprint(ast)