.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x F from Label0 to Label1
Label0:
	iconst_1
	putstatic MCClass/a I
	ldc 0.1
	fstore_1
Label4:
Label5:
	getstatic MCClass/a I
	iconst_1
	iadd
	putstatic MCClass/a I
Label6:
Label7:
	fload_1
	iconst_1
	i2f
	fadd
	fstore_1
Label8:
Label2:
	getstatic MCClass/a I
	bipush 10
	if_icmpge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label4
Label3:
	getstatic MCClass/a I
	invokestatic io/putIntLn(I)V
	fload_1
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 7
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
