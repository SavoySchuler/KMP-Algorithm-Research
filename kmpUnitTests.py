'''***************************** kmpUnitTests.py *******************************
	File: kmpUnitTests.py

    Author: Savoy Schuler

    Date: December 2, 2016

	Bugs: None
	
	Todo: None

	File Details:

        This file contains a single function filled with unit tests made for
        evaulating the success of the implemented KMP string matching algorithm. 

    File Contents:

        tests()     - function to call and evaluate prewritten unit tests

    Modifications:

        None - Original

*****************************************************************************'''

#program imports

from kmp import *   #for access to KMP and PartialMatchesTable functions

#unit testing function

def tests():
    """
	Author: Savoy Schuler

    This function is designed to repeatingly call the KMP algorithm on multiple,
    prewritten unit tests. The funciton will evaluate the success of the tests
    and print test pass/fail and total success/failure information to the 
    terminal.

    Args: 

        None

    Calls: 
    
        KMP(Text, Pattern) -    Function that evaluates number of pattern 
                                matches inside text.                             

    Passes:
    
        None    - only terminal output regarding success of tests

    """    
    #initialize local variables

    i = 1               #test number, incremented after each test
    results = []        #list of matches found in each test
    expected = []       #list of expected number of matches in each test
    successes = 0       #number of successful tests
    failures = 0        #number of failed tests

    #include a reasonably longer DNA strand:
   
    longDnaStrand = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

    #conduct tests - structured to allow flexible ordering and additional test
   
    print("Running test: " + str(i))    #inform user of test number
    print("Text: A")                    #inform user of test text
    print("Pattern: A")                 #inform user of test pattern
    results.append (KMP("A", "A"))      #store results of KMP search on test
    expected.append (1)                 #manually set expected results
    i = i + 1                           #increment test number


    print("Running test: " + str(i))
    print("Text: A")
    print("Pattern: C")
    results.append (KMP("A", "C"))
    expected.append (0)
    i = i + 1


    print("Running test: " + str(i))
    print("Text: AG")
    print("Pattern: A")
    results.append (KMP("AG", "A"))
    expected.append (1)
    i = i + 1


    print("Running test: " + str(i))
    print("Text: AG")
    print("Pattern: G")
    results.append (KMP("AG", "G"))
    expected.append (1)
    i = i + 1


    print("Running test: " + str(i))
    print("Text: AG")
    print("Pattern: AG")
    results.append (KMP("AG", "AG"))
    expected.append (1)
    i = i + 1


    print("Running test: " + str(i))
    print("Text: AG")
    print("Pattern: AGC")
    results.append (KMP("AG", "AGC"))
    expected.append (0)
    i = i + 1


    print("Running test: " + str(i))
    print("Text: AG")
    print("Pattern: C")
    results.append (KMP("AG", "C"))
    expected.append (0)
    i = i + 1


    print("Running test: " + str(i))
    print("Text: AGA")
    print("Pattern: A")
    results.append (KMP("AGA", "A"))
    expected.append (2)
    i = i + 1

    
    print("Running test: " + str(i))
    print("Text: AGA")
    print("Pattern: G")
    results.append (KMP("AGA", "G"))
    expected.append (1)
    i = i + 1


    print("Running test: " + str(i))
    print("Text: AGA")
    print("Pattern: AG")
    results.append (KMP("AGA", "AG"))
    expected.append (1)
    i = i + 1


    print("Running test: " + str(i))
    print("Text: AGA")
    print("Pattern: GA")
    results.append (KMP("AGA", "GA"))
    expected.append (1)
    i = i + 1


    print("Running test: " + str(i))
    print("Text: ACTGACGTACGTACGTACGTACGTACTG")
    print("Pattern: ACGTACGT")
    results.append (KMP("ACTGACGTACGTACGTACGTACGTACTG", "ACGTACGT"))
    expected.append (4)


    #run tests with longer DNA strand


    print("Running test: " + str(i))
    print("Text: " + longDnaStrand)
    print("Pattern: AGA")
    results.append (KMP(longDnaStrand, "AGA"))
    expected.append (6)


    print("Running test: " + str(i))
    print("Text: " + longDnaStrand)
    print("Pattern: GAGG")
    results.append (KMP(longDnaStrand, "GAGG"))
    expected.append (3)


    #Print out results of unit testing.

    print ("\n\n RESULTS:\n\n")
    for test in range(len(results)):
        print ("Test " + str(test+1) +":")  
        if results[test]==expected[test]:
            successes = successes + 1
            print("        Success\n")
        else:
            failures = failures + 1
            print("                Failure\n")

    print("\n\nTOTAL RESULTS\n")
    print("Successes: " + str(successes))
    print("Failures: " + str(failures))
    print("\nEND UNIT TESTING")  
