.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static c F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is arr [F from Label0 to Label1
	bipush 10
	newarray float
	astore_3
Label0:
	bipush 10
	istore_1
	bipush 24
	istore_2
	bipush 32
	i2f
	putstatic MCClass/c F
	aload_3
	iconst_0
	iload_1
	iload_2
	imul
	i2f
	getstatic MCClass/c F
	fsub
	fastore
	aload_3
	iconst_0
	faload
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 8
.limit locals 4
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
