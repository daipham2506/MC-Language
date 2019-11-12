
// ID : 1710929

grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}



program : (var_decl | func_decl)+ EOF;

mctype : primitive_type | void_type | arr_pointer_type ;

primitive_type: INT | FLOAT | BOOLEAN | STRING ;

void_type: VOID;

arr_pointer_type: primitive_type LSB RSB;



//2.1

var_decl: primitive_type (idlist | id_arrlist) (COMMA (id_arrlist | idlist) )* SEMI ;

id_arr: ID LSB INTLIT RSB;

idlist : ID(COMMA ID)*;

// idlist : ID COMMA idlist | ID ;

id_arrlist: id_arr(COMMA id_arr)*;


// 2.2

func_decl: mctype func_name LB param_list? RB blockStm;

func_name: ID ;

param: primitive_type ID (LSB RSB)? ;

param_list: param (COMMA param)* ;


// EXPRESSION

exp: exp1 ASSIGN exp 
    | exp1 ;

exp1: exp1 OR exp2
    | exp2 ;

exp2: exp2 AND exp3
    | exp3 ;

exp3: exp4 (EQUAL | NOT_EQUAL) exp4
    | exp4 ;

exp4: exp5 (LESS_THAN | LESS_THAN_EQUAL | GREATER_THAN | GREATER_THAN_EQUAL) exp5
    | exp5;

exp5: exp5 (ADD | SUB) exp6
    | exp6 ;

exp6: exp6 ( MUL | DIV | MOD) exp7
    | exp7;

exp7: (SUB | NOT) exp7 
    | exp8;

exp8: term LSB exp RSB | term;

term: LB exp RB | literals | ID | funcall;

funcall: ID LB list_exp? RB ;

list_exp: exp(COMMA exp)* ;

// list_exp: (exp list_exp_tail)? ;
// list_exp_tail: (COMMA exp list_exp_tail)?;



// STATEMENT

statements: ifStm | doWhileStm | forStm | breakStm | continueStm | returnStm | expStm | blockStm ;

ifStm: IF LB exp RB statements (ELSE statements)? ;

doWhileStm: DO statements+ WHILE exp SEMI ;

forStm: FOR LB exp SEMI exp SEMI exp RB statements ;

breakStm: BREAK SEMI ;

continueStm: CONTINUE SEMI ;

returnStm: RETURN exp? SEMI ;

expStm: exp SEMI ;

blockStm: LP (var_decl | statements)* RP ;


// Fragment

fragment E: [eE];
fragment NUMBER: ( [0-9]* ('.')? [0-9]+) | ( [0-9]+ ('.')? [0-9]*);
fragment EXPONENT: E '-'? [0-9]+ ;

// Keyword

/* boolean break continue else for 
ﬂoat if int return void do while true false string */

BOOLEAN: 'boolean';
BREAK: 'break';
CONTINUE: 'continue';
ELSE: 'else';
FOR: 'for';
FLOAT: 'float';
IF: 'if';
INT: 'int';
RETURN: 'return';
VOID: 'void';
DO: 'do';
WHILE: 'while';
// TRUE: 'true';
// FALSE: 'false';
STRING: 'string';


// Comment

COMMENT_1: '/*' .*? '*/' -> skip ;
COMMENT_2: '//' ~[\r\n]* -> skip ;




// Operator

ADD: '+';

SUB: '-';

MUL: '*';

DIV: '/';

NOT: '!';

MOD: '%';

AND: '&&';

OR: '||';

NOT_EQUAL: '!=';

EQUAL: '==';

ASSIGN: '=';

LESS_THAN: '<';

GREATER_THAN: '>';

LESS_THAN_EQUAL: '<=';

GREATER_THAN_EQUAL: '>=';

// Separators

LSB: '[';

RSB: ']';

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

COMMA: ',';


// Literal
literals : INTLIT | FLOAT_LIT | BOOL_LIT | STRINGLIT ;

INTLIT: [0-9]+ ;

BOOL_LIT: 'true' | 'false' ;

FLOAT_LIT: NUMBER EXPONENT? ;

STRINGLIT : UNCLOSE_STRING '"'  {self.text = self.text[1:-1]};

ID: [a-zA-Z_][0-9a-zA-Z_]* ;

WS : [ \f\t\r\b\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' ('\\' [btrnf\\"] | ~[\b\t\r\n\f\\"])*  ;
ILLEGAL_ESCAPE: UNCLOSE_STRING '\\' ~[btnfr\\"]  ;
ERROR_CHAR: .  ;



