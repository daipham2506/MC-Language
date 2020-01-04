.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo()F
.var 0 is i I from Label0 to Label1
.var 1 is arr [F from Label0 to Label1
	iconst_5
	newarray float
	astore_1
Label0:
	iconst_0
	istore_0
Label4:
	iload_0
	iconst_5
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	aload_1
	iload_0
	bipush 10
	iload_0
	isub
	i2f
	fastore
Label8:
Label2:
	iload_0
	iconst_1
	iadd
	istore_0
	goto Label4
Label3:
	aload_1
	iconst_2
	faload
	freturn
Label1:
.limit stack 8
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
Label0:
	invokestatic MCClass/foo()F
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
