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

  def exitString(self, ctx: CoolParser.StringContext):
    ctx.type = "String"
    self.typeTable[ctx] = "String"

  def exitBool(self, ctx: CoolParser.BoolContext):
    ctx.type = "Boolean"
    self.typeTable[ctx] = "Boolean"

  def exitBase(self, ctx: CoolParser.BaseContext):
    # print(ctx.getChild(0).getText())

    ctx.type = ctx.getChild(0).type
    self.typeTable[ctx] = self.typeTable[ctx.getChild(0)]

  def exitObject(self, ctx: CoolParser.ObjectContext):
    ctx.type = self.varTable[ctx.ID().getText()]
    self.typeTable[ctx] = self.varTable[ctx.ID().getText()]

  def exitMult(self, ctx: CoolParser.MultContext):
    if self.typeTable[ctx.expr(0)] == "Int" and self.typeTable[ctx.expr(1)] == "Int":
      self.typeTable[ctx] = "Int"
    else:
      raise Exception("Type error in Mult")

  def exitDiv(self, ctx: CoolParser.DivContext):
    if self.typeTable[ctx.expr(0)] == "Int" and self.typeTable[ctx.expr(1)] == "Int":
      self.typeTable[ctx] = "Int"
    else:
      raise Exception("Type error in Div")

  def exitAdd(self, ctx: CoolParser.AddContext):
    # if ctx.expr(0).type == "Int" and ctx.expr(1).type == "Int":
    #    ctx.type = "Int"

    if self.typeTable[ctx.expr(0)] == "Int" and self.typeTable[ctx.expr(1)] == "Int":
      self.typeTable[ctx] = "Int"
    else:
      raise Exception("Type error in Add")

  def exitSub(self, ctx: CoolParser.SubContext):
    if self.typeTable[ctx.expr(0)] == "Int" and self.typeTable[ctx.expr(1)] == "Int":
      self.typeTable[ctx] = "Int"
    else:
      raise Exception("Type error in Sub")

  def exitLt(self, ctx: CoolParser.LtContext):
    if self.typeTable[ctx.expr(0)] == "Boolean" and self.typeTable[ctx.expr(1)] == "Boolean":
      self.typeTable[ctx] = "Boolean"
    else:
      raise Exception("Type error in Lt")

  def exitLe(self, ctx: CoolParser.LeContext):
    if self.typeTable[ctx.expr(0)] == "Boolean" and self.typeTable[ctx.expr(1)] == "Boolean":
      self.typeTable[ctx] = "Boolean"
    else:
      raise Exception("Type error in Le")

  def exitEq(self, ctx: CoolParser.EqContext):
    if self.typeTable[ctx.expr(0)] == "Boolean" and self.typeTable[ctx.expr(1)] == "Boolean":
      self.typeTable[ctx] = "Boolean"
    else:
      raise Exception("Type error in Eq")

  def exitNot(self, ctx: CoolParser.NotContext):
    if self.typeTable[ctx.expr(0)] == "Boolean" and self.typeTable[ctx.expr(1)] == "Boolean":
      self.typeTable[ctx] = "Boolean"
    else:
      raise Exception("Type error in Not")
