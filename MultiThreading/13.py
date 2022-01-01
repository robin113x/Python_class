
l=RLock()
def factorial(n):
    l.acquire()
    if n==0 or n==1:
        res=1
    else:
        res=n*factorial(n-1)
    l.release()
    return res

def results(n):
    print("factorail of {} is {}".format(n,factorial(n)))

t1=Thread(target=results,args=(5,))
t2=Thread(target=results,args=(4,))
t1.start()
t2.start()