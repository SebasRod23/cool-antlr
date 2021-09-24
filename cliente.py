import sys
from antlr.CoolLexer import *
from antlr.CoolParser import *
from antlr.CoolListener import *


from antlr4 import *

class Printer(CoolListener):
   def exitEveryRule(self, ctx: ParserRuleContext):
       print("<{}>".format(ctx.getText()))

       return super().exitEveryRule(ctx) 

def main():
    parser = CoolParser(CommonTokenStream(CoolLexer(FileStream("test.cool"))))
    tree = parser.program()
    printer = Printer()

    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()
