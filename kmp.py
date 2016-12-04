'''******************************** kmp.py *************************************
	Final Project - Knuth-Morrus-Pratt String Matching Algorithm

    Application: DNA Pattern Matching

	Authors: Savoy Schuler

	Date: December 2, 2016

	Professor: Dr. Lisa Rebenitsch

	Course: CSC 372 - M001 Analysis of Algorithms

	System: Linux (Ubuntu tested)

	Usage Instructions: 

        Run:  python3 kmp.py <text> <pattern>
        Test: python3 kmp.py {-t} or {test} >> testResults.txt
        Help: python3 kmp.py {-h} or {help}

	Example Input: python3 kmp.py ACTGACGTACGTACGTACGTACGTACTG ACGTACGT

    Example Output:

        Prefix table: 
        0
        0
        0
        0
        1
        2
        3
        4

        Length Pattern: 8
        Length Text: 28

        Pattern starts at the 6 position. Shift = 4
        Pattern starts at the 10 position. Shift = 8
        Pattern starts at the 14 position. Shift = 12
        Pattern starts at the 18 position. Shift = 16

        Total number of matches found: 4

	Program Details:

        This program is an exercise in exploring the Knuth-Morris-Pratt (KMP) 
        string matching algorithm.

        The KMP algorithm is a string matching algorithm that improves upon 
        basic string matching algorithms by using a precomputed table of partial
        matches that contains indexes to the last element of each of the 
        pattern's internal partial matches to itself.

        Whenever the search encounters a partial match, it avoids redoing as 
        much computation as possible by skipping ahead to the last matching
        element of the first partial match of the pattern within itself. This
        allows the search to avoid comparing values that are already known to be
        mismatched or matched to values within the pattern.

        The KMP algorithm is divided into two parts:

            1. Compute a table of partial matches (PMT).

            2. Search text for a pattern using the PMT to handle partial 
            matches.

        Specifics on these two steps and their calculations can be found in 
        their corresponding functions below.  
        
    Runtime: 
    
        Worst case: O(M+N)
        Average case: O(M+N)
        
        Where M and N are the length of the pattern and the text, respectively. 


    Pseudocode used provided by:

        Introduction to Algorithms Third Edition (2009)

    Pseudocode authors:
    
        Thomas H. Cormen
        Charles E. Leiserson
        Ronald L. Rivest
        Clifford Stein

    File contents:

        KMP                     - KMP string search algorithm.
        PartialMatchesTable     - Function to compute KMP partial matches table.
        main                    - Simualted program main.

	Bugs: None
	
	Todo: None

    Modifications:

        None - Original.

*****************************************************************************'''

#program imports

import sys                  #for access to command line arguments
from kmpUnitTests import *  #for access to unit testing function


#functions

def KMP(T, P):  #T for text, P for pattern
    """
	Author: Savoy Schuler

    This is the second half of the KMP string search algorithm. It searches the
    passed in text for the passed in pattern using a precomputed table of
    pattern's internal matches to its prefix which is used to jump ahead as much
    as possible to the last matching element of the first partial match of the
    pattern within itself. This allows the search to avoid comparing values that
    are already known to be mismatched or matched to values within the pattern.
 
    The algorithm first performs its set up, including calling the
    PartialMatchesTable function compute the partial matches table (PMT). It 
    then moves into searching the text. It will brute force compare elements 
    until the first match is found. Once a match is found, it will begin 
    counting the number of matched characters. When the number of matched
    characters equals that of the length of the pattern, a successful match has
    been found. The match is declared to the user along with its location within
    the text and number of shifts needed to reach it; the search is indexed to 
    the last element of the first partial match within the pattern to continue
    the search - this allows finding matches that partial coincide with other
    matches. If a mismatch occurs however, the algorithm indexes its search to 
    the value contained with the PMT indexed by the current number of matched
    characters. 

    Args:

        T   - Text that is to be searched for pattern
        P   - Pattern being searched for in text.

    Calls:
		
        PartialMatchesTable     - Function to compute and return table 
                                containing indices of last element of the 
                                partial match's first internal match to the 
                                prefix of the pattern. 

    Passes:
    
        matches     - Number of pattern matches found within text. Used in tests 
                    function for evaluating success of unit tests.

    """

    #initialize local variables

    matches = 0                     #count number of matches found
    n = len(T)                      #length of text
    m = len(P)                      #length of pattern
    PMT = PartialMatchesTable(P)             #partial matches table    
    q = 0                           #number of characters matched

    #display prefix table for user

    print ("\nPrefix table: ")
    for i in range(len(PMT)):
        print (PMT[i])  

    #verify pattern and text lengths to user

    print ("\nLength Pattern: " + str(m))
    print ("Length Text: " + str(n)+"\n")   
 
    #begin searching string for matches    
    
    for i in range(n):                      #scan text from left to right
        while q > 0 and P[q] != T[i]:       #while next char does not match
            q = PMT[q-1]                      #use table to "jump" # char matches
        if P[q] == T[i]:                    #when next character does match
            q = q + 1                       #increment # of char matches by 1
        if q == m:                          #if all characters in pattern found
            matches = matches + 1  #update number of matches
            #output location of match and number of char shifts needed to find
            print ("Pattern starts at the " + str(i+3-m) \
                + " position. Shift = " + str(i + 1 - m) )  
            q = PMT[q-1]                    #look for next match
    
    #conclude search
    #finish function with conditional output

    if matches == 0:             #if no matches found, inform user
        print ("\nNo match!\n")     
    else:                           #if matches were found, print total number
        print ("\nTotal number of matches found: " + str(matches) + "\n")
    return matches 



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

    This function is a simulated program main used for handling command line 
    input and KMP string search call. 

    If all parameters are passed, KMP will be called on the provided parameters.
    
    If no parameters are passed or just one is passed, the user will be prompted 
    for full input. This input will then be passed on to the KMP algorithm. 

    If '-t' or 'test' is passed as the first command line parameter, a unit test
    testing function will be called to run empirical tests on the algorithm and
    return results analysis to the user. It is suggest to the user to differ
    output to a file using the >> console macro, but the option receive it in 
    the terminal is allowed. 

    If 'h' or 'help' is passed as the first command line parameter, the main 
    will not call the KMP search, but will instead print usage instructions to 
    the terminal. 

    Args:

        None.

    Calls:
		
        KMP     - String search algorithm
        tests   - Function for unit testing search algorithm function. 

    Passes:
    
        Text    - Text that is to be searched for pattern.
        Pattern - Pattern being searched for in text.
    """

    if len(sys.argv) == 3:      #if full command line parameters entered
        Text = sys.argv[1]      #set text
        Pattern = sys.argv[2]   #set pattern
        KMP (Text, Pattern)     #call KMP search
    
    elif len(sys.argv) == 2:    #if flag set, check if for test, default to help
        if sys.argv[1] == 'test' or sys.argv[1] == '-t':    #if flag for testing
            tests()             #call function to run prewritten unit tests
        else:                   #any other, default to help for usage
            print("\nUsages:")  #list usage call types
            print("Run:  python3 kmp.py <text> <pattern>")
            print("Test: python3 kmp.py {-t} or {test} >> testResults.txt")
            print("Help: python3 kmp.py {-h} or {help}\n")
    else:                       #if no parameters passed, enter user input mode
        Text = input("\nPlease enter text to be searched: \n\n")
        Pattern = input("\nPlease enter pattern to search for: \n\n") 
        KMP (Text, Pattern)     #call KMP on user input
