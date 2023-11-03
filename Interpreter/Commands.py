from Interpreter.Expressions import *

class Command:
  def __init__(self, linha):
    self.linha = linha

  def execute():
    pass

class Assign_Command(Command):
  def __init__(self, linha, variable, expr):
    super().__init__(linha)
    self.variable = variable
    self.expr = expr

  def execute(self):
    valor = int(self.expr.execute())
    self.variable.setValue(valor)

class Blocks_Command(Command):
  def __init__(self, linha):
    super().__init__(linha)
    self.commands_list = []

  def addCommand(self, command_aux):
    self.commands_list.append(command_aux)

  def execute(self):
    for object in self.commands_list:
      object.execute()

class If_Command (Command):
  def __init__(self, linha, bool_expr, then_command, else_command):
    super().__init__(linha)
    self.bool_expr = bool_expr
    self.then_command = then_command
    self.else_command = else_command

  def execute(self):
    if self.bool_expr.execute():
      self.then_command.execute()
      
    else:
      if self.else_command:
        self.else_command.execute()

class Output_Command(Command):
  def __init__(self, linha, expr):
    super().__init__(linha)
    self.expr = expr

  def execute(self):
    print(self.expr.execute())

class While_Command(Command):
  def __init__(self, linha, BoolCondition, commands):
    super().__init__(linha)
    self.BoolCondition = BoolCondition
    self.commands = commands

  def execute(self):
    while self.BoolCondition.execute():
      self.commands.execute()