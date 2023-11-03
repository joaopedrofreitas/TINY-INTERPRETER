from Lexical.TokenType import TokenType
class Lexeme:
    def __init__(self, token: str, type: TokenType, line: int) -> None:
        self.token = token
        self.type = type
        self.line=line