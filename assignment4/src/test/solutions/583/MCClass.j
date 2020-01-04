.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Z from Label0 to Label1
.var 2 is b Z from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iload_1
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iconst_1
	iand
	istore_2
	iload_2
	iconst_1
	if_icmpeq Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label6
Label9:
	ldc "This is False"
	invokestatic io/putString(Ljava/lang/String;)V
Label10:
	goto Label6
Label6:
	return
Label1:
	return
.limit stack 16
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
