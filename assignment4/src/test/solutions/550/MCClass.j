.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I
.field static x I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_2
	putstatic MCClass/x I
	iconst_2
	istore_1
Label4:
	iload_1
	iconst_0
	if_icmplt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	getstatic MCClass/arr [I
	iload_1
	getstatic MCClass/x I
	iload_1
	imul
	iastore
Label8:
Label2:
	iload_1
	iconst_1
	isub
	istore_1
	goto Label4
Label3:
	getstatic MCClass/arr [I
	iconst_1
	iaload
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 9
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
	iconst_3
	newarray int
	putstatic MCClass/arr [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
