# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#mctype.
    def visitMctype(self, ctx:MCParser.MctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primitive_type.
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#void_type.
    def visitVoid_type(self, ctx:MCParser.Void_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arr_pointer_type.
    def visitArr_pointer_type(self, ctx:MCParser.Arr_pointer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_decl.
    def visitVar_decl(self, ctx:MCParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#id_arr.
    def visitId_arr(self, ctx:MCParser.Id_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#idlist.
    def visitIdlist(self, ctx:MCParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#id_arrlist.
    def visitId_arrlist(self, ctx:MCParser.Id_arrlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_decl.
    def visitFunc_decl(self, ctx:MCParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_name.
    def visitFunc_name(self, ctx:MCParser.Func_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#param.
    def visitParam(self, ctx:MCParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#param_list.
    def visitParam_list(self, ctx:MCParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp1.
    def visitExp1(self, ctx:MCParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp2.
    def visitExp2(self, ctx:MCParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp3.
    def visitExp3(self, ctx:MCParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp4.
    def visitExp4(self, ctx:MCParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp5.
    def visitExp5(self, ctx:MCParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp6.
    def visitExp6(self, ctx:MCParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp7.
    def visitExp7(self, ctx:MCParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp8.
    def visitExp8(self, ctx:MCParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term.
    def visitTerm(self, ctx:MCParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcall.
    def visitFuncall(self, ctx:MCParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_exp.
    def visitList_exp(self, ctx:MCParser.List_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statements.
    def visitStatements(self, ctx:MCParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ifStm.
    def visitIfStm(self, ctx:MCParser.IfStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#doWhileStm.
    def visitDoWhileStm(self, ctx:MCParser.DoWhileStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#forStm.
    def visitForStm(self, ctx:MCParser.ForStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#breakStm.
    def visitBreakStm(self, ctx:MCParser.BreakStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continueStm.
    def visitContinueStm(self, ctx:MCParser.ContinueStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnStm.
    def visitReturnStm(self, ctx:MCParser.ReturnStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expStm.
    def visitExpStm(self, ctx:MCParser.ExpStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blockStm.
    def visitBlockStm(self, ctx:MCParser.BlockStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#literals.
    def visitLiterals(self, ctx:MCParser.LiteralsContext):
        return self.visitChildren(ctx)



del MCParser