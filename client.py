# Kevin Torres Martínez - A01656257
# Juan Sebastían Rodríguez Galarza - A01656159
# Víctor Antonio Godínez Rodríguez - A01339529

from antlr4 import FileStream, ParseTreeWalker, CommonTokenStream
from antlr.CoolLexer import CoolLexer
from antlr.CoolParser import CoolParser

from listeners.declare import Declarations
from listeners.typecheck import Typecheck


def main():
  input_file = FileStream('./input/semantic/simplearith.cool')

  lexer = CoolLexer(input_file)
  parser = CoolParser(CommonTokenStream(lexer))
  tree = parser.program()

  walker = ParseTreeWalker()
  typecheck = Typecheck()
  # walker.walk(typecheck, tree)

  declare = Declarations()
  walker.walk(typecheck, tree)
  walker.walk(declare, tree)
  

main()
