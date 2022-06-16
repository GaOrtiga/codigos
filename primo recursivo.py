def primo(N,Nmax):
    if N>Nmax:
        print(v)
        return v;
    
    ehprimo = True
    max = int(N**(1/2))
    for i in range(2,max+1,2):
        if N%i==0:
            ehprimo = False
            break
    if ehprimo == True:
        v.append(N)
    
    primo(N+1,Nmax)
    
n = int(input())
if n<1:
    return "entrada invalida"
    
v= []

primo(1,n)