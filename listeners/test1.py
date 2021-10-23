from antlr.CoolListener import CoolListener
from antlr.CoolParser import CoolParser
from exceptions.exceptions import *


class Declarations(CoolListener):
  idTable = {}
  inClass = False
  hasMain = False
  inMain = False
  primitiveNames = {'Int', 'String', 'Bool', 'Object', 'SELF_TYPE'}
  classname = ""
  letTable = {'self'}

  # Exit a parse tree produced by CoolParser#program.
  def exitProgram(self, ctx:CoolParser.ProgramContext):
    print("\n")
    if not self.hasMain: raise NoMainException

  def enterKlass(self, ctx:CoolParser.KlassContext):
    self.inClass = True
    self.className = ctx.getChild(1).getText()

    for i in range(0, ctx.getChildCount()):
      if ctx.getChild(i).getText() == 'inherits' and ctx.getChild(i+1).getText() in self.primitiveNames:
        raise InvalidInheritsException

    if self.className == 'Main': self.inMain = True
    elif self.className in self.primitiveNames: raise RedefineBasicClassException

  def exitKlass(self, ctx:CoolParser.KlassContext):
    self.inClass = False
    self.inMain = False
    self.className = ""
    self.letTable = {'self'}

  def enterAtribute(self, ctx:CoolParser.AtributeContext):
    if ctx.getChild(4).getText() == 'self': raise SelfAssignmentException
    elif ctx.getChild(0).getText() == 'self': raise SelfVariableException
    elif ctx.getChild(2).getText() == self.className: raise SelfVariableException

  def exitAtribute(self, ctx: CoolParser.AtributeContext):
    self.idTable[ctx.ID().getText()] = ctx.TYPE().getText()
    

  def enterMethod(self, ctx:CoolParser.MethodContext):
    if self.inMain and ctx.ID().getText() == 'main': self.hasMain = True

  def enterFormal(self, ctx:CoolParser.FormalContext):
    if ctx.TYPE().getText() == 'SELF_TYPE': raise SelftypeInvalidUseException

  def enterLet(self, ctx:CoolParser.LetContext):
    for id in ctx.ID():
      if id.getText() in self.letTable: raise SelfVariableException
      else: self.letTable.add(id.getText())