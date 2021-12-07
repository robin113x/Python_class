#!bin/python3

def fun(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)
    return
fun(3,2)
fun(10,20,30,50)
fun(25,50,arg4=100)
fun(arg2=85,arg1=888,arg4=999)

fun() #----> required two postional arguments
fun(arg3=40,arg4=9999,5,96321) #---> after keywords arguments we can't take postional arguments

fun(4,5,arg2=6) #--> we can't provide two value for a single arguments

fun(4,5,arg5=10) #---> invalid arguments
