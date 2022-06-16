def testeprimo(n):
    ehprimo = True
    max = int(n**(1/2))
    for i in range(3,max+1,2):
        if n%i==0:
            ehprimo = False
            break
    if ehprimo == True:
        v.append(n)
        
def primo(n):

    
    if N==1:
        return [1]
    if N==2:
        return [1,2]


    for i in range(2):
        v.append(i+1)

    for i in range(3,N+1,2):
        testeprimo(i)
    return(v)



N = int(input())
if N<1:
    return "entrada invalida"
v=[]
primo(N)
            
