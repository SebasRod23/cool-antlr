from antlr.CoolListener import CoolListener
from antlr.CoolParser import CoolParser
from exceptions.exceptions import *


class Declarations(CoolListener):
  def __init__(self, types={}):
    self.types = types

  idTable = {}
  inClass = False
  hasMain = False
  inMain = False
  basicClasses = {'Int', 'String', 'Bool', 'Object', 'SELF_TYPE'}
  classname = ""

  def enterProgram(self, ctx: CoolParser.ProgramContext):
    self.typesTable = ctx.typesTable
    self.var_table = ctx.var_table
    self.classTypes = ctx.classTypes

  def isMoreGeneral(self, exprType, declType):
    if exprType == declType: return False
    temp = declType
    while temp: 
      if str(self.classTypes[temp]) == str(exprType):
        return True
      temp = self.classTypes[temp]
    return False

  def enterAssign(self, ctx:CoolParser.AssignContext):
    # print(self.types[ctx])
    if self.isMoreGeneral(self.types[ctx], self.var_table[ctx.ID().getText()]):
      raise DoesNotConform
    

  def enterKlass(self, ctx: CoolParser.KlassContext):
    if ctx.inherits:
      for attr in ctx.attrs:
        if attr in self.typesTable[ctx.inherits]["attributes"]:
          raise NotSupported
    if ctx.inherits and not ctx.inherits in self.classTypes: raise TypeNotFound
  
  def enterMethod(self, ctx:CoolParser.MethodContext):
    if ctx.TYPE().getText() not in self.basicClasses and ctx.TYPE() not in self.classTypes.items(): raise TypeNotFound

  # def enterCall(self, ctx:CoolParser.CallContext):
    # print(ctx.ID())