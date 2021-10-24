from antlr.CoolListener import CoolListener
from antlr.CoolParser import CoolParser
from exceptions import *


class TreePrinter(CoolListener):
  def __init__(self, types={}):
    self.depth = 0
    self.types = types

    self.in_class = False
    self.in_method_or_attribute = False

    self.expressions = {'Atribute': 'AAttributeFeature',
                        'Integer': 'AIntExpr',
                        'String': 'AStrExpr',
                        'Bool': 'ABoolExpr',
                        'Object': 'AObjectExpr',
                        'Assign': 'AAssignExpr',
                        'Add': 'APlusExpr',
                        'Sub': 'AMinusExpr',
                        'Mult': 'AMultExpr',
                        'Div': 'ADivExpr',
                        'TODO': 'TODO',
                        }

  def enterEveryRule(self, ctx):
    ctx_name = type(ctx).__name__[:-7]
    ctx_name_to_print = type(ctx).__name__[:-7]

    if ctx_name == 'Base':
      return

    if ctx_name == 'Klass':
      self.in_class = True
      ctx_name_to_print = "AClassDecl"
    elif ctx_name == 'Method':
      self.depth = self.depth + 1
      self.in_method_or_attribute = True
      ctx_name_to_print = "AMethodFeature"
    elif ctx_name == 'Atribute':
      self.depth = self.depth + 1
      self.in_method_or_attribute = True
      ctx_name_to_print = "AAttributeFeature"
    elif ctx_name in self.expressions:
      self.depth = self.depth + 1
      ctx_name_to_print = self.expressions[ctx_name]

    indent = "     |" + "  |" * self.depth
    to_print = "%s- %s" % (indent, ctx_name_to_print)

    if ctx_name == 'Program':
      to_print = "\n  >- A%s" % ctx_name_to_print

    try:
      print("%s:%s" % (to_print, self.types[ctx]))
    except:
      print(to_print)

    # Print characteristics
    indent += "  |"
    if ctx_name == 'Klass':
      class_types = ctx.TYPE()
      if len(ctx.TYPE()) == 1:
        class_types.append('Object')

      for class_type in class_types:
        print("%s- %s" % (indent, class_type))
    elif ctx_name in ('Method', 'Atribute'):
      print("%s- %s\n%s- %s" % (indent, ctx.ID(), indent, ctx.TYPE()))
    elif ctx_name == 'Integer':
      print("%s- %s" % (indent, ctx.INTEGER()))
    elif ctx_name == 'String':
      print("%s- %s" % (indent, ctx.STRING().getText().replace('"', "")))
    elif ctx_name == 'Bool':
      print("%s- %s" % (indent, (ctx.FALSE() or ctx.TRUE())))
    elif ctx_name in ('Object', 'Assign'):
      print("%s- %s" % (indent, ctx.ID()))

  def exitEveryRule(self, ctx):
    ctx_name = type(ctx).__name__[:-7]

    if ctx_name == 'Klass':
      self.in_class = False
    elif ctx_name in ('Method', 'Atribute'):
      self.depth = self.depth - 1
      self.in_method_or_attribute = False
    elif ctx_name in self.expressions:
      self.depth = self.depth - 1

  def exitProgram(self, ctx: CoolParser.ProgramContext):
    print("\n")
