import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_var_decl(self):
        input = """int a,b,c[3],d,e[0];float k;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_simple_program(self):
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_more_complex_program(self):
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    

    def test_index_exp(self):
        input = """int main() {
            foo(2)[3+x] = a[b[2]] + 3;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_if(self):
        input = """
        int main() {
            if(true) a=10;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_invalid_function_declaration_nested_function(self) :
        input = """void b(int a[],int b){
            int foo(){return 1}
        }               
        """
        expect ="Error on line 2 col 19: ("
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_wrong_program(self):
        input = """} int main {"""
        expect = "Error on line 1 col 0: }"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_invalid_var_decl_inital(self):
        input = """int a = 10;"""
        expect = "Error on line 1 col 6: ="
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_many_var_decl(self):
        input = """int a; float b,c,d[3]; boolean e; string s; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))



    def test_valid_func_decl(self):
        input = """
        int main(string args[],int argc){
            int i;
            int arr[5];
            string s;
            i=1;
            arr = foo(i);
            s = args[0];
            println(s);
            hello();
        }
        int [] foo(int i){
            int a[5];
            for(i;i<5;i=i+1)
            a[i] = i;
            return a;
        }
        void hello(){ println("Hello MC language");}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_invalid_func_decl_case1(self):
        input = """void [] b(){ return; }"""
        expect = "Error on line 1 col 5: ["
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_invalid_func_decl_case2(self):
        input = """void b(int a,b){ return; }"""
        expect = "Error on line 1 col 13: b"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_invalid_func_decl_case3(self):
        input = """void b(int a[5]){ return; }"""
        expect = "Error on line 1 col 13: 5"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_invalid_func_decl_case4(self):
        input = """void b(int a[],void b){ return; }"""
        expect = "Error on line 1 col 15: void"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_invalid_func_decl_case5(self):
        input = """void b(int a[],int[] b){ return; }"""
        expect = "Error on line 1 col 18: ["
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_invalid_func_decl_case6(self):
        input = """void b(int a[],int b)"""
        expect = "Error on line 1 col 21: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_valid_block_statement_in_func(self):
        input = """void b(int a[],int b){
                          int a;a=1;println(a);
                          {
                            int b;b=1;
                            println(b);
                          }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_invalid_name_func(self):
        input = """int 1Calculate(){}"""
        expect = "Error on line 1 col 4: 1"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_valid_name_func(self):
        input = """void Calculate(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_valid_break_in_block(self):
        input = """int foo() {
            break;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_valid_block_func(self):
        input = """int foo(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_valid_if_stm___(self):
        input = """void foo(){
                boolean b ;
                b = true;
                if( !b == false) 
                    println(" b is true");
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_valid_for_and_ifelse(self):
        input = """
        void main(){
            int oddSum, evenSum,arr[10],i;
            oddSum = evenSum =0;
            for(i=0;i<10;i=i+1)
                arr[i]=i;
            for(i=0;i<10;i=i+1){
                if(arr[i]%2==0)
                    evenSum = evenSum + arr[i];
                else
                    oddSum = oddSum + arr[i];
            }        
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_valid_nested_if_else(self):
        input = """
                void main(){
                    int mark;
                    result(mark);
                }
                void result(int mark){
                  if(mark<5)
                    println("Trung binh");
                  else if (5<=mark&&mark<8)
                    println("Kha");
                  else
                    println("Gioi");
                }        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_valid_break_continue_in_for(self):
        input = """
                void main(){
                    int i;
                    for(i=0;i<10;i=i+1)
                    {
                      println("i= %d",i);
                      if(i == 5)
                        continue;
                      if(i==9)
                        break;
                    }
                }        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_valid_do_while(self):
        input = """
                void main(){
                    int i;
                    i = 0;
                    do 
                      println(i);
                      i=i+1;
                      if(i==9)
                        break;
                    while(i<10);
                }         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_valid_do_while_case2(self):
        input = """
                void main(){
                    int i;
                    i = 0;
                    do {
                      println(i);
                      i=i+1;
                      if(i==9)
                        break;
                      else if(i==5)
                        continue;
                    }
                    while(i<10);
                }         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_valid_nested_loop(self):
        input = """
                void main(){
                  int i,j,a[10];
                  for(i=0;i<10;i=i+1)
                    a[i]=(i+10)*5;
                  for(i=0;i<5;i=i+1)
                    for(j=10;j>5;j=j-1)
                    {
                      int temp;
                      temp = a[i];
                      a[i]=a[j];
                      a[j] = temp;
                    }
                }         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_valid_nested_loop_case2(self):
        input = """
                void main(){
                  int i,j,a[10];
                  for(i=0;i<10;i=i+1)
                    a[i]=(i+10)*5;
                    j=10;
                  for(i=0;i<5;i=i+1){
                    do{
                      int temp;
                      temp = a[i];
                      a[i]=a[j];
                      a[j] = temp;
                      j = j-1;
                    }
                    while (j<5);
                  }
                }        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_valid_if_condition(self):
        input = """
                int main(){
                  int a;a=0;
                  if(a+1)
                    println("Hello");
                }        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_invalid_if_condition(self):
        input = """
                int main(){
                  int a;a=0;
                  if()
                    println("Hello");
                }        
        """
        expect = "Error on line 4 col 21: )"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_invalid_if_not_stm_follow_if(self):
        input = """
                int main(){
                  int a;a=0;
                  if(a==0)
                    int b;
                }        
        """
        expect = "Error on line 5 col 20: int"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_invalid_if_not_stm_follow_if_2(self):
        input = """
                int main(){
                  int a;a=0;
                  if(a==0)
                }        
        """
        expect = "Error on line 5 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_valid_if_decl_var_in_block(self):
        input = """
                int main(){
                  int a;a=0;
                  if(a==0){
                      int b;
                      b=foo(2)[3];
                  }
                }       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_valid_for_stm(self):
        input = """
                int main(){
                  int a;
                  for(a=0;a+3;a=a+1)
                    a=a-1;
                }        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_invalid_for_stm_no_stm_follow(self):
        input = """
                int main(){
                  int a;
                  for(a=0;a+3;a=a+1)
                }        
        """
        expect = "Error on line 5 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_invalid_for_stm_without_exp1(self):
        input = """
                int main(){
                  int a;
                  for(;a+3;a=a+1)
                }        
        """
        expect = "Error on line 4 col 22: ;"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_invalid_do_while_without_stm(self):
        input = """
                int main(){
                  boolean a;
                  a=true;
                  do
                  while a==true;
                }       
        """
        expect = "Error on line 6 col 18: while"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_invalid_do_while_without_semi(self):
        input = """
                int main(){
                  boolean a;
                  a=true;
                  do { }
                  while a==true
                }       
        """
        expect = "Error on line 7 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_valid_do_while_(self):
        input = """
                int main(){
                  boolean a;
                  a=true;
                  do { }
                  while a+3 ;
                }       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_invalid_if_wrong_condition(self):
        input = """
                void result(int mark){
                  if(mark<5)
                    println("Trung binh");
                  else if(5<=mark<8)
                    println("Kha");
                  else
                    println("Gioi");
                }    
        """
        expect = "Error on line 5 col 33: <"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_invalid_program(self):
        input = """
        if(5<=a+8) a =7;
        """
        expect = "Error on line 2 col 8: if"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_invalid_many_relation_operator(self):
        input = """
                void result(int mark){
                  int a;
                  a = foo(2)<=a>=b;
        """
        expect = "Error on line 4 col 31: >="
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_invalid_many_relation_operator_2(self):
        input = """
                void result(int mark){
                  int a;
                  a = b>=c==d==e;
                }
        """
        expect = "Error on line 4 col 29: =="
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_invalid_and_operator(self):
        input = """
        int foo() {
          a=b&&&&c;
        }
        """
        expect = "Error on line 3 col 15: &&"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_invalid_or_operator(self):
        input = """
        int foo() {
          a=b||c||;
        }
        """
        expect = "Error on line 3 col 18: ;"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_invalid_not_operator(self):
        input = """
        int foo() {
          a=b!c;
        }
        """
        expect = "Error on line 3 col 13: !"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_invalid_index_operator(self):
        input = """
        int foo() {
          a=b[c+true][d];
        }
        """
        expect = "Error on line 3 col 21: ["
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_invalid_index_operator_2(self):
        input = """
        int foo() {
          a=b[][d];
        }
        """
        expect = "Error on line 3 col 14: ]"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_invalid_index_operator_3(self):
        input = """
        int foo() {
          a=b[d]+ 123(1)[10];
        }
        """
        expect = "Error on line 3 col 21: ("
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_valid_index_operator(self):
        input = """
        int foo() {
          a=b[d]+ 12[10];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_many_assign_stm(self):
        input = """
        int foo() {
          foo(2)[3]=arr[7]=true;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_many_assign_stm_2(self):
        input = """
        int foo() {
          foo(2)[3]=a||b&&(c-35.4e10)*9+10.0/4+true;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_invalid_not_equal(self):
        input = """
        int foo() {
          a=b!=c!=d;
        }
        """
        expect = "Error on line 3 col 16: !="
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_valid_not_equal(self):
        input = """
        int foo() {
          foo[3]= ((1+3*5)==(c-9.0+true))!=foo(3.4,1*5e10,"string");
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_valid_many_op(self):
        input = """
        int foo() {
          foo[3]= ((1+3*5==9)>=(c-9.0+true!=3))<foo(3.4!=5,1*5e10<4,"string");
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_valid_many_exp_index(self):
        input = """
        int foo() {
          foo[3]= a(ab[10[1]])[c+2] ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_valid_exp(self):
        input = """
        int foo() {
          true;
          false;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_valid_exp_1(self):
        input = """
        int foo() {
          100;
          12.2e2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_valid_exp_2(self):
        input = """
        int foo() {
          "string";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_invalid_exp_in_block(self):
        input = """
        int foo() {
          string ;
        }
        """
        expect = "Error on line 3 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_valid_exp_in_block__(self):
        input = """
        int foo() {
          arr[3];
          arr(2)[3];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_valid_exp_in_block_2(self):
        input = """
        int foo() {
          foo();
          foo(3);
          Caculate("",true);
          c==d=f=g;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_invalid_nested_if_else_stm(self):
        input = """
        int foo() {
          if(a==1)
            foo(a);
          else if(a==2)
            foo(a,2);
          else
            foo(3);
          else foo(4);
        }
        """
        expect = "Error on line 9 col 10: else"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_invalid_nested_if_else_stm_(self):
        input = """
        int foo() {
          if(a==1)
            foo(a);
          else ;
        }
        """
        expect = "Error on line 5 col 15: ;"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_invalid_nested_if_else_stm_2(self):
        input = """
        int foo() {
          if(a==1)
            foo(a);
          else int a;
        }
        """
        expect = "Error on line 5 col 15: int"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_valid_nested_if_else_stm(self):
        input = """
        int foo() {
          if(a==1)
            foo(a);
          else a;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_valid_nested_if_else_stm_in_block(self):
        input = """
        int foo() {
          if(a==1)
          {
            if(a)
              c=10.45E-10;
            else
              for(i=0;i=1;i)
                1230;
          }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_valid_nested_if_else_stm_in_block_2(self):
        input = """
        int foo() {
          if(a==1)
          {
            if(a)
              c=10.45E-10;
            else
              return 1;
          }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_invalid_for_wrong_exp(self):
        input = """
        int foo() {
          for(int i=0;i<10;i=i+1)
              println();
        }
        """
        expect = "Error on line 3 col 14: int"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_valid_for(self):
        input = """
        int foo() {
          for(1;true;3)
            a=a+1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_valid_for_1(self):
        input = """
        int foo() {
          for(a;b;c)
            break ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_valid_many_func(self):
        input = """
        int i ;
        int f ( ) {
        return 200;
        }
        void main ( ) {
            int main ;main = f ( ) ;putIntLn ( i ) ;
        {
            int i ;int main ;int f ;
            main = f = i = 100;
        }
            putIntLn(main);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_invalid_for_loop(self):
        input = """
        int foo() {
          for(;;)
            c=c;
        }
        """
        expect = "Error on line 3 col 14: ;"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_valid_program_(self):
        input = """
          int a;
          int main () {
             int b;
             b = a+3;
          }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_valid_index_stm(self):
        input = """
        int main() {
            !a[-3];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_valid_index_stm_2(self):
        input = """
        int main() {
            !a[b[m[7]]];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_valid_index_stm_(self):
        input = """
        int main() {
            -a[12];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_valid_index_stm_1(self):
        input = """
        int main() {
            -a[a[6]];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))



    def test_invalid_do_while_(self):
        input = """
        int foo() {
            do
              { }
            while();
        }
        """
        expect = "Error on line 5 col 18: )"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_invalid_do_while_2(self):
        input = """
        int foo() {
            do
              { }
            while({});
        }
        """
        expect = "Error on line 5 col 18: {"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_invalid_do_while_3(self):
        input = """
        int foo() {
            do
              a  = 1
            while(a<1);
        }
        """
        expect = "Error on line 5 col 12: while"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_valid_do_while__(self):
        input = """
        int foo() {
            do
            {}{}{}
            while(1);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_valid_do_while__1(self):
        input = """
        int foo() {
            do
            { 1; }{}{}
            while(1);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_invalid_arr(self):
        input = """
        int foo() {
          a=b[1][2];
        }
        """
        expect = "Error on line 3 col 16: ["
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_valid_program_(self):
        input = """
        int main(){
          int a;
          a = b && c + d;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_valid_program__(self):
        input = """
        int main(){
          int a;
          a = b && c + d && f || e;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_valid_program_1(self):
        input = """
        int main(){
          int a;
          a = 5<  (b <7);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_valid_program_2(self):
        input = """
        string upper(string arr, int n) {
          for (i = 0; i < n; i=i+1) {
            if (arr[i] >= "0" && arr[i] <= "9") continue;
            if (arr[i] >= "a" && arr[i] <= "z") {
              arr[i] = "A" - ("a" - arr[i]);
            }
          }
          return arr;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_valid_program_3(self):
        input = """
    boolean isIsomorphic(string s, string t) {
      if (s_length() != t_length())
            return false;

      dodai   = s_length();
      compare = "";
      for (i = 0; i < dodai; i=i+1) {
            compare = " ";
      }
      for (i = 0; i < dodai; i) {
            if (compare[i] != " ")
                  continue;
            for (j = i; j < dodai; j)
                  if (s[i] == s[j])
                        compare[j] = t[i];
      }
      return compare == t;
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_valid_program_4(self):
        input = """
      int main(){
       // Gia su mang co 5 phan tu
          int array[5],a;
        for (i = 0; i < 5; i)
        {
        cout("array[",i,"] = ");
        cin(array[i]);
        }
         for (i = 0; i < 5;i)
           cout(array[i]," ");

         for (i = 0; i < 2; i)
         {
            a = array[i];
            array[i] = array[4 - i];
            array[4 - i] = a;
        }
      system("pause");}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_valid_program_5(self):
        input = """
        int main(){
            print(arr[i]) ;
        }
  
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))


    def test_valid_program_6(self):
        input = """
        int main(){
            print((arr[i])[j]) ;
        }
  
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292)) 

    def test_valid_program_7(self):
        input = """
        int fibonacci(int N){
          if (N == 0) return  0;
          else if (N == 1) return 1;
          else return fibonacci(N - 1) + fibonacci(N - 2);
        }
          int main()
          {
            int N;N=0;
            for (i = 0; i < N; i)
              cout(fibonacci(i), " ");
            system("pause");
          }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_valid_program_8(self):
        input = """
        int a[10];
        void printArray(int begin, int end){
          if(begin < end){ 
            cout(a[begin]);
            printArray(begin + 1, end);
          }
        }
        int minimum(int b[], int begin, int end){
          if (begin < end){
            if (b[begin] < b[begin + 1]) 
               small = b[begin];
            minimum(b, begin + 1, end);
          }
          return small;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_valid_program_9(self):
        input = """
        void ngto(int a, int b){
        for (i = a; counter=0; i <= b)
          for (j = 2; j <= sqrt(i); j)
            if (i%j == 0) counter=couter+1;
          if (counter == 0 && i!=1) cout(i);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_valid_program_10(self):
        input = """
        void foo(float a [] ){ }
        void goo(float x[]) { 
          float y[10]; 
          int z [10]; 
          foo(x); //CORRECT 
          foo(y); //CORRECT 
          }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_valid_program_11(self):
        input = """
        boolean isLeapYear(int year){
          if (year < 0 )
            cout ("This is a invalid Year." ,endl);
          else
            if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))
              return true;
            else
              return false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_valid_program_12(self):
        input = """
        void many_for(){
          for (i = 0; i < 2; i)
            for (j = 0; j < 2; j)
              for (k = 0; k < 2; k)
                (c[i])[j] = (a[i])[k]*(b[k])[j];
          for (i = 0; i < 2; i){
            for (j = 0; j < 2; j)
              cout(c(i)[j]);
          }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))



    def test_valid_program_14(self):
        input = """
       boolean isPrime(int number){
        int i;
          if (number < 2) {
            return false;
          }
          for (i = 2; i*i <= number; i) {
            if (number % i == 0) return false;
          }
          return true;
        }
        void printPrime(int arr[], int N)
        {
          if (N == 0) return;
          else if (isPrime(arr))
              cout(arr);
          printPrime(arr+1, N-1);  
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))  

    def test_non_decl(self):
        input = """ Hello teacher!"""
        expect = "Error on line 1 col 1: Hello"
        self.assertTrue(TestParser.checkParser(input,expect,300))   

    def test_valid_program_15(self):
        input = """
        int main(){
            do { }
            while((arr[i])[j]);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,301))

    def test_invalid_var_decl_case1(self):
        input = """int a,b[]; """
        expect = "Error on line 1 col 8: ]"
        self.assertTrue(TestParser.checkParser(input,expect,302))




    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  