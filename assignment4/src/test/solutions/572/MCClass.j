.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
	iconst_2
	istore_1
	bipush 10
	istore_2
	iload_1
	iload_2
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_1
	bipush 10
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	iload_1
	iload_2
	iadd
	istore_1
	goto Label6
Label7:
	iload_1
	iconst_2
	iload_2
	imul
	iadd
	istore_1
Label6:
	goto Label2
Label3:
	iload_1
	bipush 10
	if_icmple Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	iload_1
	iload_2
	isub
	istore_1
	goto Label10
Label11:
	iload_1
	iconst_2
	iload_2
	imul
	isub
	istore_1
Label10:
Label2:
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 14
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
