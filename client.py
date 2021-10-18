# Kevin Torres Martínez - A01656257
# Juan Sebastían Rodríguez Galarza - A01656159
# Víctor Antonio Godínez Rodríguez - A01339529

from antlr4 import FileStream, ParseTreeWalker, CommonTokenStream
from antlr.CoolLexer import CoolLexer
from antlr.CoolParser import CoolParser

from listeners.typecheck import Typecheck


def main():
  input_file = FileStream('./cool-test-files/test.cool')

  lexer = CoolLexer(input_file)
  parser = CoolParser(CommonTokenStream(lexer))
  tree = parser.program()

  walker = ParseTreeWalker()
  typecheck = Typecheck()
  walker.walk(typecheck, tree)


main()
