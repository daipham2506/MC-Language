.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is arr [F from Label0 to Label1
	iconst_5
	newarray float
	astore_2
Label0:
	iconst_0
	istore_1
Label4:
Label5:
	iload_1
	iconst_1
	iadd
	istore_1
	aload_2
	iload_1
	iload_1
	iload_1
	imul
	i2f
	fastore
	ldc "arr["
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	invokestatic io/putInt(I)V
	ldc "] ="
	invokestatic io/putString(Ljava/lang/String;)V
	aload_2
	iload_1
	faload
	invokestatic io/putFloatLn(F)V
Label6:
Label2:
	iload_1
	iconst_4
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label4
Label3:
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
