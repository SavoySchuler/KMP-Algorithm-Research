def KMP(T, P):

    #initialize local variables

    matchFound = 0                  #count number of matches found
    n = len(T)                      #length of text
    m = len(P)                      #length of pattern
    PMT = PrefixFunc(P)             #partial matches table    
    q = 0                           #number of characters matched

    #display prefix table for user

    print ("\n\nPrefix table: ")
    for i in range(len(PMT)):
        print (PMT[i])  

    #verify pattern and text lengths to user

    print ("\nLength Pattern: " + str(m))
    print ("Length Text: " + str(n)+"\n")   
 
    #begin searching string for matches    
  
    for i in range(n-1):                    #scan text from left to right
        while q > 0 and P[q] != T[i+1]:     #while next char does not match
            q = PMT[q]                      #use table to "jump" # char matches
        if P[q] == T[i+1]:                  #when next character does match
            q = q + 1                       #increment # of char matches by 1
        if q == m:                          #if all characters in pattern found
            matchFound = matches found + 1  #update number of matches
            #output location of match and number of char shifts needed to find            
            print ("Pattern occurs at the " + str(i+2-m) \
                + " position. Shift = " + str(i + 1 - m) )  
            q = PMT[q-1]                    #look for next match
    
    #conclude search
    #finish function with conditional output

    if matchFound == 0:             #if no matches found...
        print ("\nNo match!\n")     #inform userno matches were found
    else:                           #if matches were found...
        print ("\n")                #print separator for formatting 



def PrefixFunc(Pattern): 

    #initialize local variables

    m = len(Pattern)    #store length of patterm
    PMT = []            #table for prefix = suffix lengths in pattern 
                        #used for partial match "jumps" in full string search
    k = 0               #number of characters in pattern matched

    #initialize values of partial matches table

    for i in range(m):      #for length of the pattern...
        PMT.append(i+1)     #set each index to its 1-indexed location
    PMT[0] = 0              #set index of first character in pattern to zero

    #create table for prefix = suffix partial match jumps

    for q in range(m-1):                #for 1-index number of chars in pattern
        while k > 0 and P[k] != P[q+1]: #while char and index char do not match
            k = PMT[k]                  #use table to "jump" # of char matches
        if P[k] == P[q+1]:              #when indexed char does match
            k = k + 1                   #increment number of char matches by 1
        PMT[q+1] = k                    #update table with # of matched chars
                                        
    #this table will reflect the number of characters the search can skip ahead
        # when a partial mismatch occurs
    
    #return the table of partial matches to be used in search

    return PMT      

KMP("ACTGACGTACGTACGTACGTACGTACTG", "ACGTACGT")
