from enum import Enum

class Expr: 
  def __init__(self,linha):
    self.linha = linha

  def execute():
    pass 

class BinaryIntExpr(Expr):
  Op = Enum('Op', ['ADD', 'SUB', 'MUL', 'DIV', 'MOD','POT'])

  OPERATOR_FUNCTIONS = {
    Op.ADD: lambda x, y: x + y,
    Op.SUB: lambda x, y: x - y,
    Op.MUL: lambda x, y: x * y,
    Op.DIV: lambda x, y: x // y,
    Op.MOD: lambda x, y: x % y,
    Op.POT: lambda x, y: x ** y,
  }

  def __init__(self, linha, left, operation, right):
    super().__init__(linha)
    self.left = left
    self.operation = operation
    self.right = right

  def execute(self):
    expr1 = int(self.left.execute())
    expr2 = int(self.right.execute())

    operator_func = self.OPERATOR_FUNCTIONS.get(self.operation)
    if operator_func:
      return operator_func(expr1, expr2)
      
    else:
      raise ValueError("Operador inválido")


class ConstBoolExpr (Expr):
  def __init__(self, linha, booleano):
    super().__init__(linha)
    self.booleano = booleano

  def execute(self):
    return self.booleano


class ConstIntExpr (Expr):
  def __init__(self, linha, valor):
    super().__init__(linha)
    self.valor = valor

  def execute(self):
    return self.valor

class NegIntExpr (Expr):
  def __init__(self, linha, int_expr):
    super().__init__(linha)
    self.int_expr = int_expr

  def execute(self):
    return -self.int_expr.execute()

class NotBoolExpr (Expr): 
  def __init__(self, linha, bool_expr):
    super().__init__(linha)
    self.bool_expr = bool_expr

  def execute(self):
    return not self.bool_expr.execute()

class ReadIntExpr(Expr):
  def __init__(self, linha):
    super().__init__(linha)

  def execute(self):
    while True:
      try:
        var = int(input())
        return var
        
      except ValueError:
        pass

class SingleBoolExpr (Expr):
  Op = Enum('Op', ['EQUAL','NOT_EQUAL','LOWER','LOWER_EQUAL','GREATER', 'GREATER_EQUAL'])

  OPERATOR_FUNCTIONS = {
    Op.EQUAL: lambda x, y: x == y,
    Op.NOT_EQUAL: lambda x, y: x != y,
    Op.LOWER: lambda x, y: x < y,
    Op.LOWER_EQUAL: lambda x, y: x <= y,
    Op.GREATER: lambda x, y: x > y,
    Op.GREATER_EQUAL: lambda x, y: x >= y,
  }

  def __init__(self, linha, left, logical_operator, right):
    super().__init__(linha)
    self.left = left
    self.right = right
    self.logical_operator = logical_operator

  def execute(self):
    expr1 = int(self.left.execute())
    expr2 = int(self.right.execute())

    operator_func = self.OPERATOR_FUNCTIONS.get(self.logical_operator)
    if operator_func:
        return operator_func(expr1, expr2)
    else:
        raise ValueError("Operador lógico inválido")


class Variable (Expr):
  variables_map = {}

  def __init__(self, nome):
    super().__init__(-1)
    self.nome = nome
    self.valor = 0

  def getVariavel(self, nome):
    var = self.variables_map.get(nome)

    if var is None:
      var = Variable(nome)
      self.variables_map[nome] = var

    return var

  def setValue(self, valor):
    self.valor = valor

  def execute(self):
    return self.valor