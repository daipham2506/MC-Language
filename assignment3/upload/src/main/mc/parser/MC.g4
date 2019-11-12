
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




program : decl+ EOF;
// program: (var_decl | func_decl)+ EOF;

decl: var_decl | func_decl;

mctype : primitive_type | void_type | arr_pointer_type ;

primitive_type: INT | FLOAT | BOOLEAN | STRING ;

void_type: VOID;

arr_pointer_type: primitive_type LSB RSB;


//2.1

var_decl: primitive_type id_var_list SEMI ;

id_var_list : id_var COMMA id_var_list | id_var ;

id_var : ID (LSB INTLIT RSB)? ;



// 2.2

func_decl: mctype func_name LB param_list? RB block_stm;

func_name: ID ;

param_list: param COMMA param_list | param ;

param: primitive_type ID (LSB RSB)? ;


// exp

// Literal
literals : INTLIT | FLOAT_LIT | BOOL_LIT | STRINGLIT ;

funcall: ID LB list_exp? RB ;

list_exp: exp(COMMA exp)* ;

exp: exp1 ASSIGN exp
    |   exp1;
exp1: exp1 OR exp2
    |   exp2;
exp2: exp2 AND exp3
    |   exp3;
exp3: exp4 EQUAL exp4
    |   exp4 NOT_EQUAL exp4
    |   exp4;
exp4: exp5 LESS_THAN exp5
    |   exp5 LESS_THAN_EQUAL exp5
    |   exp5 GREATER_THAN exp5
    |   exp5 GREATER_THAN_EQUAL exp5
    |   exp5;
exp5: exp5 ADD exp6
    |   exp5 SUB exp6
    |   exp6;
exp6: exp6 DIV exp7
    |   exp6 MUL exp7
    |   exp6 MOD exp7
    |   exp7;
exp7: SUB exp7
    |   NOT exp7
    |   exp8;

exp8: term LSB exp RSB | term;

term: LB exp RB | literals | ID | funcall;




// STATEMENT

statements: if_stm | do_while_stm | for_stm | break_stm | continue_stm | return_stm | exp_stm | block_stm ;

if_stm: IF LB exp RB statements (ELSE statements)? ;

do_while_stm: DO statements+ WHILE exp SEMI ;

for_stm: FOR LB exp SEMI exp SEMI exp RB statements ;

break_stm: BREAK SEMI ;

continue_stm: CONTINUE SEMI ;

return_stm: RETURN exp? SEMI ;

exp_stm: exp SEMI ;

block_stm: LP block* RP ;

block : var_decl | statements;

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




INTLIT: [0-9]+ ;

BOOL_LIT: 'true' | 'false' ;

FLOAT_LIT: NUMBER EXPONENT? ;

STRINGLIT : UNCLOSE_STRING '"'  {self.text = self.text[1:-1]};

ID: [a-zA-Z_][0-9a-zA-Z_]* ;

WS : [ \f\t\r\b\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' ('\\' [btrnf\\"] | ~[\b\t\r\n\f\\"])*  ;
ILLEGAL_ESCAPE: UNCLOSE_STRING '\\' ~[btnfr\\"]  ;
ERROR_CHAR: .  ;



