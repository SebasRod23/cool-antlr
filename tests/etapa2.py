# coding=utf-8
import sys
import unittest

from antlr4 import *
from antlr.CoolLexer import CoolLexer
from antlr.CoolParser import CoolParser
from exceptions import *


def parseCase(caseName):
  parser = CoolParser(CommonTokenStream(
      CoolLexer(FileStream("input/semantic/%s.cool" % caseName))))
  return parser.program()


class CoolTests(unittest.TestCase):
  def setUp(self):
    self.walker = ParseTreeWalker()

  def test1(self):
    '''
    Los tipos no coinciden en la asignación: una variable de tipo más especializado
    no puede asignarse a un objeto de un tipo más general.

    '''
    tree = parseCase("assignnoconform")
    with self.assertRaises(DoesNotConform):
      self.walker.walk(Listener(), tree)

  def test2(self):
    """
    Cuando se asigna moo a sound, no se sabe qué es moo.
    """
    tree = parseCase("attrbadinit")
    with self.assertRaises(UndeclaredIdentifier):
      self.walker.walk(Listener(), tree)

  def test3(self):
    """
    No es posible redefinir atributos en una subclase.
    """
    tree = parseCase("attroverride")
    with self.assertRaises(NotSupported):
      self.walker.walk(Listener(), tree)

  def test4(self):
    """
    Cuando se pasa manda llamar a foo en la línea 5, es de tipo A, 
    que no se puede asignar a una variable de tipo B (más específica).
    """
    tree = parseCase("badargs1")
    with self.assertRaises(DoesNotConform):
      self.walker.walk(Listener(), tree)

  def test5(self):
    """
    Sumar entero y string.
    """
    tree = parseCase("badarith")
    with self.assertRaises(TypeCheckMismatch):
      self.walker.walk(Listener(), tree)

  def test6(self):
    """
    No existe el método moo en un objeto de tipo Animal.
    """
    tree = parseCase("baddispatch")
    with self.assertRaises(MethodNotFound):
      self.walker.walk(Listener(), tree)

  def test7(self):
    """
    Error de tipos en la comparación (Int y String)
    """
    tree = parseCase("badequalitytest")
    with self.assertRaises(TypeCheckMismatch):
      self.walker.walk(Listener(), tree)

  def test8(self):
    """
    Error de tipos en la comparación (Int y Boolean)
    """
    tree = parseCase("badequalitytest2")
    with self.assertRaises(TypeCheckMismatch):
      self.walker.walk(Listener(), tree)

  def test9(self):
    """
    f recibe Int, no puede recibir Object.
    """
    tree = parseCase("badmethodcallsitself")
    with self.assertRaises(CallTypeCheckMismatch):
      self.walker.walk(Listener(), tree)

  def test10(self):
    """
    El método bar está en un tipo más especializado, no se puede usar @.
    """
    tree = parseCase("badstaticdispatch")
    with self.assertRaises(MethodNotFound):
      self.walker.walk(Listener(), tree)

  def test11(self):
    """
    Int no tiene método length.
    """
    tree = parseCase("badwhilebody")
    with self.assertRaises(MethodNotFound):
      self.walker.walk(Listener(), tree)

  def test12(self):
    """
    La primera expresión de while debe tener tipo Boolean.
    """
    tree = parseCase("badwhilecond")
    with self.assertRaises(TypeCheckMismatch):
      self.walker.walk(Listener(), tree)

  def test13(self):
    """
    Dos ramas de case tienen el mismo tipo.
    """
    tree = parseCase("caseidenticalbranch")
    with self.assertRaises(InvalidCase):
      self.walker.walk(Listener(), tree)

  def test14(self):
    """
    Dos parámetros con el mismo nombre en el método foo.
    """
    tree = parseCase("dupformals")
    with self.assertRaises(KeyError):
      self.walker.walk(Listener(), tree)

  def test15(self):
    """
    La primera expresión de while debe tener tipo Boolean.
    """
    tree = parseCase("letbadinit")
    with self.assertRaises(DoesNotConform):
      self.walker.walk(Listener(), tree)

  def test16(self):
    """
    Pruebas con el operador de conformidad.
    """
    tree = parseCase("lubtest")
    with self.assertRaises(DoesNotConform):
      self.walker.walk(Listener(), tree)

  def test17(self):
    """
    Heredar de una clase inexistente.
    """
    tree = parseCase("missingclass")
    with self.assertRaises(TypeNotFound):
      self.walker.walk(Listener(), tree)

  def test18(self):
    """
    Variable en otro scope.
    """
    tree = parseCase("outofscope")
    with self.assertRaises(UndeclaredIdentifier):
      self.walker.walk(Listener(), tree)

  def test19(self):
    """
    Redefinición de clase A.
    """
    tree = parseCase("redefinedclass")
    with self.assertRaises(ClassRedefinition):
      self.walker.walk(Listener(), tree)

  def test20(self):
    """
    Heredar de una clase inexistente.
    """
    tree = parseCase("returntypenoexist")
    with self.assertRaises(TypeNotFound):
      self.walker.walk(Listener(), tree)

  def test21(self):
    """
    No se puede hacer @ de A a B.
    """
    tree = parseCase("trickyatdispatch2")
    with self.assertRaises(MethodNotFound):
      self.walker.walk(Listener(), tree)

  def test22(self):
    """
    La clase que regresa el método->A es fija, y la definición de SELF_TYPE
    es variable.
    """
    tree = parseCase("selftypebadreturn")
    with self.assertRaises(TypeCheckMismatch):
      self.walker.walk(Listener(), tree)

  def test23(self):
    """
    Se intenta redefinir un método cambiando los parámetros.
    """
    tree = parseCase("overridingmethod4")
    with self.assertRaises(InvalidMethodOverride):
      self.walker.walk(Listener(), tree)

  def test24(self):
    """
    Se intenta cambiar la firma de un método.
    """
    tree = parseCase("signaturechange")
    with self.assertRaises(InvalidMethodOverride):
      self.walker.walk(Listener(), tree)


if __name__ == '__main__':
  unittest.main()
