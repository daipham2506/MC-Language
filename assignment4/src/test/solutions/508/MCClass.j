.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is a I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_1
	istore_2
Label4:
Label5:
	iload_2
	iconst_2
	iadd
	istore_2
	iload_2
	iload_1
	iconst_2
	isub
	iconst_5
	imul
	bipush 7
	irem
	iadd
	istore_1
Label6:
Label2:
	iload_2
	bipush 20
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label4
Label3:
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 7
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
