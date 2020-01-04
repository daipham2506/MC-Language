.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass/arr [Z
	iconst_0
	iconst_0
	bastore
	getstatic MCClass/arr [Z
	iconst_1
	iconst_1
	bastore
	getstatic MCClass/arr [Z
	iconst_1
	ifle Label2
Label3:
	ldc "This is ArrayCell True"
	invokestatic io/putString(Ljava/lang/String;)V
Label4:
	goto Label2
Label2:
Label1:
	return
.limit stack 10
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
	iconst_2
	newarray boolean
	putstatic MCClass/arr [Z
Label1:
	return
.limit stack 1
.limit locals 0
.end method
