.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass/a [Z
	iconst_1
	iconst_1
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iconst_1
	ior
	bastore
	getstatic MCClass/a [Z
	iconst_1
	baload
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 15
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
	iconst_5
	newarray boolean
	putstatic MCClass/a [Z
Label1:
	return
.limit stack 1
.limit locals 0
.end method
