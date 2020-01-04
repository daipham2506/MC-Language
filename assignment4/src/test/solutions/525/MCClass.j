.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is s I from Label0 to Label1
Label0:
	iconst_1
	istore_2
	iconst_1
	istore_1
Label4:
Label5:
	iload_2
	iload_1
	imul
	istore_2
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	bipush 6
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	goto Label3
	goto Label7
Label7:
Label6:
Label2:
	iload_2
	sipush 1000
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label4
Label3:
	iload_2
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 9
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
