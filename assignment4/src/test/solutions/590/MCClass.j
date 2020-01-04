.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo(I)[I
.var 0 is n I from Label0 to Label1
.var 1 is arr [I from Label0 to Label1
	iconst_3
	newarray int
	astore_1
Label0:
	aload_1
	areturn
Label1:
.limit stack 1
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is a [I from Label0 to Label1
	iconst_5
	newarray int
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
	iastore
	iconst_3
	invokestatic MCClass/foo(I)[I
	iconst_1
	iload_1
	iadd
	aload_2
	aload_3
	iconst_2
	iaload
	iaload
	iconst_3
	iadd
	iastore
	iconst_3
	invokestatic MCClass/foo(I)[I
	iconst_1
	iload_1
	iadd
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 12
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
