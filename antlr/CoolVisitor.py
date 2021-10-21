# Generated from c:\Users\sebas\Documents\Python\Compiladores\cool-antlr\antlr\Cool.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CoolParser import CoolParser
else:
    from CoolParser import CoolParser

# This class defines a complete generic visitor for a parse tree produced by CoolParser.

class CoolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CoolParser#program.
    def visitProgram(self, ctx:CoolParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#klass.
    def visitKlass(self, ctx:CoolParser.KlassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#method.
    def visitMethod(self, ctx:CoolParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#atribute.
    def visitAtribute(self, ctx:CoolParser.AtributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#formal.
    def visitFormal(self, ctx:CoolParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#add.
    def visitAdd(self, ctx:CoolParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#new.
    def visitNew(self, ctx:CoolParser.NewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#sub.
    def visitSub(self, ctx:CoolParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#mult.
    def visitMult(self, ctx:CoolParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#isvoid.
    def visitIsvoid(self, ctx:CoolParser.IsvoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#lt.
    def visitLt(self, ctx:CoolParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#while.
    def visitWhile(self, ctx:CoolParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#eq.
    def visitEq(self, ctx:CoolParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#call.
    def visitCall(self, ctx:CoolParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#div.
    def visitDiv(self, ctx:CoolParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#neg.
    def visitNeg(self, ctx:CoolParser.NegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#not.
    def visitNot(self, ctx:CoolParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#at.
    def visitAt(self, ctx:CoolParser.AtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#le.
    def visitLe(self, ctx:CoolParser.LeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#let.
    def visitLet(self, ctx:CoolParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#block.
    def visitBlock(self, ctx:CoolParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#if.
    def visitIf(self, ctx:CoolParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#case.
    def visitCase(self, ctx:CoolParser.CaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#base.
    def visitBase(self, ctx:CoolParser.BaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#assign.
    def visitAssign(self, ctx:CoolParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#parens.
    def visitParens(self, ctx:CoolParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#object.
    def visitObject(self, ctx:CoolParser.ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#integer.
    def visitInteger(self, ctx:CoolParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#string.
    def visitString(self, ctx:CoolParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#bool.
    def visitBool(self, ctx:CoolParser.BoolContext):
        return self.visitChildren(ctx)



del CoolParser