from Interpreter.Commands import *
from Interpreter.Expressions import *
from Lexical.Lexical import Lexical
from Lexical.TokenType import TokenType
from Lexical.SymbolTable import SymbolTable

class Syntatic:
    def __init__(self, TokenLst: list):
        self.Token=None
        self.Index=0
        self.TokenList=TokenLst
    
    def advance(self,expectedToken):
        #print(f"EXPECTED: {expectedToken}\n")
        if self.TokenList[self.Index].type == expectedToken:
            #print(f"TOKEN: {self.TokenList[self.Index].token} \t TYPE: {self.TokenList[self.Index].type}")
            self.Index += 1
            if self.Index < self.size:
                self.Token = self.TokenList[self.Index]
        else:
            #print(f"TOKEN: {self.TokenList[self.Index].token} \t TYPE: {self.TokenList[self.Index].type}")
            print("ERRO, TOKEN NÃO ESPERADO1\n")

    def ProxToken(self):
        self.Index+=1
        self.Token=self.TokenList[self.Index].token
    def Analise_S(self):
        self.size=len(self.TokenList)
        comandos=self.get_CmdList()
        self.advance(TokenType.END_OF_FILE)
        return comandos
    def get_CmdList(self):
        if self.Index == 0:
            self.advance(TokenType.PROGRAM)
        line=int(self.TokenList[self.Index].line)
        blocos=Blocks_Command(line)
        comando=self.procCmd()
        blocos.addCommand(comando)
        lista=[TokenType.VAR, TokenType.OUTPUT, TokenType.IF, TokenType.WHILE]

        while self.TokenList[self.Index].type in lista:
            comando=self.procCmd()
            blocos.addCommand(comando)
        return blocos
    def procCmd(self):
        program_command = None
        if self.TokenList[self.Index].type == TokenType.VAR:
            program_command = self.procAssign()
        elif self.TokenList[self.Index].type == TokenType.OUTPUT:
            program_command = self.procOutput()
        elif self.TokenList[self.Index].type == TokenType.IF:
            program_command = self.procIf()
        elif self.TokenList[self.Index].type == TokenType.WHILE:
            program_command = self.procWhile()
        else:
            print("ERRO, TOKEN NÃO ESPERADO\n")

        self.advance(TokenType.SEMICOLON)
        return program_command 

    def procAssign(self):
        var = self.procVar()
        linha = int(self.TokenList[self.Index].line)
        self.advance(TokenType. ASSIGN)
        expr = self.procIntExpr()
        
        return Assign_Command (linha, var, expr)

  
    def procOutput(self):
        self.advance(TokenType.OUTPUT)
        linha = int(self.TokenList[self.Index].line)
        expr = self.procIntExpr()
        
        return Output_Command (linha, expr)

    
    def procIf(self):
        self.advance(TokenType. IF)
        linha = int(self.TokenList[self.Index].line)

        bool_expr = self.procBoolExpr()
        self.advance(TokenType. THEN)

        then_command = self.get_CmdList()
        else_command = None

        if self. TokenList[self.Index].type == TokenType. ELSE:
            self.ProxToken()
            else_command = self.get_CmdList()

            self.advance(TokenType. DONE)
        
        return If_Command(linha, bool_expr, then_command, else_command)

    
    def procWhile(self):
        self.advance(TokenType. WHILE)
        linha = int(self.TokenList[self.Index].line)

        bool_expr = self.procBoolExpr()

        self.advance(TokenType. DO)

        program_command = self.get_CmdList()
        self.advance(TokenType. DONE)

        return While_Command(linha, bool_expr, program_command)

    def procBoolExpr(self):
        if self. TokenList[self.Index].type == TokenType. FALSE:
            self.ProxToken()
            linha = int(self.TokenList[self.Index].line)
            
            return ConstBoolExpr(linha, False)

        elif self. TokenList[self.Index].type == TokenType. TRUE:
            self.ProxToken()
            linha = int(self.TokenList[self.Index].line)
        
            return ConstBoolExpr(linha, False)
        
        elif self. TokenList[self.Index].type == TokenType. NOT:
            self.ProxToken()
            linha = int(self.TokenList[self.Index].line)
            bool_expr = self.procBoolExpr()
        
            return NotBoolExpr (linha, bool_expr)

        else:
            linha = int(self.TokenList[self.Index].line)
            expr_left = self.procIntTerm()
            log_op = None

        if self.TokenList[self.Index].type == TokenType.EQUAL:
            log_op = SingleBoolExpr.Op.EQUAL
            self.ProxToken()

        elif self.TokenList[self.Index].type == TokenType.NOT_EQUAL:       
            log_op = SingleBoolExpr.Op.NOT_EQUAL
            self.ProxToken()

        elif self.TokenList[self.Index].type ==TokenType.LOWER: 
            log_op = SingleBoolExpr.Op.LOWER
            self.ProxToken()

        elif self.TokenList[self.Index].type == TokenType.LOWER_EQUAL:
            log_op = SingleBoolExpr.Op.LOWER_EQUAL
            self.ProxToken()

        elif self.TokenList[self.Index].type == TokenType.GREATER: 
            log_op = SingleBoolExpr.Op.GREATER
            self.ProxToken()

        elif self.TokenList[self.Index].type == TokenType.GREATER_EQUAL: 
            log_op = SingleBoolExpr.Op.GREATER_EQUAL
            self.ProxToken()

        else:
            print("ERRO, TOKEN NÃO ESPERADO\n")

        expr_right = self.procIntTerm()
        
        return SingleBoolExpr (linha, expr_left, log_op, expr_right)

    
    def procIntExpr(self):
        boolean = False 
        left = None
        op = None

        if self.TokenList[self.Index].type == TokenType.ADD:
            self.ProxToken()

        elif self.TokenList[self.Index].type == TokenType.SUB:
            self.ProxToken()
            boolean = True

        if boolean:    
            linha = int(self.TokenList[self.Index].line)
            int_expr = self.procIntTerm()
            left = NegIntExpr(linha, int_expr)

        else:
            linha = int(self.TokenList[self.Index].line)
            left = self.procIntTerm()

        if self.TokenList[self.Index].type == TokenType.ADD:
            op = BinaryIntExpr.Op.ADD
            self.ProxToken()
            right = self.procIntTerm()
            left = BinaryIntExpr (linha, left, op, right)

        elif self.TokenList[self.Index].type == TokenType.SUB:
            op = BinaryIntExpr.Op.SUB
            self.ProxToken()
            right = self.procIntTerm()
            left = BinaryIntExpr (linha, left, op, right)

        elif self.TokenList[self.Index].type == TokenType.MUL:
            op = BinaryIntExpr.Op.MUL
            self.ProxToken()
            right = self.procIntTerm()
            left = BinaryIntExpr (linha, left, op, right)

        elif self.TokenList[self.Index].type == TokenType.DIV:
            op = BinaryIntExpr.Op.DIV
            self.ProxToken()
            right = self.procIntTerm()
            left = BinaryIntExpr (linha, left, op, right)

        elif self.TokenList[self.Index].type == TokenType.MOD:
            op = BinaryIntExpr.Op.MOD
            self.ProxToken()
            right = self.procIntTerm()
            left = BinaryIntExpr (linha, left, op, right)

        return left

    def procIntTerm(self):
        if self.TokenList[self.Index].type == TokenType.VAR:
            return self.procVar()

        elif self.TokenList[self.Index].type == TokenType.NUMBER:
            return self.procConst()

        else:
            self.advance(TokenType.READ)
            linha = int(self.TokenList[self.Index].line)
            
            return ReadIntExpr(linha)

    def procVar(self):
        name = self.TokenList[self.Index].token
        self.advance(TokenType.VAR)

        return Variable (name).getVariavel(name)

    def procConst(self):
        name = self.TokenList[self.Index].token
        self.advance(TokenType. NUMBER)
        linha = int(self.TokenList[self.Index].line)
        num = int(name)

        return ConstIntExpr (linha, num)
