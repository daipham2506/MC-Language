.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	putstatic MCClass/x I
	getstatic MCClass/x I
	iconst_3
	if_icmpgt Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label2
	getstatic MCClass/x I
	iconst_1
	iadd
	putstatic MCClass/x I
	goto Label2
Label2:
	getstatic MCClass/x I
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 5
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
