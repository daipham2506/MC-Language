.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo()F
Label0:
	ldc 5.2
	freturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x F from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	ldc 7.2
	fstore_1
	iconst_0
	istore_2
Label4:
Label5:
	iload_2
	iconst_1
	iadd
	istore_2
	iload_2
	i2f
	invokestatic MCClass/foo()F
	fcmpl
	ifle Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iload_2
	i2f
	fload_1
	fcmpl
	ifge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	iand
	ifle Label7
	goto Label2
	goto Label7
Label7:
	iload_2
	invokestatic io/putInt(I)V
Label6:
Label2:
	iload_2
	bipush 10
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label4
Label3:
Label1:
	return
.limit stack 10
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
