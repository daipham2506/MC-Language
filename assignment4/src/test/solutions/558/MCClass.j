.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo(IF)F
.var 0 is a I from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	iload_0
	i2f
	fload_1
	fsub
	freturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x F from Label0 to Label1
Label0:
	bipush 6
	ldc 1.5
	invokestatic MCClass/foo(IF)F
	fstore_1
	fload_1
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 2
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
