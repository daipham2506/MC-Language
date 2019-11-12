
"""
    Modify by Pham Tan Dai
    MSSV : 1710929
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return 'MPType([' + ','.join(str(i) for i in self.partype) + "]" +',' + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    
    def __str__(self):
        return "Symbol(" + str(self.name) + ',' + str(self.mtype) + ')'

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType())),
    Symbol("putInt",MType([IntType()],VoidType())),
    Symbol("getFloat",MType([],FloatType())),
    Symbol("putFloat",MType([FloatType()],VoidType())),
    Symbol("putFloatLn",MType([FloatType()],VoidType())),
    Symbol("putBool",MType([BoolType()],VoidType())),
    Symbol("putBoolLn",MType([BoolType()],VoidType())),
    Symbol("putString",MType([StringType()],VoidType())),
    Symbol("putStringLn",MType([StringType()],VoidType())),
    Symbol("putLn",MType([],VoidType()))
    ]

    list_name_func_check_unreach = []
            
    
    def __init__(self,ast):
        self.ast = ast

    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)


    def checkRedeclared(self, kind, name, list_check):
        dupName = self.lookup(name, list_check, lambda x: x.name)
        if dupName is not None:
            raise Redeclared(kind, name)

    def visitProgram(self,ast,c):
        list_global = c[:]
        self.list_name_func_check_unreach = []
        for _decl in ast.decl:
            if type(_decl) is VarDecl:  # Variable declaration
                self.checkRedeclared(Variable(), _decl.variable, list_global)
                list_global += [Symbol(_decl.variable, _decl.varType)]
            else:  # Function declaration
                self.checkRedeclared(Function(), _decl.name.name, list_global)
                list_global += [Symbol(_decl.name.name, MType([x.varType for x in _decl.param], _decl.returnType))]
                if _decl.name.name != "main":
                    self.list_name_func_check_unreach += [_decl.name.name]

        list_global_func = list(filter(lambda x: type(x.mtype) is MType, list_global))
        res = self.lookup("main",list_global_func,lambda x: x.name)

        if res is not None :
            func_decl = filter(lambda x: type(x) is FuncDecl, ast.decl)
            [self.visit(x,list_global) for x in func_decl]
            # check unreachable function
            for name_func in self.list_name_func_check_unreach:
                raise UnreachableFunction(name_func)
        else:
            raise NoEntryPoint()

#--------------------------------------------------------------------------------------#
#----------------------------------------DECLARE---------------------------------------#
#--------------------------------------------------------------------------------------# 
        
    def visitFuncDecl(self,ast, c): 
        list_local = []
        isReturn = False
        for param in ast.param:
            self.checkRedeclared(Parameter(), param.variable, list_local)
            list_local += [Symbol(param.variable, param.varType)]
        # visit block of function
        for block_mem in ast.body.member:
            if isinstance(block_mem, VarDecl):
                self.visit(block_mem,list_local)
                list_local += [Symbol(block_mem.variable, block_mem.varType)]  
            else:    # type is Stmt
                # False in (c+list_local , False , Symbol) to check Break/Continue NotInLoop
                if self.visit(block_mem, (c+list_local , False , self.lookup(ast.name.name,c,lambda x: x.name)) ) is True:
                    isReturn = True

        if not isinstance(ast.returnType, VoidType):  
            if isReturn == False:
                raise FunctionNotReturn(ast.name.name) 

            
    def visitVarDecl(self,ast,c):  # Variable in Block Stmt without Block in FuncDecl
        self.checkRedeclared(Variable(),ast.variable,c)

#--------------------------------------------------------------------------------------#
#----------------------------------------STATEMENTS------------------------------------#
#--------------------------------------------------------------------------------------# 

    def visitBlock(self,ast, c): # Block Stmt without in FuncDecl
        list_local = []
        isReturn = False
        for block_mem in ast.member:
            if isinstance(block_mem, VarDecl):
                self.visit(block_mem,list_local)
                list_local += [Symbol(block_mem.variable, block_mem.varType)]  
            else:    # type is Stmt
                if self.visit(block_mem,(c[0]+list_local,c[1],c[2])) is True:
                    isReturn = True
                    
        return isReturn
        
    def visitIf(self,ast,c):
        # c : (List[Symbol], Inloop, Symbol_FuncDecl)
        exp = self.visit(ast.expr,c)    
        if type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        then_stmt = self.visit(ast.thenStmt,c)
        if ast.elseStmt :
            else_stmt =  self.visit(ast.elseStmt, c)
            if then_stmt is True and else_stmt is True:
                return True

    def visitFor(self,ast,c):
        # c : (List[Symbol], Inloop, Symbol_FuncDecl)
        exp1 = self.visit(ast.expr1,c)
        exp2 = self.visit(ast.expr2,c)
        exp3 = self.visit(ast.expr3,c)

        if not (type(exp1) is IntType and type(exp2) is BoolType and type(exp3) is IntType):
            raise TypeMismatchInStatement(ast)

        self.visit(ast.loop, (c[0],True,c[2]))


    def visitDowhile(self,ast,c):
        isReturn = False
        exp = self.visit(ast.exp,c)
        if not isinstance(exp, BoolType):
            raise TypeMismatchInStatement(ast)
        
        for stmt in ast.sl:
            if self.visit(stmt, (c[0], True, c[2])) is True:
                isReturn = True

        return isReturn


    def visitBreak(self,ast,c):
        # c[1] from FuncDec / doWhile / For
        if c[1] == False:   
            raise BreakNotInLoop(ast)
        

    def visitContinue(self,ast,c):
        # c[1] from FuncDec / doWhile / For
        if c[1] == False: 
            raise ContinueNotInLoop(ast)

    def visitReturn(self,ast,c):
        # c[2] is Symbol FuncDecl
        if ast.expr is None: # expr return is None
            if not isinstance(c[2].mtype.rettype,VoidType): # type(c[2]) is not VoidType with c[2] is return Type of Function
                raise TypeMismatchInStatement(ast)
        else:
            if isinstance(c[2].mtype.rettype, VoidType): # type(c[2]) is VoidType  AND  expr return is not None
                raise TypeMismatchInStatement(ast)  
            res = self.visit(ast.expr, c)  # res = expr return
            if isinstance(c[2].mtype.rettype, FloatType):
                if not isinstance(res, (FloatType, IntType)):
                    raise TypeMismatchInStatement(ast)

            elif isinstance(c[2].mtype.rettype, ArrayPointerType):
                if not isinstance(res, (ArrayPointerType,ArrayType)):
                    raise TypeMismatchInStatement(ast)
                else: # type(res) is ArrayPointerType or ArrayType
                    if type(res.eleType) is not type(c[2].mtype.rettype.eleType):
                        raise TypeMismatchInStatement(ast)
            
            elif type(c[2].mtype.rettype) is not type(res):
                raise TypeMismatchInStatement(ast)

        return True

#--------------------------------------------------------------------------------------#
#----------------------------------------EXPRESSION------------------------------------#
#--------------------------------------------------------------------------------------#

    def visitCallExpr(self, ast, c): 

        at_param = [self.visit(x,c) for x in ast.param]
        res = self.lookup(ast.method.name, c[0][::-1], lambda x: x.name);

        #check unreachable function:
        if res is not None :
            if c[2].name != ast.method.name: # c[2].name is function name
                if ast.method.name in self.list_name_func_check_unreach:  # check whether ast.method.name has delete yet.
                    self.list_name_func_check_unreach.remove(ast.method.name);

        if res is None or type(res.mtype) is not MType:
            raise Undeclared(Function(), ast.method.name)
    
        elif len(res.mtype.partype) != len(at_param):
            raise TypeMismatchInExpression(ast)

        for x in zip(res.mtype.partype, at_param):
            left = x[0]  # parameter of function declare
            right = x[1] # parameter of call expr
            if isinstance(left, FloatType):
                if not isinstance(right, (FloatType, IntType)):
                    raise TypeMismatchInExpression(ast)

            elif isinstance(left, ArrayPointerType):
                if not isinstance(right, (ArrayPointerType,ArrayType)):
                    raise TypeMismatchInExpression(ast)
                else: # type(right) is ArrayPointerType or ArrayType
                    if type(left.eleType) is not type(right.eleType):
                        raise TypeMismatchInExpression(ast)
            
            elif type(left) is not type(right):
                raise TypeMismatchInExpression(ast)  

        return res.mtype.rettype

    def visitBinaryOp(self,ast,c):
        expr_left = self.visit(ast.left, c)
        expr_right = self.visit(ast.right, c)
        op = ast.op
        type_left = type(expr_left)
        type_right = type(expr_right)

        if op == '=' and type(ast.left) not in [Id, ArrayCell] :
            raise NotLeftValue(ast)

        if type_left is IntType and type_right is IntType:
            if op in ["+","-","*","/","%","="]:
                return IntType()
            elif op in [">",">=","<","<=","==","!="]:
                return BoolType()

        elif type_left is FloatType and type_right in [FloatType, IntType]:
            if op in ["+","-","*","/","="]:
                return FloatType()
            elif op in [">",">=","<","<="]:
                return BoolType()

        elif type_left is IntType and type_right is FloatType:
            if op in ["+","-","*","/"]:
                return FloatType()
            elif op in [">",">=","<","<="]:
                return BoolType();
        
        elif type_left is BoolType and type_right is BoolType:
            if op in ["==","!=","&&","||","="]:
                return BoolType()

        elif type_left is StringType and type_right is StringType:
            if op == '=':
                return StringType()

        raise TypeMismatchInExpression(ast)

 

    def visitUnaryOp(self,ast,c):
        expr = self.visit(ast.body,c) 
        op = ast.op
        if op == '-':
            if type(expr) in [FloatType,IntType]:
                return expr
        elif op == '!':
            if type(expr) is BoolType:
                return BoolType();

        raise TypeMismatchInExpression(ast)

#--------------------------------------------------------------------------------------#
#----------------------------------------LHS-------------------------------------------#
#--------------------------------------------------------------------------------------# 

    def visitId(self,ast,c):

        res = self.lookup(ast.name, c[0][::-1], lambda x: x.name)

        if res is None or type(res.mtype) is MType:
            raise Undeclared(Identifier(),ast.name)

        return res.mtype

    def visitArrayCell(self,ast,c):
        at_arr = self.visit(ast.arr, c)
        at_idx = self.visit(ast.idx, c)
        if (isinstance(at_arr,ArrayType) or isinstance(at_arr,ArrayPointerType)) and isinstance(at_idx,IntType):
            return at_arr.eleType
        raise TypeMismatchInExpression(ast) 

#--------------------------------------------------------------------------------------#
#----------------------------------------LITERALS--------------------------------------#
#--------------------------------------------------------------------------------------#

    def visitIntLiteral(self,ast,c):
        return IntType()

    def visitFloatLiteral(self,ast,c):
        return FloatType()

    def visitStringLiteral(self,ast,c):
        return StringType()

    def visitBooleanLiteral(self,ast,c):
        return BoolType()







        



    


