from antlr.CoolListener import CoolListener
from antlr.CoolParser import CoolParser
from exceptions.exceptions import *


class Declarations(CoolListener):
  idTable = {}
  inClass = False
  hasMain = False
  inMain = False
  primitiveNames = {'Int', 'String', 'Bool', 'Object', 'SELF_TYPE'}

  # Exit a parse tree produced by CoolParser#program.
  def exitProgram(self, ctx:CoolParser.ProgramContext):
    print("\n")
    if not self.hasMain: raise NoMainException

  def exitAtribute(self, ctx: CoolParser.AtributeContext):
    self.idTable[ctx.ID().getText()] = ctx.TYPE().getText()

  def enterKlass(self, ctx:CoolParser.KlassContext):
    self.inClass = True
    className = ctx.getChild(1).getText()
    print(className)
    if className == 'Main': self.inMain = True
    elif className in self.primitiveNames: raise RedefineBasicClassException

  def exitKlass(self, ctx:CoolParser.KlassContext):
    self.inClass = False
    self.inMain = False

  def enterMethod(self, ctx:CoolParser.MethodContext):
    if self.inMain and ctx.ID().getText() == 'main': self.hasMain = True