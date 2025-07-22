import re

# Define token types and regex patterns
TOKEN_TYPES = [
    ('LET',      r'let'),
    ('PRINT',    r'print'),
    ('NUMBER',   r'\d+'),
    ('IDENT',    r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('EQUALS',   r'='),
    ('PLUS',     r'\+'),
    ('MINUS',    r'-'),
    ('TIMES',    r'\*'),
    ('DIVIDE',   r'/'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('SEMICOLON',r';'),
    ('SKIP',     r'[ \t]+'),   # ignore spaces and tabs
    ('NEWLINE',  r'\n'),
]

def tokenize(code):
    tokens = []
    index = 0

    while index < len(code):
        match = None
        for token_type, pattern in TOKEN_TYPES:
            regex = re.compile(pattern)
            match = regex.match(code, index)
            if match:
                text = match.group(0)
                if token_type != 'SKIP' and token_type != 'NEWLINE':
                    tokens.append((token_type, text))
                index = match.end(0)
                break
        if not match:
            raise SyntaxError(f'Unexpected character: {code[index]}')
    return tokens

# Test the tokenizer
if __name__ == "__main__":
    code = "let x = 5 + 2;"
    print(tokenize(code))