def KMP(T, P):
    matchFound = 0
    n = len(T)
    m = len(P)
    o = PrefixFunc(P)

    print ("\n\nPrefix table: ")
    for i in range(len(o)):
        print (o[i])  


    print ("\nLength Pattern: " + str(m))
    print ("Length Text: " + str(n)+"\n")   
 

    q = 0
    for i in range(n-1):  
        while q > 0 and P[q] != T[i+1]:
            q = o[q]
        if P[q] == T[i+1]:
            q = q + 1
        if q == m:
            matchFound = 1
            print ("Pattern occurs at the " + str(i + 2 - m) +
" position. Shift = " + str(i + 1 - m))      
            q = o[q-1]
  
    if matchFound == 0:
        print ("\nNo match!\n")
    else:
        print ("\n")

def PrefixFunc(P): 
    m = len(P)
    o = []
    for i in range(m):
        o.append(i+1)
    o[0] = 0
    k = 0
    for q in range(m-1):
        while k > 0 and P[k] != P[q+1]:
            k = o[k]
        if P[k] == P[q+1]:
            k = k + 1      
        o[q+1] = k
    return o

KMP("abacabacabacabacd", "ac")


