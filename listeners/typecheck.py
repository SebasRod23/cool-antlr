from antlr.CoolParser import CoolParser
from antlr.CoolListener import CoolListener
from exceptions.exceptions import *


class Typecheck(CoolListener):
  def __init__(self, types={}):
    self.types = types
    self.var_table = {}

  def enterProgram(self, ctx: CoolParser.ProgramContext):
    # Initilize
    self.typesTable = {}
    self.inClass = False
    self.classTypes = {}
    self.className = ''
    self.inMethod = False
    self.methodName = ''
    self.attrs = {}
    self.basicClasses = {'Int', 'String', 'Bool', 'Object', 'SELF_TYPE'}
    self.typesNotToInherit = {'Int', 'String', 'Bool', 'SELF_TYPE'}

  def exitProgram(self, ctx: CoolParser.ProgramContext):
    # Check for exceptions
    hasMain = False
    for klass in self.typesTable:
      inherits = self.typesTable[klass]['inherits']
      attrs = self.typesTable[klass]['attributes']
      methods = self.typesTable[klass]['methods']

      if klass in self.basicClasses:
        raise RedefineBasicClassException

      if inherits in self.typesNotToInherit or inherits == klass:
        raise InvalidInheritsException

      for attr in attrs:
        if attr == 'self':
          raise SelfVariableException

      for method in methods:
        params = methods[method]['params']

        if method == 'main':
          hasMain = True

        if not params:
          continue
        for param in params:
          if param == 'self':
            raise SelfVariableException
          if params[param] == 'SELF_TYPE':
            raise SelftypeInvalidUseException

    if not hasMain:
      raise NoMainException

    # If there are no exceptions, then save the types table for the next listener
    ctx.typesTable = self.typesTable
    ctx.var_table = self.var_table
    ctx.classTypes = self.classTypes

  def enterKlass(self, ctx: CoolParser.KlassContext):
    # Every time you enter a class, define the structure of the class dictionary
    self.inClass = True
    self.className = ctx.getChild(1).getText()
    self.typesTable[self.className] = {}
    self.typesTable[self.className]['attributes'] = {}
    self.typesTable[self.className]['methods'] = {}
    self.attrs = {}

    if self.className in self.classTypes: raise ClassRedefinition

    # Check if it inherits another class
    if ctx.getChild(2).getText() == 'inherits':
      self.typesTable[self.className]['inherits'] = ctx.getChild(3).getText()
      self.classTypes[self.className] = ctx.getChild(3).getText()
      ctx.inherits = ctx.getChild(3).getText()
    else:
      self.typesTable[self.className]['inherits'] = None
      self.classTypes[self.className] = None
      ctx.inherits = None
    

  def enterAtribute(self, ctx: CoolParser.AtributeContext):
    self.typesTable[self.className]['attributes'][ctx.ID().getText()
                                                  ] = ctx.TYPE().getText()

    self.var_table[ctx.ID().getText()] = ctx.TYPE().getText()
    self.attrs[ctx.ID().getText()] = ctx.TYPE().getText()

  def exitKlass(self, ctx: CoolParser.KlassContext):
    self.className = ''
    self.inClass = False
    ctx.attrs = self.attrs

  def enterMethod(self, ctx: CoolParser.MethodContext):
    # Every time you enter a  new method, define the structure of the dictionary
    self.inMethod = True
    self.methodName = ctx.ID().getText()
    self.typesTable[self.className]['methods'][self.methodName] = {
        'type': ctx.TYPE().getText()}
    self.typesTable[self.className]['methods'][self.methodName]['params'] = {}
    self.types[ctx] = ctx.TYPE().getText()
    self.currParams = set()

  def exitMethod(self, ctx: CoolParser.MethodContext):
    self.inMethod = False
    self.methodName = ''
    for param in self.currParams:
      del self.var_table[param]

  def enterFormal(self, ctx: CoolParser.FormalContext):
    # Get the type and id for each formal parameter in a method
    if self.inMethod:
      self.typesTable[self.className]['methods'][self.methodName]['params'][ctx.ID().getText()] = ctx.TYPE().getText()
      self.var_table[ctx.ID().getText()] = ctx.TYPE().getText()
      if str(ctx.ID().getText()) in self.currParams: raise KeyError
      self.currParams.add(str(ctx.ID().getText()))

  def enterLet(self, ctx: CoolParser.LetContext):
    # Get the id for each let in a line
    for id in ctx.ID():
      let = id.getText()
      # Self cannot be redefine
      if let == 'self':
        raise SelfVariableException

  def enterAssign(self, ctx: CoolParser.AssignContext):
    # Get the id for the assign
    assign = ctx.ID().getText()
    # Self cannot be redefine
    if assign == 'self':
      raise SelfAssignmentException

  def exitInteger(self, ctx: CoolParser.IntegerContext):
    ctx.type = "Int"
    self.types[ctx] = "Int"

  def exitString(self, ctx: CoolParser.StringContext):
    ctx.type = "String"
    self.types[ctx] = "String"

  def exitBool(self, ctx: CoolParser.BoolContext):
    ctx.type = "Bool"
    self.types[ctx] = "Bool"

  def exitBase(self, ctx: CoolParser.BaseContext):
    # print(ctx.getChild(0).getText())
    if hasattr(ctx.getChild(0), 'type'):
      ctx.type = ctx.getChild(0).type
      self.types[ctx] = self.types[ctx.getChild(0)]

  def exitObject(self, ctx: CoolParser.ObjectContext):
    if ctx.ID().getText() == "self":
      self.types[ctx] = self.className
    else: 
      ctx.type = self.var_table[ctx.ID().getText()]
      self.types[ctx] = self.var_table[ctx.ID().getText()]

  def exitMult(self, ctx: CoolParser.MultContext):
    if self.types[ctx.expr(0)] == "Int" and self.types[ctx.expr(1)] == "Int":
      self.types[ctx] = "Int"
    else:
      raise Exception("Type error in Mult")

  def exitDiv(self, ctx: CoolParser.DivContext):
    if self.types[ctx.expr(0)] == "Int" and self.types[ctx.expr(1)] == "Int":
      self.types[ctx] = "Int"
    else:
      raise TypeCheckMismatch

  def exitAdd(self, ctx: CoolParser.AddContext):
    # if ctx.expr(0).type == "Int" and ctx.expr(1).type == "Int":
    #    ctx.type = "Int"

    if self.types[ctx.expr(0)] == "Int" and self.types[ctx.expr(1)] == "Int":
      self.types[ctx] = "Int"
    else:
      raise TypeCheckMismatch
  
  def exitEq(self, ctx:CoolParser.EqContext):
    if self.types[ctx.expr(0)] == "Int" and self.types[ctx.expr(1)] == "Int":
      self.types[ctx] = "Int"
    else:
      raise TypeCheckMismatch

  def exitSub(self, ctx: CoolParser.SubContext):
    if self.types[ctx.expr(0)] == "Int" and self.types[ctx.expr(1)] == "Int":
      self.types[ctx] = "Int"

  def exitAssign(self, ctx:CoolParser.AssignContext):
    self.types[ctx] = self.types[ctx.expr()]

  def exitNew(self, ctx:CoolParser.NewContext):
    self.types[ctx] = ctx.TYPE()

  def exitBlock(self, ctx:CoolParser.BlockContext):
    lastExpr = ctx.expr(len(ctx.expr())-1)
    self.types[ctx] = self.types[lastExpr]

  def exitWhile(self, ctx:CoolParser.WhileContext):
    if not self.types[ctx.expr(0)] == "Bool":
      raise TypeCheckMismatch
    # TODO: Add type to while

  def exitNeg(self, ctx:CoolParser.NegContext):
    self.types[ctx] = 'Int'

  def enterCase(self, ctx:CoolParser.CaseContext):
    types = set()
    size = len(ctx.TYPE())
    for i in range(size):
      if ctx.TYPE(i).getText() in types: raise InvalidCase
      types.add(ctx.TYPE(i).getText())
      self.var_table[ctx.ID(i).getText()] = ctx.TYPE(i).getText()

    # self.types[ctx] = types

  # def exitCall(self, ctx:CoolParser.CallContext):
    # if str(ctx.getChild(1)) == '.':
      # Something with the first expr
      # Something with the rest of the call
      # for expr in ctx.expr()[1:]:
        
  