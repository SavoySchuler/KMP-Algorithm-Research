'''**************************** kmpTiming.py ***********************************
	File: kmpTiming.py

    Author: Savoy Schuler

    Date: December 2, 2016

    Usage: 

        python3 kmpTiming.py

	File Details:

        This file is designed for clocking and storing the runtime of the KMP
        algorithm on variable length text inputs in milliseconds.
    
        This file, for the most part, is a copy of the kmp.py file. All of the  
        prints have been removed to allow for more accurate timing of the KMP
        algorithm. The simluated main has been changed to iteratively call the
        KMP on variable length text inputs and write the results to a file. The
        KMP function has been modified to include timing. 

    Timing unit:    

        milliseconds (msec)

    Timing results stored in:

        timingResults.txt

    File Contents:

        timingKMP               - Timingversion of KMP string search algorithm.
        PartialMatchesTable     - Function to compute KMP partial matches table.
        main                    - Simualted program main for timing program.
 
	Bugs: None
	
	Todo: None

    File modifications:

        None - Original

*****************************************************************************'''

#program imports

import sys                  #for access to command line arguments
import time
from kmpUnitTests import *  #for access to unit testing function


#functions

def timingKMP(T, P):  #T for text, P for pattern
    """
	Author: Savoy Schuler

    This is the timing version of the KMP algorithm from kmp.py.

    Args:

        T   - Text that is to be searched for pattern
        P   - Pattern being searched for in text.

    Calls:
		
        PartialMatchesTable     - Function to compute and return table 
                                containing indices of last element of the 
                                partial match's first internal match to the 
                                prefix of the pattern. 

    Passes:
    
        (endTime - startTime)   - The algorithm's run time.
    """

    #start timing
    
    timeStart = time.clock()


    #initialize local variables

    matches = 0                     #count number of matches found
    n = len(T)                      #length of text
    m = len(P)                      #length of pattern
    PMT = PartialMatchesTable(P)             #partial matches table    
    q = 0                           #number of characters matched  
 
    #begin searching string for matches    
    
    for i in range(n):                      #scan text from left to right
        while q > 0 and P[q] != T[i]:       #while next char does not match
            q = PMT[q-1]                      #use table to "jump" # char matches
        if P[q] == T[i]:                    #when next character does match
            q = q + 1                       #increment # of char matches by 1
        if q == m:                          #if all characters in pattern found
            matches = matches + 1           #update number of matches
            q = PMT[q-1]                    #look for next match
    
    #conclude search, end timing

    timeEnd = time.clock()

    return (timeEnd-timeStart) 



def PartialMatchesTable(P):  #P for pattrn
    """
	Author: Savoy Schuler

    In string matching algorithms, it is commonly neglected that a pattern being
    searched for may contain within itself subsegments that match its prefix. 

    The PartialMatchesTable is the first half of the the KMP search algorihm. As
    its name implies, it computes a table of 'internal pattern segment' == 
    'pattern prefix' lengths. 

    Precomputing this table allows the KMP algoritm to greatly improve upon 
    preceding string matching algorithms by avoiding recomparing elements of a 
    partial match and instead jump to the last element of the first partial 
    submatch within the partially matched string segment.

    The 'trick' of the process is the fact that the 'partial matches table' 
    (PMT) is really an indexible table of indices to jump back within the 
    pattern itself to find that last element of first internal pattern match of
    itself. This function performs the calculation of that table by first 
    creating a list of elements 1 to the length of elements in the pattern 
    string (followed by reseting the first element to 0). Once this list is
    built, the function will move into a for loop with three options: First, 
    while the current number of elements matched is greater than zero and 
    previously referred to elements do not match, set the current number of
    elements matched so far to the value in the pattern index by the current
    number of elements matched so far (the jump back); If the element at the 
    pattern indexed by the number of elements matched so far equals the element 
    of the pattern indexed by the interation count, add 1 to the number of 
    elements matched so far; If neither of these two conditions are met, set the
    value of the PMT indexed by the current iteration to be the number of 
    elements matched so far. This is all that is needed to compute the PMT 
    table. Return it to the KMP search for use. 

    Args:

        P       - The pattern being searched for withing a larger body of text.   
 
    Calls:
		
        None.

    Passes:

        PMT     - Table of 'internal pattern segment' == 'pattern prefix' 
                lengths. Can be used to index a partially matched string the 
                last element of the pattern's first internal prefix match.
    """

    #initialize local variables

    m = len(P)  #store length of patterm
    PMT = []    #table of pattern's internal partial match to prefix lengths
    k = 0       #internal partial match to prefix length (chars matched so far)

    #initialize values of partial matches table

    for i in range(m):      #for length of the pattern...
        PMT.append(i+1)     #set each index to its 1-indexed location
    PMT[0] = 0              #set index of first character in pattern to zero

    #create table of pattern's internal partial matches to its prefix

    for q in range(m-1):                #for 1-indexed # of chars in pattern
        while k > 0 and P[k] != P[q+1]: #while char and index char do not match
            k = PMT[k-1]                  #jump count to last element of first
                                            #internal match back in current
        if P[k] == P[q+1]:              #when indexed char does match next
            k = k + 1                   #increment number of char matches by 1
        PMT[q+1] = k                    #update table with # of matched chars
                                        
    #this table will now reflect the number of characters the search can skip 
        # ahead when a partial mismatch occurs
    
    #return the table of partial matches to be used in search

    return PMT      



if __name__ == '__main__':
    """
	Author: Savoy Schuler

    This function is a simulated program main used for timing the KMP algorithm 
    and storing the results in the timingResults.txt output file.

    If all parameters are passed, the timing version of the KMP will be called 
    on the provided parameters.
    
    If no parameters the timing version of the KMP will run on variable length 
    input from 0 to 1000.

    One argument is passed as a command line parameter, usage will be printed.

    Args:

        None.

    Calls:
		
        KMP     - String search algorithm

    Passes:
    
        Text    - Text that is to be searched for pattern.
        Pattern - Pattern being searched for in text.
    """
    
    #set up array to store run times      
  
    runTimes = []

    #open file to store results of variable length input timing    

    timingResults = open('timingResults.txt', 'w')

    #allow user to call help -> program print usage    

    if len(sys.argv) > 1:    #default all one parameter calls to display use
            print("\nUsages:") 
            print("Run:  python3 kmpTiming.py")
            print("Help: python3 kmpTiming.py {-h} or {help}\n")
    
    #run KMP timing program on variable length input
    #write results to file

    else:                       
        Text = ""                   #intial text state
        Pattern = "AAGAA"           #default search pattern for timing

        for i in range(1000):       #test on test lengths 0 to 1000
            
            if (i+1)%3 == 0:        #every third character, append a 'g'
                Text = Text + "G"        
            else:            
                Text = Text + "A"   #non x%3==0 iterations, append 'a' to text
            runTimes.append(timingKMP (Text, Pattern))  #call timing KMP

        for i in runTimes:          #write all run times to file
            timingResults.write(str(i*1000) + "\n")
       
    #close results file

    timingResults.close()
