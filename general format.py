#define function------------
def funcname(param):

    return ()

#main fcn-----------------------------------------------
import time as t
t1=t.time()

param=[]
print( funcname(param) )

t2=t.time()
print(f"{1000*(t2-t1)}ms")#execution time in ms----------