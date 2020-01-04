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


    # Visit a parse tree produced by MCParser#decl.
    def visitDecl(self, ctx:MCParser.DeclContext):
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


    # Visit a parse tree produced by MCParser#id_var_list.
    def visitId_var_list(self, ctx:MCParser.Id_var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#id_var.
    def visitId_var(self, ctx:MCParser.Id_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_decl.
    def visitFunc_decl(self, ctx:MCParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_name.
    def visitFunc_name(self, ctx:MCParser.Func_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#param_list.
    def visitParam_list(self, ctx:MCParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#param.
    def visitParam(self, ctx:MCParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#literals.
    def visitLiterals(self, ctx:MCParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcall.
    def visitFuncall(self, ctx:MCParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_exp.
    def visitList_exp(self, ctx:MCParser.List_expContext):
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


    # Visit a parse tree produced by MCParser#statements.
    def visitStatements(self, ctx:MCParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_stm.
    def visitIf_stm(self, ctx:MCParser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#do_while_stm.
    def visitDo_while_stm(self, ctx:MCParser.Do_while_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_stm.
    def visitFor_stm(self, ctx:MCParser.For_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_stm.
    def visitBreak_stm(self, ctx:MCParser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_stm.
    def visitContinue_stm(self, ctx:MCParser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_stm.
    def visitReturn_stm(self, ctx:MCParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_stm.
    def visitExp_stm(self, ctx:MCParser.Exp_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_stm.
    def visitBlock_stm(self, ctx:MCParser.Block_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block.
    def visitBlock(self, ctx:MCParser.BlockContext):
        return self.visitChildren(ctx)



del MCParser