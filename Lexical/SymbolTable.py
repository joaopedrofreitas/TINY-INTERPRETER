from Lexical.TokenType import TokenType

class SymbolTable:

    Symbols: dict = {
        # simbolos
        ';': TokenType.SEMICOLON,
        '=': TokenType.ASSIGN,

        # operadores logicos
        '==': TokenType.EQUAL,
        '!=': TokenType.NOT_EQUAL,
        '<':  TokenType.LOWER,
        '<=': TokenType.LOWER_EQUAL,
        '>':  TokenType.GREATER,
        '>=': TokenType.GREATER_EQUAL,

        # operadores aritmeticos
        '+': TokenType.ADD,
        '-': TokenType.SUB,
        '*': TokenType.MUL,
        '/': TokenType.DIV,
        '%': TokenType.MOD,

        # palavras-chave
        'program': TokenType.PROGRAM,
        'while': TokenType.WHILE,
        'do': TokenType.DO,
        'done': TokenType.DONE,
        'if': TokenType.IF,
        'then': TokenType.THEN,
        'else': TokenType.ELSE,
        'output': TokenType.OUTPUT,
        'true': TokenType.TRUE,
        'false': TokenType.FALSE,
        'read': TokenType.READ,
        'not': TokenType.NOT,
    }

    def contains(self, token: str) -> bool:
        return token in self.Symbols

    def find(self, token: str) -> TokenType:
        if self.contains(token):
            return self.Symbols.get(token)
        else:
            return TokenType.VAR