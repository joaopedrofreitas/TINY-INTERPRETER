from Lexical.TokenType import TokenType
from Lexical.SymbolTable import SymbolTable
from Lexical.Lexeme import Lexeme

class Lexical:

    def __init__(self,arquivo):
        self.file_content= open(arquivo,'r')
        self.line=1
    def prox_Token(self) -> Lexeme:
        lex = Lexeme("",TokenType.END_OF_FILE,self.line)
        estado = 1
        while estado != 7 and estado != 8:
            c = self.file_content.read(1)
            match estado:
                case 1:
                    if c == ' ' or c == '\r' or c == '\t':
                        estado = 1
                    elif c == '\n':
                        self.line += 1
                        estado = 1
                    elif c == '#':
                        estado = 2
                    elif c == '=' or c == '<' or c == '>':
                        lex.token += c
                        estado = 3
                    elif c == '!':
                        lex.token += c
                        estado = 4
                    elif c == ';' or c == '+' or c == '-' or c == '*' or c == '/' or c == '%' or c=='^':
                        lex.token += c
                        estado = 7
                    elif c.isalpha() or c == '_':
                        lex.token += c
                        estado = 5
                    elif c.isdigit():
                        lex.token += c
                        estado = 6
                    elif c == '':
                        lex.type = TokenType.END_OF_FILE
                        estado = 8
                    else:
                        lex.token += c
                        lex.type = TokenType.INVALID_TOKEN
                        lex.line=self.line
                        estado = 8
                case 2:
                    if c == '\n':
                        self.line += 1
                        estado = 1
                    elif c == '':
                        lex.type = TokenType.END_OF_FILE
                        lex.line=self.line
                        estado = 8
                    else:
                        estado = 2
                case 3:
                    if c == '=':
                        lex.token += c
                        estado = 7
                    else:
                        self.file_content.seek(self.file_content.tell() - 1)
                        estado = 7
                case 4:
                    if c == '=':
                        lex.token += c
                    elif c == '':
                        lex.type = TokenType.UNEXPECTED_EOF
                        lex.line=self.line
                        estado = 8
                    else:
                        lex.type = TokenType.INVALID_TOKEN
                        lex.line=self.line
                        estado = 8
                case 5:
                    if c.isalpha() or c.isdigit() or c == '_':
                        lex.token += c
                        estado = 5
                    else:
                        self.file_content.seek(self.file_content.tell() - 1)
                        estado = 7
                case 6:
                    if c.isdigit():
                        lex.token += c
                        estado = 6
                    else:
                        self.file_content.seek(self.file_content.tell() - 1)
                        lex.type = TokenType.NUMBER
                        lex.line=self.line
                        estado = 8
                case _:
                    print(lex.token)
                    print(estado)
                    raise ValueError("Unreachable")

        if estado == 7:
            aux=SymbolTable()
            lex.type = aux.find(lex.token)
        return lex
        
                

                
                        


    
