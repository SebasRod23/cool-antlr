from antlr.CoolListener import CoolListener
from antlr.CoolParser import CoolParser
from exceptions import *


class TreePrinter(CoolListener):
  def __init__(self, types={}):
    self.output = ""

    self.depth = 0
    self.types = types

    self.in_class = False
    self.in_method_or_attribute = False

    self.expressions = {
        'Atribute': 'AAttributeFeature',
        'Integer': 'AIntExpr',
        'String': 'AStrExpr',
        'Bool': 'ABoolExpr',
        'Object': 'AObjectExpr',
        'Assign': 'AAssignExpr',
        'Add': 'APlusExpr',
        'Sub': 'AMinusExpr',
        'Mult': 'AMultExpr',
        'Div': 'ADivExpr',
        'Block': 'AListExpr',
        'New': 'ANewExpr',
        'At': 'AAtExpr',
        'Call': 'ACallExpr',
        'Eq': 'AEqExpr',
        'Lt': 'ALtExpr',
        'Le': 'ALeExpr',
        'Not': 'ANotExpr',
        'Isvoid': 'Isvoid',
        'Let': 'ALetExpr',
        'Neg': 'ANegExpr',
        'Parens': 'ABranch',
        'Case': 'ACaseExpr',
        'List': 'List',
        'If': 'AIfExpr',
    }

  def enterEveryRule(self, ctx):
    ctx_name = type(ctx).__name__[:-7]
    ctx_name_to_print = type(ctx).__name__[:-7]

    if ctx_name in ('Base', 'Formal'):
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

    base_indent = "  |"
    quote_indent = "  `"
    indent = "     |" + base_indent * self.depth
    to_print = "%s- %s" % (indent, ctx_name_to_print)

    if ctx_name == 'Program':
      to_print = "\n  >- A%s" % ctx_name_to_print

    try:
      self.output += self.print_and_return("%s:%s" %
                                           (to_print, self.types[ctx]))
    except:
      self.output += self.print_and_return(to_print)

    # Print characteristics
    if ctx_name == 'Klass':
      indent += base_indent
      class_types = ctx.TYPE()
      if len(ctx.TYPE()) == 1:
        class_types.append('Object')

      for class_type in class_types:
        self.output += self.print_and_return("%s- %s" % (indent, class_type))
    elif ctx_name == 'Atribute':
      indent += base_indent
      self.output += self.print_and_return("%s- %s\n%s- %s" %
                                           (indent, ctx.ID(), indent, ctx.TYPE()))
    elif ctx_name in ('Method', 'Atribute'):
      indent += base_indent
      self.output += self.print_and_return("%s- %s" % (indent, ctx.ID()))
      for formal in ctx.formal():
        self.output += self.print_and_return("%s- AFormal" % (indent))
        self.output += self.print_and_return("%s%s- %s" %
                                             (indent, base_indent, formal.ID()))
        self.output += self.print_and_return("%s%s- %s" %
                                             (indent, quote_indent, formal.TYPE()))
      self.output += self.print_and_return("%s- %s" % (indent, ctx.TYPE()))
    elif ctx_name == 'Integer':
      indent += quote_indent
      self.output += self.print_and_return("%s- %s" % (indent, ctx.INTEGER()))
    elif ctx_name == 'String':
      indent += quote_indent
      self.output += self.print_and_return("%s- %s" %
                                           (indent, ctx.STRING().getText().replace('"', "")))
    elif ctx_name == 'Bool':
      indent += quote_indent
      self.output += self.print_and_return("%s- %s" %
                                           (indent, (ctx.FALSE() or ctx.TRUE())))
    elif ctx_name == 'New':
      indent += quote_indent
      self.output += self.print_and_return("%s- %s" % (indent, (ctx.TYPE())))
    elif ctx_name in ('Object', 'Assign', 'Call'):
      indent += quote_indent
      self.output += self.print_and_return("%s- %s" % (indent, ctx.ID()))
    elif ctx_name in ('Let'):
      indent += base_indent
      self.output += self.print_and_return("%s- %s\n%s- %s" %
                                           (indent, ctx.ID()[0], indent, ctx.TYPE()[0]))

  def print_and_return(self, text: str):
    print(text)
    return text

  def exitEveryRule(self, ctx):
    ctx_name = type(ctx).__name__[:-7]

    if ctx_name == "Klass":
      self.in_class = False
    elif ctx_name in ('Method', 'Atribute'):
      self.depth = self.depth - 1
      self.in_method_or_attribute = False
    elif ctx_name == "At":
      indent = "     |" + "  |" * (self.depth + 1)
      self.output += self.print_and_return("%s- %s" % (indent, ctx.ID()))
      self.depth = self.depth - 1
    elif ctx_name in self.expressions:
      self.depth = self.depth - 1

  def exitProgram(self, ctx: CoolParser.ProgramContext):
    self.print_and_return("\n")

  def get_output(self):
    return self.output
