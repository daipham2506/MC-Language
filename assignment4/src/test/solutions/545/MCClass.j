.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	ifle Label3
Label4:
	ldc "This is False"
	invokestatic io/putString(Ljava/lang/String;)V
Label5:
	goto Label2
Label3:
Label6:
	ldc "This is True"
	invokestatic io/putString(Ljava/lang/String;)V
Label7:
Label2:
	return
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
