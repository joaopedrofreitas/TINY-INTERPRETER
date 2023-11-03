from Lexical.Lexical import Lexical
from Lexical.TokenType import TokenType
from Lexical.SymbolTable import SymbolTable
from Interpreter.SyntaticAnalysis import Syntatic

TokenLst=[]
a_lex = Lexical('Examples/if.tiny')
lex =  a_lex.prox_Token()
TokenLst.append(lex)
#print(lex.token, lex.type)

while lex.type != TokenType.END_OF_FILE and lex.type != TokenType.INVALID_TOKEN and lex.type != TokenType.UNEXPECTED_EOF:
    lex = a_lex.prox_Token()
    TokenLst.append(lex)#GUARDAR A LISTA DE TOKENS, COM INFORMAÇÕES DO TIPO E LINHA ONDE SÃO ENCONTRADOS
sintatico=Syntatic(TokenLst)
sintatico.Analise_S().execute()

    #print(f"TOKEN: {lex.token}  \t TYPE: {lex.type}")
