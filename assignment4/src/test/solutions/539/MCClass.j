.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo(I)I
.var 0 is a I from Label0 to Label1
Label0:
Label4:
Label5:
Label6:
Label7:
	iload_0
	iconst_2
	iadd
	istore_0
Label8:
	iload_0
	ireturn
Label9:
Label10:
Label2:
	iload_0
	iconst_3
	if_icmpge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label4
Label3:
Label1:
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	invokestatic MCClass/foo(I)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 1
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
