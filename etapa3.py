import sys
import unittest

from antlr4 import *
from antlr.CoolLexer import CoolLexer
from antlr.CoolParser import CoolParser
from other.tree import TreePrinter
from exceptions import *

from listeners.declarechecker import DeclareChecker
from listeners.typechecker import TypeChecker

from other.tree import TreePrinter


def parseAndCompare(caseName):
  parser = CoolParser(CommonTokenStream(
      CoolLexer(FileStream("input/semantic/%s.cool" % caseName))))
  tree = parser.program()
  walker = ParseTreeWalker()

  types = {}
  typecheck = Checker(types)
  declare = Declarations(types)
  tree_printer = TreePrinter(types)

  walker.walk(typecheck, tree)
  walker.walk(declare, tree)
  output = tree_printer.get_output()

  expected = output.split('\n')
  with open('./output/semantic/%s.cool' % caseName) as f:
    for line1, line2 in zip(f, expected):
      if line1[:-1] != line2:
        print("Diferencia!!! [%s]-[%s]" % (line1, line2))
        return False
  return True


class BaseTest(unittest.TestCase):
  def setUp(self):
    self.walker = ParseTreeWalker()


test_cases = ['simplearith',
              'basicclassestree',
              'expressionblock',
              'objectdispatchabort',
              'initwithself',
              'compare',
              'comparisons',
              'cycleinmethods',
              'letnoinit',
              'forwardinherits',
              'letinit',
              'newselftype',
              'basic',
              'overridingmethod',
              'letshadows',
              'neg',
              'methodcallsitself',
              'overriderenamearg',
              'isvoid',
              'overridingmethod3',
              'inheritsObject',
              'scopes',
              'letselftype',
              'if',
              'methodnameclash',
              'trickyatdispatch',
              'stringtest',
              'overridingmethod2',
              'simplecase',
              'assignment',
              'subtypemethodreturn',
              'dispatch',
              'io',
              'staticdispatch',
              'classes',
              'hairyscary',
              'cells',
              'list',
              ]

if __name__ == '__main__':
  methods = {}
  i = 0
  for test_case in test_cases:
    methods['test%d' % i] = lambda self: self.assertTrue(
        parseAndCompare(test_case))
    i = i+1
  CoolTests = type('CoolTests', (BaseTest,), methods)
  unittest.main()
