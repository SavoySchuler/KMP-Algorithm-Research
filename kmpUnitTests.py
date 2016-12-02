from kmp import *

def tests():
    
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


    #run tests with a reasonably longer DNA strand


    print("Running test: " + str(i))
    print("Text: " + longDnaStrand)
    print("Pattern: AGA")
    results.append (KMP(longDnaStrand, "AGA"))
    expected.append (6)


    print("Running test: " + str(i))
    print("Text: " + longDnaStrand)
    print("Pattern: GAGG")
    results.append (KMP(longDnaStrand, "GAGG"))
    expected.append (4)


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
