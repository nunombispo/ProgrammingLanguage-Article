# ProgrammingLanguage-Article

This project demonstrates a simple programming language pipeline in Python, including a tokenizer, parser, and interpreter.

## Features

- Tokenizes source code into tokens
- Parses tokens into an Abstract Syntax Tree (AST)
- Interprets the AST to execute code (supports variables, arithmetic, and print statements)

---

## 1. Tokenizer (`tokenizer.py`)

**Purpose:**
Converts source code (as a string) into a list of tokens.

**How to use:**

```bash
python tokenizer.py
```

**Example code:**

```python
let x = 5 + 2;
```

**Example output:**

```
[('LET', 'let'), ('IDENT', 'x'), ('EQUALS', '='), ('NUMBER', '5'), ('PLUS', '+'), ('NUMBER', '2'), ('SEMICOLON', ';')]
```

---

## 2. Parser (`parser.py`)

**Purpose:**
Takes a list of tokens and builds an Abstract Syntax Tree (AST) representing the program structure.

**How to use:**

```bash
python parser.py
```

**Example code:**

```python
let x = 5 + 2;
print(x);
```

**Example output:**

```
[LetStatement(name=x, value=BinaryOp(left=Number(value=5), op=+, right=Number(value=2))),
 PrintStatement(expr=Identifier(name=x))]
```

---

## 3. Interpreter (`interpreter.py`)

**Purpose:**
Executes the AST produced by the parser, evaluating expressions, managing variables, and printing output.

**How to use:**

```bash
python interpreter.py
```

**Example code:**

```python
let a = 10;
let b = a + 20 * 2;
print(b);
```

**Example output:**

```
[('LET', 'let'), ('IDENT', 'a'), ('EQUALS', '='), ('NUMBER', '10'), ('SEMICOLON', ';'), ...]
[LetStatement(name=a, value=Number(value=10)), LetStatement(name=b, value=BinaryOp(left=Identifier(name=a), op=+, right=BinaryOp(left=Number(value=20), op=*, right=Number(value=2)))), PrintStatement(expr=Identifier(name=b))]
50
```

---

## File Descriptions

- `tokenizer.py`: Tokenizes source code into tokens.
- `parser.py`: Parses tokens into an AST.
- `interpreter.py`: Interprets the AST and executes the program.

---

## Future Work

- Extend the language with more features (control flow, functions, etc.)
- Add error reporting and better diagnostics
