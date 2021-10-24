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
  primitiveNames = {'Int', 'String', 'Bool', 'Object', 'SELF_TYPE'}
  classname = ""
  letTable = {'self'}

  def enterProgram(self, ctx: CoolParser.ProgramContext):
    # print(ctx.typesTable)
    pass
