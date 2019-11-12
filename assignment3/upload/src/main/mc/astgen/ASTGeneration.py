
# ID :1710929

from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

def Flatten(lst):
    FlatList = []
    for i in lst:
       if type(i) == list: 
           FlatList.extend(i)
       else: 
           FlatList.append(i)
    return FlatList

class ASTGeneration(MCVisitor):


    # def visitProgram(self,ctx:MCParser.ProgramContext):
    #     numChild = ctx.getChildCount() - 1
    #     return Program(Flatten([self.visit(ctx.getChild(i)) for i in range(numChild)]))

    def visitProgram(self,ctx:MCParser.ProgramContext):
        return Program(Flatten([self.visit(x) for x in ctx.decl()]))

    def visitPrimitive_type(self,ctx:MCParser.Primitive_typeContext):
        if ctx.BOOLEAN():
            return BoolType()
        elif ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()

    def visitVoid_type(self,ctx:MCParser.Void_typeContext):
        if ctx.VOID():
            return VoidType()

    def visitArr_pointer_type(self,ctx:MCParser.Arr_pointer_typeContext):
        return ArrayPointerType(self.visit(ctx.primitive_type()))

    def visitVar_decl(self, ctx:MCParser.Var_declContext):
        typeID = self.visit(ctx.primitive_type())
        listID =self.visit(ctx.id_var_list())
        return [VarDecl(x[0],typeID) if len(x) == 1 else VarDecl(x[0],ArrayType(x[1],typeID)) for x in listID]

    def visitId_var_list(self, ctx:MCParser.Id_var_listContext):
        if ctx.id_var_list():
            return [self.visit(ctx.id_var())] + self.visit(ctx.id_var_list())
        else:
            return [self.visit(ctx.id_var())]


    def visitId_var(self, ctx:MCParser.Id_varContext):
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        else:     
            return [ctx.ID().getText(),int(ctx.INTLIT().getText())]

    def visitFunc_decl(self, ctx:MCParser.Func_declContext):
        return [FuncDecl(self.visit(ctx.func_name()),
                        self.visit(ctx.param_list()) if ctx.param_list() else [],
                        self.visit(ctx.mctype()),
                        self.visit(ctx.block_stm()))]
    
    def visitFunc_name(self, ctx:MCParser.Func_nameContext):
        return Id(ctx.ID().getText())

    def visitParam_list(self, ctx:MCParser.Param_listContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.param())] + self.visit(ctx.param_list())
        else:
            return [self.visit(ctx.param())]

    def visitParam(self, ctx:MCParser.ParamContext):
        typeID = self.visit(ctx.primitive_type())
        var_id = ctx.ID().getText()
        if ctx.getChildCount() == 2:
            return VarDecl(var_id,typeID)
        else:
            return VarDecl(var_id,ArrayPointerType(typeID))


    #-------------------------------------------
    #---------------EXPRESSION------------------
    #-------------------------------------------

    def visitExp(self, ctx:MCParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1())
        return BinaryOp(ctx.ASSIGN().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp()))

    def visitExp1(self, ctx:MCParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2())
        return BinaryOp(ctx.OR().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp2()))

    def visitExp2(self, ctx:MCParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        return BinaryOp(ctx.AND().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))

    def visitExp3(self, ctx:MCParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4(0))
        op = ctx.getChild(1).getText()
        return BinaryOp(op,self.visit(ctx.exp4(0)),self.visit(ctx.exp4(1)))

    def visitExp4(self, ctx:MCParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5(0))
        op = ctx.getChild(1).getText()
        return BinaryOp(op,self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))

    def visitExp5(self, ctx:MCParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        op = ctx.getChild(1).getText()
        return BinaryOp(op,self.visit(ctx.exp5()),self.visit(ctx.exp6()))

    def visitExp6(self, ctx:MCParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        op = ctx.getChild(1).getText()
        return BinaryOp(op,self.visit(ctx.exp6()),self.visit(ctx.exp7()))

    def visitExp7(self, ctx:MCParser.Exp7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp8())
        op = ctx.getChild(0).getText()
        return UnaryOp(op,self.visit(ctx.exp7()))

    def visitExp8(self, ctx:MCParser.Exp8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.term()) 
        return ArrayCell(self.visit(ctx.term()),self.visit(ctx.exp()))

    def visitTerm(self, ctx:MCParser.TermContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.exp())
        elif ctx.literals():
            return self.visit(ctx.literals())
        elif ctx.funcall():
            return self.visit(ctx.funcall())
        else : 
            return Id(ctx.ID().getText())
    
    def visitFuncall(self, ctx: MCParser.FuncallContext):
        return CallExpr(Id(ctx.ID().getText()),self.visit(ctx.list_exp())) if ctx.list_exp() else CallExpr(Id(ctx.ID().getText()),[])


    def visitList_exp(self, ctx: MCParser.List_expContext):
        return [self.visit(i) for i in ctx.exp()]
    
    def visitLiterals(self, ctx: MCParser.LiteralsContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.BOOL_LIT():
            return BooleanLiteral(True) if ctx.BOOL_LIT().getText() == 'true' else BooleanLiteral(False)
        else:
            return StringLiteral(ctx.STRINGLIT().getText())



    # ----------------------------------------------------
    # -------------------- STATEMENT ---------------------
    # ----------------------------------------------------

    def visitIf_stm(self, ctx: MCParser.If_stmContext):
        expr = self.visit(ctx.exp())
        if ctx.ELSE():
            return If(expr,self.visit(ctx.statements(0)),self.visit(ctx.statements(1)))
        return If(expr,self.visit(ctx.statements(0)))
     

    def visitDo_while_stm(self, ctx: MCParser.Do_while_stmContext):
        listStm = [self.visit(x) for x in ctx.statements()]
        expr = self.visit(ctx.exp())
        return Dowhile(listStm,expr)

    def visitFor_stm(self, ctx: MCParser.For_stmContext):
        exp1 = self.visit(ctx.exp(0))
        exp2 = self.visit(ctx.exp(1))
        exp3 = self.visit(ctx.exp(2))
        stmt = self.visit(ctx.statements())
        return For(exp1,exp2,exp3,stmt)

    def visitBreak_stm(self, ctx: MCParser.Break_stmContext):
        return Break()

    def visitContinue_stm(self, ctx: MCParser.Continue_stmContext):
        return Continue()

    def visitReturn_stm(self, ctx: MCParser.Return_stmContext):
        return Return(self.visit(ctx.exp())) if ctx.exp() else Return()

    def visitExp_stm(self, ctx: MCParser.Exp_stmContext):
        return self.visit(ctx.exp())

    def visitBlock_stm(self, ctx: MCParser.Block_stmContext):
        return Block(Flatten([self.visit(x) for x in ctx.block()])) 


    def visitBlock(self, ctx: MCParser.BlockContext):
        return self.visit(ctx.var_decl()) if ctx.var_decl() else self.visit(ctx.statements())   



