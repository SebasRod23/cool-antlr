from antlr.CoolParser import CoolParser
from antlr.CoolListener import CoolListener
from exceptions.exceptions import *


class Typecheck(CoolListener):

  def enterProgram(self, ctx:CoolParser.ProgramContext):
    # Initilize
    self.typesTable = {}
    self.inClass = False
    self.className = ''
    self.inMethod = False
    self.methodName = ''
    self.basicClasses = {'Int', 'String', 'Bool', 'Object', 'SELF_TYPE'}
    self.typesNotToInherit = {'Int', 'String', 'Bool', 'SELF_TYPE'}
  
  def exitProgram(self, ctx:CoolParser.ProgramContext):
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

        if method == 'main': hasMain = True

        if not params: continue
        for param in params:
          if param == 'self':
            raise SelfVariableException
          if params[param] == 'SELF_TYPE':
            raise SelftypeInvalidUseException
    
    if not hasMain: 
      raise NoMainException
    
    # If there are no exceptions, then save the types table for the next listener
    ctx.typesTable = self.typesTable
    

  def enterKlass(self, ctx:CoolParser.KlassContext):
    # Every time you enter a class, define the structure of the class dictionary
    self.inClass = True
    self.className = ctx.getChild(1).getText()
    self.typesTable[self.className] = {}
    self.typesTable[self.className]['attributes'] = {}
    self.typesTable[self.className]['methods'] = {}

    # Check if it inherits another class
    if ctx.getChild(2).getText() == 'inherits': 
      self.typesTable[self.className]['inherits'] = ctx.getChild(3).getText()
    else:
      self.typesTable[self.className]['inherits'] = None


  def enterAtribute(self, ctx: CoolParser.AtributeContext):
    self.typesTable[self.className]['attributes'][ctx.ID().getText()] = ctx.TYPE().getText()
  
  def exitKlass(self, ctx:CoolParser.KlassContext):
    self.className = ''
    self.inClass = False

  def enterMethod(self, ctx:CoolParser.MethodContext):
    # Every time you enter a  new method, define the structure of the dictionary
    self.inMethod = True
    self.methodName = ctx.ID().getText()
    self.typesTable[self.className]['methods'][self.methodName] = {'type':ctx.TYPE().getText()}
    self.typesTable[self.className]['methods'][self.methodName]['params'] = {}
    

  def exitMethod(self, ctx:CoolParser.MethodContext):
    self.inMethod = False
    self.methodName = ''

  def enterFormal(self, ctx:CoolParser.FormalContext):
    # Get the type and id for each formal parameter in a method
    if self.inMethod:
      self.typesTable[self.className]['methods'][self.methodName]['params'][ctx.ID().getText()]=ctx.TYPE().getText()
  
  def enterLet(self, ctx:CoolParser.LetContext):
    # Get the id for each let in a line
    for id in ctx.ID():
      let = id.getText()
      # Self cannot be redefine
      if let == 'self':
        raise SelfVariableException


  def enterAssign(self, ctx:CoolParser.AssignContext):
    # Get the id for the assign
    assign = ctx.ID().getText()
    # Self cannot be redefine
    if assign == 'self':
      raise SelfAssignmentException