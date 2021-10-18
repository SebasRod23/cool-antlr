from antlr.CoolParser import CoolParser
from antlr.CoolListener import CoolListener


class Typecheck(CoolListener):
  typeTable = {}
  varTable = {}

  def enterAtribute(self, ctx: CoolParser.AtributeContext):
    self.varTable[ctx.ID().getText()] = ctx.TYPE().getText()

  def exitInteger(self, ctx: CoolParser.IntegerContext):
    ctx.type = "Int"
    self.typeTable[ctx] = "Int"

  def exitBase(self, ctx: CoolParser.BaseContext):
    print(ctx.getChild(0).getText())

    ctx.type = ctx.getChild(0).type

    self.typeTable[ctx] = self.typeTable[ctx.getChild(0)]

  def exitObject(self, ctx: CoolParser.ObjectContext):
    ctx.type = self.varTable[ctx.ID().getText()]
    self.typeTable[ctx] = self.varTable[ctx.ID().getText()]

  def exitAdd(self, ctx: CoolParser.AddContext):
    # if ctx.expr(0).type == "Int" and ctx.expr(1).type == "Int":
    #    ctx.type = "Int"

    left = ctx.expr(0)
    right = ctx.expr(1)
    if self.typeTable[ctx.expr(0)] == "Int" and self.typeTable[ctx.expr(1)] == "Int":
      self.typeTable[ctx] = "Int"
    else:
      raise Exception("Type error")
