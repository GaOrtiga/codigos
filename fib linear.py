def fib(n): 
    n1=0
    n2=1
    n3=1
    if n==0:
        return 0
    for i in range(n-1):
        n3=n1+n2
        n1=n2
        n2=n3
    return n3
    
N = int(input())

if N<0:
    return "entrada invalida"
    
fib(N)
        
        