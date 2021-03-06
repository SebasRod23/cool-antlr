# Kevin Torres Martínez - A01656257
# Juan Sebastían Rodríguez Galarza - A01656159
# Víctor Antonio Godínez Rodríguez - A01339529

from antlr4 import FileStream, ParseTreeWalker, CommonTokenStream
from antlr.CoolLexer import CoolLexer
from antlr.CoolParser import CoolParser

from listeners.declarechecker import DeclareChecker
from listeners.typechecker import TypeChecker

from other.tree import TreePrinter


def main():
  input_file = FileStream('./input/semantic/cells.cool')

  lexer = CoolLexer(input_file)
  parser = CoolParser(CommonTokenStream(lexer))
  tree = parser.program()

  walker = ParseTreeWalker()

  types = {}
  typecheck = Checker(types)
  declare = Declarations(types)
  tree_printer = TreePrinter(types)

  walker.walk(typecheck, tree)
  walker.walk(declare, tree)
  walker.walk(tree_printer, tree)

  # output = tree_printer.get_output()
  # expected = output.split('\n')


main()
