.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static gcd(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_1
	iconst_0
	if_icmpne Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label2
Label5:
	iload_0
	ireturn
Label6:
Label2:
	iload_1
	iload_0
	iload_1
	irem
	invokestatic MCClass/gcd(II)I
	ireturn
Label1:
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "GCD of 9 and 6: "
	invokestatic io/putString(Ljava/lang/String;)V
	bipush 9
	bipush 6
	invokestatic MCClass/gcd(II)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
