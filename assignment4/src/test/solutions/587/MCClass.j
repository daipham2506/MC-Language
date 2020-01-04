.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I

.method public static f()I
Label0:
	sipush 200
	ireturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is main I from Label0 to Label1
Label0:
	invokestatic MCClass/f()I
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
.var 2 is main I from Label2 to Label3
.var 3 is f I from Label2 to Label3
.var 4 is i I from Label2 to Label3
Label2:
	bipush 100
	dup
	istore 4
	dup
	istore_3
	istore_2
	iload_2
	invokestatic io/putIntLn(I)V
	iload_3
	invokestatic io/putIntLn(I)V
	iload 4
	invokestatic io/putIntLn(I)V
Label3:
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
.limit locals 5
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
