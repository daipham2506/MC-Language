.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is a [F from Label0 to Label1
	iconst_5
	newarray float
	astore_2
.var 3 is b [I from Label0 to Label1
	iconst_5
	newarray int
	astore_3
Label0:
	iconst_1
	istore_1
	aload_3
	iconst_2
	iconst_2
	iastore
	aload_2
	iconst_2
	iconst_5
	i2f
	fastore
	aload_2
	aload_3
	iconst_2
	iaload
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
