import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_add(self):
        input = """void main() {
            int a;
            a = 10;
            putInt(a+3);
        }"""
        expect = "13"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_int_sub(self):
        input = """void main() {
            int a;
            a = 10;
            putInt(a - 7);
        }"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_int_mul(self):
        input = """void main() {
            int a;
            a = 10;
            putInt(a * 7);
        }"""
        expect = "70"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_int_div(self):
        input = """void main() {
            int a;
            a = 100;
            putInt(a / 3);
        }"""
        expect = "33"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_int_mod(self):
        input = """void main() {
            int a;
            a = 100;
            putInt(a % 3);
        }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_doWhile_add(self):
        input = """void main() {
            int i; i= 0;
            do
                i = i +1;
            while(i<10);
            putInt(i);
        }"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    def test_doWhile_block(self):
        input = """void main() {
            int i; i= 1;
            int a;
            a = 1;
            do {
                a = a+ 1;
                i = i * a;
            }
            while(a <10);
            putInt(i);
        }"""
        expect = "3628800"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    def test_doWhile_block_with_multi_Arithmethic(self):
        input = """void main() {
            int i; i= 1;
            int a;
            a = 1;
            do {
                a = a + 2;
                i = a + ((i - 2)*5)%7;
            }
            while(a <20);
            putInt(i);
        }"""
        expect = "26"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    def test_if(self):
        input = """void main() {
            int a;
            a = 1;
            if(a==1){
                putString("condition true");
            }
        }"""
        expect = "condition true"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    def test_if_condition_false(self):
        input = """void main() {
            int a;
            a = 1;
            if(a==2){
                putString("condition true");
            }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,510))
    def test_if_else(self):
        input = """void main() {
            int a;
            a = 1;
            if(a==2){
                putString("condition true");
            }
            else{
                putString("condition wrong");
            }
        }"""
        expect = "condition wrong"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    def test_if_else_with_false_cond(self):
        input = """void main() {
            int a;
            a = 1;
            if(a==2){
                putString("condition true");
            }
            else{
                int b;
                b = 10 ;
                putInt(b);
            }
        }"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    def test_if_else_with_true_cond(self):
        input = """void main() {
            int a;
            a = 1;
            if(a==1){
                putString("condition true");
            }
            else{
                int b;
                b = 10 ;
                putInt(b);
            }
        }"""
        expect = "condition true"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_call_exp(self):
        input = """
        int foo(int a){
            return a*2;
        }
        void main(){
            putInt(foo(3));
        }"""
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    def test_call_exp_with_if(self):
        input = """
        int foo(int a){
            if (a == 3)
                return a*2;
            return 1;
        }
        void main(){
            putInt(foo(3));
        }"""
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,515))
    def test_call_exp_with_if_false(self):
        input = """
        int foo(int a){
            if (a == 3)
                return a*2;
            return 1;
        }
        void main(){
            putInt(foo(5));
        }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,516))
    def test_call_exp_(self):
        input = """
        int foo(int a){
            
            return a + 2;
        }
        void main(){
            putInt(foo(5)*3);
        }"""
        expect = "21"
        self.assertTrue(TestCodeGen.test(input,expect,517))

    def test_call_exp_with_recursive_func(self):
        input ="""
        void main(){
            int a;
            a=gt(3);
            putInt(a);
        }
        int gt(int n){
            if(n==1 || n==0){
                return 1;
            }
            return n*gt(n-1);
        }
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,518))
    def test_call_exp_with_recursive_func_1(self):
        input = """
        int foo(int a){
            if(a == 1)
                return 1;
            else
                return a*foo(a-1);
        }
        void main(){
            putInt(foo(3));
        }"""
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,519))
    def test_call_exp_with_recursive_block_func(self):
        input = """
        int foo(int a){
            if(a == 1){
                return 1;
            }   
            else{
                return a*foo(a-1);
            }    
        }
        void main(){
            putInt(foo(3));
        }"""
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,520))
    def test_for(self):
        input = """
            void main(){
                int i;
                int s; s = 0;
                for(i=1;i<10;i = i + 1){
                    s = s + i;
                }
                putInt(s);
            }
        
        """
        expect = "45"
        self.assertTrue(TestCodeGen.test(input,expect,521))
    def test_for_with_if(self):
        input = """
            void main(){
                int i, s;
                s = 0;
                for(i=1;i<10;i = i + 1){
                    s = s + i;
                }
                if(s < 40){
                    putStringLn("Tan Dai");
                }
                else{
                    putStringLn("Pham Tan Dai");
                }
            }
        
        """
        expect = "Pham Tan Dai\n"
        self.assertTrue(TestCodeGen.test(input,expect,522))
    def test_for_with_break(self):
        input = """
            void main(){
                int i, s;
                s = 0;
                for(i=1;i<10;i = i + 1){
                    s = s + i;
                    if(s > 30)
                        break;
                }
                putInt(s);
            }
        
        """
        expect = "36"
        self.assertTrue(TestCodeGen.test(input,expect,523))
    def test_for_with_continue(self):
        input = """
            void main(){
                int i, s;
                s = 0;
                for(i=1;i<10;i = i + 1){
                    if(s > 25)
                        continue;
                    s = s + i;  
                }
                putInt(s);
            }
        
        """
        expect = "28"
        self.assertTrue(TestCodeGen.test(input,expect,524))
    def test_DoWhile_with_break(self):
        input = """
            void main(){
                int i, s;
                s = 1;
                i = 1;
                do{
                    s = s*i;
                    i = i+ 1;
                    if(i> 6)
                        break;
                }while(s < 1000);
                putInt(s);
            }
        
        """
        expect = "720"
        self.assertTrue(TestCodeGen.test(input,expect,525))
    def test_DoWhile_with_continue(self):
        input = """
            void main(){
                int i, s;
                s = 1;
                i = 1;
                do{
                    if(i> 8)
                        continue;
                    s = s*i;
                    i = i+ 1;                   
                }while(s < 1000);
                putInt(s);
            }
        
        """
        expect = "5040"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    
    def test_Funcdecl_after_main(self):
    	input ="""
        void main(){
                foo1();
            }
            void foo1(){
                putInt(3);
            }
        """
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_Funcdecl_And_FuncCall_More(self):
    	input ="""
        void main(){
            putInt(foo(2));
            return;            
        }
        int foo(int x){
            return 0;
        }
        """
    	expect = "0"
    	self.assertTrue(TestCodeGen.test(input,expect,528))

    def test_Div_Float_Simple(self):
    	input ="""
        void main(){
            int a;
            a = 2;
            float x;
            x  = 0;            
            if(a<=3){
                x = 3 / 2; 
            }
            putFloat(x);                 
        }
        """
    	expect = "1.0"
    	self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_String_Simple(self):
    	input ="""
        void main(){
            putString("Hello World");               
        }
        """
    	expect = "Hello World"
    	self.assertTrue(TestCodeGen.test(input,expect,530))

    def test_String_with_Dowhile(self):
    	input ="""
        void main(){
            int i;
            i = 0 ;
            do{
                i = i + 1;                
                if (i == 3){
                    continue;
                }                 
                putString("Do while time: ");
                putIntLn(i); 
            }while(i < 5);                         
        }
        """
    	expect = "Do while time: 1\nDo while time: 2\nDo while time: 4\nDo while time: 5\n"
    	self.assertTrue(TestCodeGen.test(input,expect,531))

    
    def test_For_with_Break_simple(self):
    	input ="""
        void main(){
            int i;
            for(i = 0; i <= 5 ; i = i * 2){
                putInt(i);
                break;
            }                   
        }
        """
    	expect = "0"
    	self.assertTrue(TestCodeGen.test(input,expect,532))

    def test_Return_In_Block(self):
    	input ="""
        int func(int a){
            if (a < 3){
                a = 2;
                return a;
            }
            else 
                return 3;
        }
        void main(){
            putInt(func(1));
        }
        """
    	expect = "2"
    	self.assertTrue(TestCodeGen.test(input,expect,533))    

    def test_Funcdecl_Recursive_with_Return_In_Block(self):
            input = """
            int foo(int a){
                if(a == 1){
                    return 1;
                }
                else{
                    return a* foo(a-1);
                }
            }
            void main(){
                putInt(foo(3));
            }"""
            expect = "6"
            self.assertTrue(TestCodeGen.test(input,expect,534))

    def test_Funcdecl_with_Return_In_IfElse(self):
            input = """
            int foo(){
                int x ;
                x = 3;
                if(x <= 2)
                    return 3 * 2;
                else
                    return 3 + 2;
            }
            void main(){
                putInt(foo());
            }"""
            expect = "5"
            self.assertTrue(TestCodeGen.test(input,expect,535))

    def test_Funcdecl_with_Return_and_For(self):
            input = """
            int foo(int a){
                for (a =0 ; a <= 3; a = a +1){
                    a = a + 1;
                }
                return a; 
            }
            void main(){
                putInt(foo(3));
            }"""
            expect = "4"
            self.assertTrue(TestCodeGen.test(input,expect,536))

    def test_Funcdecl_with_Return_In_For(self):
            input = """
            int foo(int a){
                for (a =0 ; a <= 3; a = a +1){
                    a = a + 1;
                    return 10;
                }
                return a;
            }
            void main(){
                putInt(foo(3));
            }"""
            expect = "10"
            self.assertTrue(TestCodeGen.test(input,expect,537))

    def test_Return_In_DoWhile(self):
            input = """
            int foo(int a){
                do{
                    a = a + 1 ;
                    return a;
                }while(a <3);
            }
            void main(){
                putInt(foo(0));
            }"""
            expect = "1"
            self.assertTrue(TestCodeGen.test(input,expect,538))

    def test_Return_In_DoWhile_With_manyStmt(self):
            input = """
            int foo(int a){
                do
                {
                }
                {
                    a = a + 2 ;
                }
                return a;
                {
                }
                while(a <3);
            }
            void main(){
                putInt(foo(0));
            }"""
            expect = "2"
            self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_Return_In_VoidType_Function(self):
            input = """
            void func(int a){
                putString("Hello");
                return;
            }
            void main(){
                func(3);
            }"""
            expect = "Hello"
            self.assertTrue(TestCodeGen.test(input,expect,540))

    def test_Return_In_VoidType_Main_Function(self):
            input = """
            void func(){
                putFloat(5.3);
                return;
            }
            void main(){
                func();
                return;
            }"""
            expect = "5.3"
            self.assertTrue(TestCodeGen.test(input,expect,541))

    def test_UnOp_NEGOP_Simple(self):
            input = """
            void main(){
                int a;
                a = 5 ;
                a = 5 + -3;
                putInt(a);
                return;
            }"""
            expect = "2"
            self.assertTrue(TestCodeGen.test(input,expect,542))

    def test_UnOp_NOT_Simple(self):
            input = """
            void main(){
                boolean a;
                a = false;
                if (!a){
                    putString("This is False");
                }
                return;
            }"""
            expect = "This is False"
            self.assertTrue(TestCodeGen.test(input,expect,543))

    def test_UnOp_NOT_More(self):
            input = """
            void main(){
                boolean a;
                boolean b;
                a = true;
                b = !a && true;
                if (b != true){
                    putString("This is False");
                }
                return;
            }"""
            expect = "This is False"
            self.assertTrue(TestCodeGen.test(input,expect,544))

    def test_IfElse_with_Booleanliteral(self):
            input = """
            void main(){
                if (false){
                    putString("This is False");
                }
                else{
                    putString("This is True");
                }
                return;
            }"""
            expect = "This is True"
            self.assertTrue(TestCodeGen.test(input,expect,545))
    def test_ArrayCell_Simple(self):
            input = """
            void main(){
                int a[2];
                a[0] = 1;
                a[1] = 2;
                putInt(a[0]);
            }"""
            expect = "1"
            self.assertTrue(TestCodeGen.test(input,expect,546))

    def test_ArrayCell_Float_Simple(self):
            input = """
            void main(){
                float arr[3];
                arr[0]= 1.2;
                arr[1] = 2;
                arr[2] = arr[0] * arr[1];
                putFloat(arr[2]);
            }"""
            expect = "2.4"
            self.assertTrue(TestCodeGen.test(input,expect,547))

    def test_ArrayCell_With_For(self):
            input = """
            void main(){
                int i;
                int arr[5];
                for (i = 0 ; i < 5; i = i + 1){
                    arr[i] = i;
                    putIntLn(arr[i]);
                }
            }"""
            expect = "0\n1\n2\n3\n4\n"
            self.assertTrue(TestCodeGen.test(input,expect,548))

    def test_ArrayCell_With_DoWhile(self):
            input = """
            void main(){
                int i;
                i = 0;
                float arr[5];
                do{
                    i = i + 1;
                    arr[i] = i*i;
                    putString("arr[");
                    putInt(i);
                    putString("] =");
                    putFloatLn(arr[i]);
                }while(i<4);
            }"""
            expect = "arr[1] =1.0\narr[2] =4.0\narr[3] =9.0\narr[4] =16.0\n"
            self.assertTrue(TestCodeGen.test(input,expect,549))

    def test_GlobalVariable_ArrayType(self):
            input = """
            int arr[3];
            int x;
            void main(){
                int i;
                x = 2;
                for (i = 2; i >=0; i =  i -1 ){
                    arr[i] = x * i;
                }
                putIntLn(arr[1]);
            }"""
            expect = "2\n"
            self.assertTrue(TestCodeGen.test(input,expect,550))

    def test_GlobalVariable_ArrayType_More(self):
            input = """
            boolean arr[2];
            void main(){
                arr[0] = false;
                arr[1] = true;
                if(arr[1]){
                    putString("This is ArrayCell True");
                }
            }"""
            expect = "This is ArrayCell True"
            self.assertTrue(TestCodeGen.test(input,expect,551))

    def test_Function_Return_ArrayCell(self):
            input = """
            float foo(){
                int i;
                float arr[5];
                for(i = 0 ; i < 5; i = i + 1){
                    arr[i] = 10 - i;
                }
                return arr[2];
            }
            void main(){
                putFloat(foo());
            }"""
            expect = "8.0"
            self.assertTrue(TestCodeGen.test(input,expect,552))

    def test_Function_Return_ArrayCell_More(self):
            input = """
            float foo(){
                int i;
                int arr[5];
                for(i = 0 ; i < 5; i = i + 1){
                    arr[i] = i + 10;
                }
                return arr[3];
            }
            void main(){
                putFloat(foo());
            }"""
            expect = "13.0"
            self.assertTrue(TestCodeGen.test(input,expect,553))

    def test_program_with_simple_Exp_Add_Float(self):
        input = """
        void main() {
            float x;
            x = 8.3 - 3;
            putFloatLn(x);
        }"""
        expect = "5.3\n"
        self.assertTrue(TestCodeGen.test(input,expect,554))

    def test_program_with_simple_Exp_And(self):
    	input = """
        void main() {
            boolean flag;
            flag = true && false;
            putBool(flag);
        }"""
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,555))

    def test_funcdecl_and_funccall_simple(self):
    	input = """
        int foo(){
            return 1 + 3 ;
        }
        void main() {
            int x;
            x = foo();
            putInt(x);
        }"""
    	expect = "4"
    	self.assertTrue(TestCodeGen.test(input,expect,556))
    def test_funcdecl_ReturnType_Float_simple(self):
    	input = """
        float foo(){
    
            return 2.0;
        }
        void main() {
            putFloat(foo());
        }"""
    	expect = "2.0"
    	self.assertTrue(TestCodeGen.test(input,expect,557))

    def test_Float_FuncCall_with_Param(self):
    	input = """
        float foo(int a, float b){
            return a - b;
        }
        void main() {
            float x;
            x  = foo(6,1.5);
            putFloat(x);
        }"""
    	expect = "4.5"
    	self.assertTrue(TestCodeGen.test(input,expect,558))
    def test_IfElseStmt_Simple(self):
    	input = """
        void main() {
            int x;
            x  = 5 ;
            if (x == 5)
                putFloat(5.5);
            else
                putFloat(1.5);
        }"""
    	expect = "5.5"
    	self.assertTrue(TestCodeGen.test(input,expect,559))

    def test_IfElseStmt_More_Simple(self):
    	input = """
        void main() {
            int x;
            x = 2;
            if (x >= 3)
                x = 3;
            else
                x = 5;
            putIntLn(x);
        }"""
    	expect = "5\n"
    	self.assertTrue(TestCodeGen.test(input,expect,560))


    def test_IfStmt_Simple(self): #error
    	input = """
        int x;
        void main() {
            x = 3;
            if (x <= 3)
                x = x + 1;
            putIntLn(x);
        }"""
    	expect = "4\n"
    	self.assertTrue(TestCodeGen.test(input,expect,561))

    def test_Block_Simple(self):
    	input = """
        int x,y;
        void main() {
            x = 3;
            y = 0;
            if (x <= 3){
                x = x + 1;
                y = x - 3;
            }
            putIntLn(1);
        }"""
    	expect = "1\n"
    	self.assertTrue(TestCodeGen.test(input,expect,562))

    def test_Dowhile_Simple(self): #error
    	input = """
        int a;
        void main() {
            a = 1;
            do{
                a = a + 1 ;
            }while(a < 10);
            putIntLn(a);
        }"""
    	expect = "10\n"
    	self.assertTrue(TestCodeGen.test(input,expect,563))

    def test_Dowhile_Many_Stmt(self):  #error
    	input = """
        int a;
        void main() {
            a = 1;
            float x;
            x = 0.1;
            do{
                a = a + 1 ;
            }
            {
                x = x + 1;
            }while(a < 10);
            putIntLn(a);
            putFloat(x);
        }"""
    	expect = "10\n9.1"
    	self.assertTrue(TestCodeGen.test(input,expect,564))

    def test_Dowhile_With_Break(self):
    	input = """
        void main() {
            int a;
            a = 0;
            do{
                a = a + 1 ;
                if (a == 5){
                    break;
                }
            }
            while(a < 10);
            putIntLn(a);
        }"""
    	expect = "5\n"
    	self.assertTrue(TestCodeGen.test(input,expect,565))

    def test_Dowhile_With_Continue(self):
    	input = """
        void main() {
            int a;
            a = 0 ;
            do{
                a = a + 1;
                if (a == 2){
                    continue;
                }
                putIntLn(3);                
                
            }
            while(a < 4);
        }"""
    	expect = "3\n3\n3\n"
    	self.assertTrue(TestCodeGen.test(input,expect,566))

    def test_For_Simple(self):
    	input = """
        void main() {
            int i;
            int a;
            a = 0 ;
            for (i = 0 ; i <= 3; i = i + 1 ){
                a =  a + 1; 
            }
            putInt(a);
        }"""
    	expect = "4"
    	self.assertTrue(TestCodeGen.test(input,expect,567))

    def test_For_Break_After_Exp(self):
    	input = """
        void main() {
            int i;
            int a;
            a = 0 ;
            for (i = 0 ; i <= 3; i = i + 1 ){
                a =  a + 1; 
                if (i == 2){
                    break;
                }
            }
            putInt(a);
        }"""
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,568))

    def test_For_Break_Before_Exp(self):
    	input = """
        void main() {
            int i;
            int a;
            a = 0 ;
            for (i = 0 ; i <= 3; i = i + 1 ){
                if (i == 2){
                    break;
                }
                a =  a + 1; 
            }
            putInt(a);
        }"""
    	expect = "2"
    	self.assertTrue(TestCodeGen.test(input,expect,569))


    def test_For_Continue(self):
    	input = """
        void main() {
            int i;
            int a;
            a = 0 ;
            for (i = 0 ; i <= 3; i=i+1 ){
                if (i == 2){
                    continue;
                }
                a = a + 1; 
            }
            putInt(a);
        }"""
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,570))

    def test_Function_With_Param_ArrayPointerType(self):
            input = """
            int foo(int arr[]){
                int i;
                for(i = 0 ; i < 3; i = i + 1){
                    arr[i] = i;
                }
                return arr[1];
            }
            void main(){
                int arr[3];
                putInt(foo(arr));
            }"""
            expect = "1"
            self.assertTrue(TestCodeGen.test(input,expect,571))
 
    def test_ifstatementfollowifstatementandassignexpression(self):
            input = """void main () {
                        int a,b; 
                        a = 2; b = 10;  
                        if (a==b) 
                          if (a<10) 
                            a = a + b;
                          else
                            a = a + 2*b; 
                        else 
                          if (a>10) 
                            a = a - b;
                          else
                            a = a - 2*b;   
                        putIntLn(a); 
                  }"""
            expect = "-18\n"
            self.assertTrue(TestCodeGen.test(input,expect,572))   
 
    def test_call_exp_with_func_return_array_type(self):
            input = """
                int[] foo(){
                int a[5];
                a[1] = 100;
                return a;
                }
                void main(){
                putInt(foo()[1]);
                }  
            """
            expect = "100"
            self.assertTrue(TestCodeGen.test(input,expect,573))   
 
    def test_call_exp_with_func_return_array_type_1(self):
        # check call-function as index in access of array
            input = """
                int boo(){
                return 1;
                }
                int[] foo(){
                int a[5];
                a[1] = 100;
                return a;
                }
                void main(){
                putInt(foo()[boo()]);
                }  
            """
            expect = "100"
            self.assertTrue(TestCodeGen.test(input,expect,574))   
    def test_BoolType_array_global_variable(self):
    
            input ="""
                boolean a[5];
                void main() {
                a[1] = !true||true;
                putBool(a[1]);
                }
            """
            expect = "true"
            self.assertTrue(TestCodeGen.test(input,expect,575)) 
  
    def test_Function_Return_ArrayCell_hieu(self):
        input = """
            float foo(){
                int i;
                float arr[5];
                for(i = 0 ; i < 5; i = i + 1){
                    arr[i] = 10 - i;
                }
                return arr[2];
            }
            void main(){
                float a;
                a=foo();
                putFloat(a);
            }"""
        expect = "8.0"
        self.assertTrue(TestCodeGen.test(input,expect,576))

    #test dowhile statement complex
    def test_dowhile_statement_complex(self):
    	input ="""
        void main(){
            int i;
            i=0;
            do{
                putString("Hello ");
            }
            {
                putString("PPL ");
                i=i+1;
            }
            while(i<5);
        }
        """
    	expect = "Hello PPL Hello PPL Hello PPL Hello PPL Hello PPL "
    	self.assertTrue(TestCodeGen.test(input,expect,577))

    def test_dowhile_statement_complex_with_continue(self):
    	input ="""
        void main(){
            int i;
            i=0;
            do
            {
                putString("PPL LOVER ");
                i=i+1;
                if(i==3){
                    {
                        continue;
                    }
                }
            }
            while(i<5);
        }
        """
    	expect = "PPL LOVER PPL LOVER PPL LOVER PPL LOVER PPL LOVER "
    	self.assertTrue(TestCodeGen.test(input,expect,578))

    def test_Function_Return_ArrayCell_More_hieu(self):
        input = """
        float foo(){
            int i;
            int arr[5];
            for(i = 0 ; i < 5; i = i + 1){
                arr[i] = i + 10;
            }
            return arr[3];
        }
        void main(){
            putFloat(foo());
        }"""
        expect = "13.0"
        self.assertTrue(TestCodeGen.test(input,expect,579))

    def test_dowhile_statement_complex_with_break(self):
    	input ="""
        void main(){
            int i;
            i=0;
            do
            {
                putString("PPL LOVER ");
                i=i+1;
                if(i==3){
                    {
                        break;
                    }
                }
            }
            while(i<5);
        }
        """
    	expect = "PPL LOVER PPL LOVER PPL LOVER "
    	self.assertTrue(TestCodeGen.test(input,expect,580))

    def test_Function_With_Param_ArrayCell_hieu(self):
        input = """
        int foo(int arr[]){
            int i;
            for(i = 0 ; i < 3; i = i + 1){
                arr[i] = i;
            }
            return arr[1];
        }
        void main(){
            int arr[3];
            putInt(foo(arr));
        }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,581))

    def test_program_with_simple_Exp_And_hieu(self):
    	input = """
        void main() {
            boolean flag;
            flag = true && false;
            putBool(flag);
        }"""
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,582))

    def test_UnOp_NOT_More_hieu(self):
        input = """
        void main(){
            boolean a;
            boolean b;
            a = true;
            b = !a && true;
            if (b != true){
                putString("This is False");
            }
            return;
        }"""
        expect = "This is False"
        self.assertTrue(TestCodeGen.test(input,expect,583))

    def test_IfElse_with_Booleanliteral_hieu(self):
        input = """
        void main(){
            if (false){
                putString("This is False");
            }
            else{
                putString("This is True");
            }
            return;
        }"""
        expect = "This is True"
        self.assertTrue(TestCodeGen.test(input,expect,584))

    def test_Function_With_ArrayPoiterType_hieu(self):
        input = """
        int[] foo(){
            int i;
            int arr[3];
            for(i = 0 ; i < 3; i = i + 1){
                arr[i] = i + 1;
            }
            return arr;
        }
        void main(){
            putInt(foo()[1]);
        }"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,585))

    def test_function_and_scope(self):
        input = """
      
        void main(){
            int main;
            main=1;
            putInt(main);
            {
                int main;
                main=100;
                putInt(main);
            }
            putInt(main);
        }"""
        expect = "11001"
        self.assertTrue(TestCodeGen.test(input,expect,586))

    def test_function_and_scope_in_mc_file(self):
        input = """
        int i;
        int f(){
            return 200;
        }
        void main(){
            int main;
            main=f();
            putIntLn(main);
            {
                int main;
                int f,i;
                main=f=i=100;
                putIntLn(main);
                putIntLn(f);
                putIntLn(i);
            }
            putInt(main);
        }"""
        expect = "200\n100\n100\n100\n200"
        self.assertTrue(TestCodeGen.test(input,expect,587))

    # def test_many_assign_with_array_cell(self):
    #     input = """
    #     void main(){
    #         int i;
    #         int arr[10];
    #         arr[0]=arr[1]=arr[2]=10;
    #         putIntLn(arr[0]);
    #         putIntLn(arr[1]);
    #         putInt(arr[2]);
    #     }"""
    #     expect = "10\n10\n10"
    #     self.assertTrue(TestCodeGen.test(input,expect,588))

    def test_Function_With_ArrayPoiterType_And_ArrayCell_hieu(self): 
        input = """
        void main(){
            int x;
            x = 1;
            float a[5];
            int b[5];
            b[2] = 2;
            a[2]= 5;
            putFloat(a[b[2]]);
        }"""
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,589)) 

    def test_Function_With_ArrayPoiterType_And_ArrayCell_More_hieu(self):
        input = """
        int[] foo(int n){
            int arr[3];
            return arr;
        }
        void main(){
            int x;
            x = 1 ;
            int a[5];
            int b[5];
            b[2] = 2;
            a[2]= 5;
            foo(3)[1+x] = a[b[2]] + 3;
            putInt(foo(3)[1+x]);
        }"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,590))

    def test_SumFunction_Recursion(self):
        input = """
        // tinh tong tu 1 den n            
        int foo(int n){
            if(n == 1) {
                return 1;
            }
            else {
                return n + foo(n-1);
            }
        }
        void main(){
            int x;
            x = foo(10);
            putInt(x);
        }"""
        expect = "55"
        self.assertTrue(TestCodeGen.test(input,expect,591))

    def test_MulFunction_Recursion(self):
        input = """
        // tinh tich tu 1 den n            
        int foo(int n){
            if(n == 1) {
                return 1;
            }
            else {
                return n * foo(n-1);
            }
        }
        void main(){
            int x;
            x = foo(10);
            putInt(x);
        }"""
        expect = "3628800"
        self.assertTrue(TestCodeGen.test(input,expect,592))

    def test_GCD_Recursion_hieu(self):
        input = """            
        int gcd(int a, int b){
            if(b == 0){
                return a;
            }
            return gcd(b, a % b);
        }
        void main(){
            putString("GCD of 9 and 6: ");
            putInt(gcd(9, 6));
        }"""
        expect = "GCD of 9 and 6: 3"
        self.assertTrue(TestCodeGen.test(input,expect,593))

    def test_binaryop_complex_int_both_side_and_array(self):
        input ="""
            void main(){
                int a,b,c;
                int arr[10];
                a=10;
                b=20;
                c=30;
                arr[0]=a*b-c;
                putInt(arr[0]);
            }
            
            """
        expect = "170"
        self.assertTrue(TestCodeGen.test(input,expect,594))

    def test_binaryop_complex_float_both_side(self):
    	input ="""
        void main(){
            float a,b,c;
            float arr[10];
            a=1.0;
            b=2.4;
            c=3.2;
            arr[0]=a*b-c;
            putFloat(arr[0]);
        }
        
        """
    	expect = "-0.79999995"
    	self.assertTrue(TestCodeGen.test(input,expect,595))
    
    def test_binaryop_complex_float_side_left_and_int_side_right(self):
    	input ="""
        void main(){
            int a,b;
            float c;
            float arr[10];
            a=10;
            b=24;
            c=32;
            arr[0]=a*b-c;
            putFloat(arr[0]);
        }
        
        """
    	expect = "208.0"
    	self.assertTrue(TestCodeGen.test(input,expect,596))

    def test_binaryop_complex_float_global(self):
    	input ="""
        float c;
        void main(){
            int a,b;
            float arr[10];
            a=10;
            b=24;
            c=32;
            arr[0]=a*b-c;
            putFloat(arr[0]);
        }
        
        """
    	expect = "208.0"
    	self.assertTrue(TestCodeGen.test(input,expect,597))

    def test_binaryop_complex_float_array_global(self):
    	input ="""
        float c[20];
        void main(){
            int a,b;
            a=10;
            b=24;
            c[0]=a*b-20;
            putFloat(c[0]);
        }
        """
    	expect = "220.0"
    	self.assertTrue(TestCodeGen.test(input,expect,598))

    def test_LessThanEqual_Float(self):
    	input ="""
        void main(){
            float x;
            x = 5.6;
            if (x <= 6.0){
                putString("Successful");
            }
            else{
                putString("Fail");
            }
        }
        """
    	expect = "Successful"
    	self.assertTrue(TestCodeGen.test(input,expect,599))

    def test_Equal_Float_And_Int(self):
    	input ="""
        float foo(){
            return 5.2;
        }
        void main(){
            float x;
            x = 7.2;
            int i;
            i = 0;
            do{
                i = i + 1;
                if ((i > foo()) && (i < x)) continue;
                putInt(i);
            }while(i < 10);
        }
        """
    	expect = "123458910"
    	self.assertTrue(TestCodeGen.test(input,expect,600))



























        
   