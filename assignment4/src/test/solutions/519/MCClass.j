.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iconst_1
	ireturn
Label3:
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MCClass/foo(I)I
	imul
	ireturn
Label2:
Label1:
.limit stack 5
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
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
