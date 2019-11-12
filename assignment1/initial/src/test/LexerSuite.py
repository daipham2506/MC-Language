import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier_my_name(self):
        self.assertTrue(TestLexer.checkLexeme("Pham Tan Dai","Pham,Tan,Dai,<EOF>",101))
    
    def test_identifier_simple(self):
        self.assertTrue(TestLexer.checkLexeme("abc12a","abc12a,<EOF>",102))
    
    def test_identifier_simple_2(self):
        self.assertTrue(TestLexer.checkLexeme("FunCtion123","FunCtion123,<EOF>",103))

    def test_identifier_simple_3(self):
        self.assertTrue(TestLexer.checkLexeme("_abc1e-5","_abc1e,-,5,<EOF>",104))
    
    def test_identifier_special(self):
        self.assertTrue(TestLexer.checkLexeme("_123_a__","_123_a__,<EOF>",105))

    def test_identifier_wrong(self):
        self.assertTrue(TestLexer.checkLexeme("1_variable","1,_variable,<EOF>",106))
   
    def test_identifier_wrong_2(self):
        self.assertTrue(TestLexer.checkLexeme("++abc","+,+,abc,<EOF>",107))
    
    def test_identifier_wrong_3(self):
        self.assertTrue(TestLexer.checkLexeme("abc+-","abc,+,-,<EOF>",108))
    
    def test_identifier_wrong_4(self):
        self.assertTrue(TestLexer.checkLexeme("wrong+.3E-2","wrong,+,.3E-2,<EOF>",109))
    
    def test_identifier_wrong_5(self):
        self.assertTrue(TestLexer.checkLexeme("*(a)*","*,(,a,),*,<EOF>",110))

    # INTEGER

    def test_integer(self):
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",111))

    def test_integer_1(self):
        self.assertTrue(TestLexer.checkLexeme("123-10e","123,-,10,e,<EOF>",112))

    def test_integer_2(self):
        self.assertTrue(TestLexer.checkLexeme("_a_123_ 123","_a_123_,123,<EOF>",113))

    def test_integer_3(self):
        self.assertTrue(TestLexer.checkLexeme("-10a3","-,10,a3,<EOF>",114))

    def test_integer_4(self):
        self.assertTrue(TestLexer.checkLexeme("123-10","123,-,10,<EOF>",115))

    # COMMENT

    def test_cmt_line(self):
        self.assertTrue(TestLexer.checkLexeme("// a\n b","b,<EOF>",116))
    
    def test_cmt_line_2(self):
        self.assertTrue(TestLexer.checkLexeme("// **10e7","<EOF>",117))

    def test_cmt_line_3(self):
        self.assertTrue(TestLexer.checkLexeme("// Dai \t */","<EOF>",118))

    def test_cmt_line_4(self):
        self.assertTrue(TestLexer.checkLexeme("// DAI \n","<EOF>",119))

    def test_cmt_block(self):
        self.assertTrue(TestLexer.checkLexeme("/*abc\n\n%#\/\n*/","<EOF>",120))

    def test_cmt_block_2(self):
        self.assertTrue(TestLexer.checkLexeme("/*\t\t\y\n\f\s*/","<EOF>",121))

    def test_cmt_block_wrong(self):
        self.assertTrue(TestLexer.checkLexeme("/* string","/,*,string,<EOF>",122))

    def test_cmt_block_wrong_2(self):
        self.assertTrue(TestLexer.checkLexeme("ab-1e10*/","ab,-,1e10,*,/,<EOF>",123))

    def test_cmt_block_3(self):
        self.assertTrue(TestLexer.checkLexeme("/* // this is a block cmt*/","<EOF>",124))


    # FLOAT

    def test_float(self):
        self.assertTrue(TestLexer.checkLexeme("1.2e-2abc","1.2e-2,abc,<EOF>",125))

    def test_float_2(self):
        self.assertTrue(TestLexer.checkLexeme("1E0","1E0,<EOF>",126))

    def test_float_with_dot_after(self):
        self.assertTrue(TestLexer.checkLexeme("-1.","-,1.,<EOF>",127))

    def test_float_with_dot_before(self):
        self.assertTrue(TestLexer.checkLexeme(".10",".10,<EOF>",128))

    def test_float_with_exponent_1(self):
        self.assertTrue(TestLexer.checkLexeme("10e-7","10e-7,<EOF>",129))

    def test_float_with_exponent_2(self):
        self.assertTrue(TestLexer.checkLexeme("-4E4","-,4E4,<EOF>",130))

    def test_float_with_fraction_exponent_1(self):
        self.assertTrue(TestLexer.checkLexeme("10.123e-7","10.123e-7,<EOF>",131))

    def test_float_with_fraction_exponent_2(self):
        self.assertTrue(TestLexer.checkLexeme(".123E-4",".123E-4,<EOF>",132))

    def test_float_with_fraction_exponent_wrong_1(self):
        self.assertTrue(TestLexer.checkLexeme("123.1E-12+","123.1E-12,+,<EOF>",133))
    
    def test_float_with_fraction_exponent_wrong_2(self):
        self.assertTrue(TestLexer.checkLexeme("123.o1E+12.1e2","123.,o1E,+,12.1e2,<EOF>",134))

    def test_float_wrong_case1(self):
        self.assertTrue(TestLexer.checkLexeme("123.e","123.,e,<EOF>",135))
    
    def test_float_wrong_case2(self):
        self.assertTrue(TestLexer.checkLexeme("123.123e-13abcd","123.123e-13,abcd,<EOF>",136))

    def test_float_wrong_case3(self):
        self.assertTrue(TestLexer.checkLexeme("e123.123","e123,.123,<EOF>",137))
    
    def test_float_wrong_case4(self):
        self.assertTrue(TestLexer.checkLexeme("123e","123,e,<EOF>",138))
    
    def test_float_wrong_case5(self):
        self.assertTrue(TestLexer.checkLexeme("123ea3","123,ea3,<EOF>",139))


    # STRING

    def test_string_simple(self):
        self.assertTrue(TestLexer.checkLexeme(' "This is string" ',"This is string,<EOF>",140))
    
    def test_string_simple_case2(self):
        self.assertTrue(TestLexer.checkLexeme(" \"This is string\"This is not string ","This is string,This,is,not,string,<EOF>",141))
    
    def test_string(self):
        self.assertTrue(TestLexer.checkLexeme(" \"This is string\"\"This is string too\" ","This is string,This is string too,<EOF>",142))
    
    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(" \"This is string\\ttoo\" ","This is string\\ttoo,<EOF>",143))
    
    def test_string_unclosed_string(self):
        self.assertTrue(TestLexer.checkLexeme(" \"My name is Dai\"s\" ","My name is Dai,s,Unclosed String:  ",144))
    
    def test_string_unclosed_string_case2(self):
        self.assertTrue(TestLexer.checkLexeme("\"Dai\"\"\"\"","Dai,,Unclosed String: ",145))
    
    def test_string_unclosed_string_case3(self):
        self.assertTrue(TestLexer.checkLexeme("\"Tan\nDai\"","Unclosed String: Tan",146))
    
    def test_string_unclosed_string_case4(self):
        self.assertTrue(TestLexer.checkLexeme("\"HELLO \t \"","Unclosed String: HELLO ",147))
    
    def test_string_illegal_escape(self):
        self.assertTrue(TestLexer.checkLexeme("\"Name: Dai \haha \" ","Illegal Escape In String: Name: Dai \h",148))
    
    def test_string_illegal_escape_case2(self):
        self.assertTrue(TestLexer.checkLexeme("\"Tan \y\oDai  \" ","Illegal Escape In String: Tan \y",149))
    
    def test_errorToken(self):
        self.assertTrue(TestLexer.checkLexeme("Dai's","Dai,Error Token '",150))
    
    def test_errorToken_case2(self):
        self.assertTrue(TestLexer.checkLexeme("char a='$'","char,a,=,Error Token '",151))
    
    def test_errorToken_case3(self):
        self.assertTrue(TestLexer.checkLexeme("\"string s=\" HELLO %\h","string s=,HELLO,%,Error Token \\",152))

    def test_errorToken_case4(self):
        self.assertTrue(TestLexer.checkLexeme("$","Error Token $",153))
    
    def test_string_special(self):
        self.assertTrue(TestLexer.checkLexeme("\"String\\n\"","String\\n,<EOF>",154))

    def test_string_special_2(self):
        self.assertTrue(TestLexer.checkLexeme("\" String a = 10\" a + \" "," String a = 10,a,+,Unclosed String:  ",155))

    def test_string_special_3(self):
        self.assertTrue(TestLexer.checkLexeme("\" String a = 10 \\\"","Unclosed String:  String a = 10 \\\"",156))


    # OPERATOR

    def test_many_operator(self):
        self.assertTrue(TestLexer.checkLexeme("==+-!=>=<==<>","==,+,-,!=,>=,<=,=,<,>,<EOF>",157))
    
    
    def test_operator_with_add(self):
        self.assertTrue(TestLexer.checkLexeme("+","+,<EOF>",158))
    
    def test_operator_with_less_than_equal(self):
        self.assertTrue(TestLexer.checkLexeme("<=","<=,<EOF>",159))
    
    def test_operator_logical_not(self):
        self.assertTrue(TestLexer.checkLexeme("!","!,<EOF>",160))
    
    def test_operator_logical_AND(self):
        self.assertTrue(TestLexer.checkLexeme("&&","&&,<EOF>",161))
    
    def test_operator_special(self):
        self.assertTrue(TestLexer.checkLexeme("===","==,=,<EOF>",162))

    def test_operator_special_2(self):
        self.assertTrue(TestLexer.checkLexeme("===%!==#","==,=,%,!=,=,Error Token #",163))

    # SEPERATOR

    def test_seperator(self):
        self.assertTrue(TestLexer.checkLexeme("{{}","{,{,},<EOF>",164))

    def test_seperator_1(self):
        self.assertTrue(TestLexer.checkLexeme("{ } [] ; ,","{,},[,],;,,,<EOF>",165))

    def test_seperator_2(self):
        self.assertTrue(TestLexer.checkLexeme("{{{;;","{,{,{,;,;,<EOF>",166))  

    # Type

    def test_type(self):
        self.assertTrue(TestLexer.checkLexeme("int a","int,a,<EOF>",167))

    def test_type_1(self):
        self.assertTrue(TestLexer.checkLexeme("void main","void,main,<EOF>",168)) 

    def test_type_2(self):
        self.assertTrue(TestLexer.checkLexeme("float foo","float,foo,<EOF>",169))

    # Array

    def test_array_type(self):
        self.assertTrue(TestLexer.checkLexeme("int a[10];","int,a,[,10,],;,<EOF>",170))
    
    def test_array_type_case2(self):
        self.assertTrue(TestLexer.checkLexeme("float *a;","float,*,a,;,<EOF>",171))


    # EXPRESSION

    def test_arithmetic_expression(self):
        self.assertTrue(TestLexer.checkLexeme("sum = a[3]*5","sum,=,a,[,3,],*,5,<EOF>",172))

    def test_equality_expression(self):
        self.assertTrue(TestLexer.checkLexeme("(b+5*9) == c","(,b,+,5,*,9,),==,c,<EOF>",173))

    def test_equality_expression_case2(self):
        self.assertTrue(TestLexer.checkLexeme("(a[2]*9) == true","(,a,[,2,],*,9,),==,true,<EOF>",174))

    def test_equality_expression_case3(self):
        self.assertTrue(TestLexer.checkLexeme("(b+5&&9) == (c==d)","(,b,+,5,&&,9,),==,(,c,==,d,),<EOF>",175))

    def test_relational_expression(self):
        self.assertTrue(TestLexer.checkLexeme("(a+5.0e-2)*10 >= (d-100)/2","(,a,+,5.0e-2,),*,10,>=,(,d,-,100,),/,2,<EOF>",176))

    def test_relational_expression_case2(self):
        self.assertTrue(TestLexer.checkLexeme("result = (b[1]==5)(c==2)","result,=,(,b,[,1,],==,5,),(,c,==,2,),<EOF>",177))

    def test_open_close_parentheses(self):
        self.assertTrue(TestLexer.checkLexeme("}Tan Dai{","},Tan,Dai,{,<EOF>",178))

    def test_complex_expression(self):
        self.assertTrue(TestLexer.checkLexeme("int a = foo(2)[3+x]+fruits[3]*b[a[2][3]]+foo1(b,c,d);","int,a,=,foo,(,2,),[,3,+,x,],+,fruits,[,3,],*,b,[,a,[,2,],[,3,],],+,foo1,(,b,,,c,,,d,),;,<EOF>",179))

    def test_for_loop(self):
        self.assertTrue(TestLexer.checkLexeme("for(int i =0;i<10;i++){ a += 10;}","for,(,int,i,=,0,;,i,<,10,;,i,+,+,),{,a,+,=,10,;,},<EOF>",180))

    def test_while_loop(self):
        self.assertTrue(TestLexer.checkLexeme("int i=0; while(i++ <= 10)","int,i,=,0,;,while,(,i,+,+,<=,10,),<EOF>",181))

    def test_expession_statement(self):
        self.assertTrue(TestLexer.checkLexeme("foo(2)[3]=a || b(c+35.4e10)*9+10.0 / 4;","foo,(,2,),[,3,],=,a,||,b,(,c,+,35.4e10,),*,9,+,10.0,/,4,;,<EOF>",182))

    def test_separator_token(self):
        self.assertTrue(TestLexer.checkLexeme("}{[()],;","},{,[,(,),],,,;,<EOF>",183))

    def test_expression_case1(self):
        self.assertTrue(TestLexer.checkLexeme("a+123e-1+-1*.3","a,+,123e-1,+,-,1,*,.3,<EOF>",184))

    def test_expression_case2(self):
        self.assertTrue(TestLexer.checkLexeme("a+12.4+e32-43e","a,+,12.4,+,e32,-,43,e,<EOF>",185))
    
    def test_legal_escape_backspace(self):
        self.assertTrue(TestLexer.checkLexeme("\"HELLO \\f\"","HELLO \\f,<EOF>",186))
    
    def test_legal_escape_newline(self):
        self.assertTrue(TestLexer.checkLexeme("\"This is old line \\n\"","This is old line \\n,<EOF>",187))

    def test_legal_escape_tab(self):
        self.assertTrue(TestLexer.checkLexeme("\"This is test for tab \\t\"","This is test for tab \\t,<EOF>",188))

    def test_legal_carriage_return(self):
        self.assertTrue(TestLexer.checkLexeme("\"This is test for carriage return \\r\"","This is test for carriage return \\r,<EOF>",189))
    
    def test_legal_formfeed(self):
        self.assertTrue(TestLexer.checkLexeme("\"This is test for formfeed \\f\"","This is test for formfeed \\f,<EOF>",190))

    def test_illegal(self):
        self.assertTrue(TestLexer.checkLexeme("\"string \\a\"","Illegal Escape In String: string \\a",191))

    def test_function_(self):
        self.assertTrue(TestLexer.checkLexeme("int foo(int n){ return foo(n-1)*foo(n-2);}","int,foo,(,int,n,),{,return,foo,(,n,-,1,),*,foo,(,n,-,2,),;,},<EOF>",192))

    def test_function_2(self):
        self.assertTrue(TestLexer.checkLexeme("do{a+=10;} while(a<100);","do,{,a,+,=,10,;,},while,(,a,<,100,),;,<EOF>",193))

    def test_break_(self):
        self.assertTrue(TestLexer.checkLexeme("if(a==-10) break;","if,(,a,==,-,10,),break,;,<EOF>",194))

    def test_break_2(self):
        self.assertTrue(TestLexer.checkLexeme("if(a==-10) break;","if,(,a,==,-,10,),break,;,<EOF>",195))

    def test_continue(self):
        self.assertTrue(TestLexer.checkLexeme("if(a==-10) continue;","if,(,a,==,-,10,),continue,;,<EOF>",196))

    def test_string_(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123" ""","""123a\\n123,<EOF>""",197))

    def test_unclose_string_(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123 ""","""Unclosed String: 123a\\n123 """,198))

    def test_illegal_escape_(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\m123" ""","""123,Illegal Escape In String: 123a\\m""",199))

    def test_double_slash(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\\\123" ""","""123,123a\\\\123,<EOF>""",200))



    
 
