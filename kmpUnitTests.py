from kmp import *

def tests():
    i = 1
    results = []
    expected = []
    successes = 0 
    failures = 0


    print("Running test: " + str(i))
    print("Text: A")
    print("Pattern: A")
    results.append (KMP("A", "A"))
    expected.append (1)


    print("Running test: " + str(i))
    print("Text: A")
    print("Pattern: C")
    results.append (KMP("A", "C"))
    expected.append (0)

    print("Running test: " + str(i))
    print("Text: AG")
    print("Pattern: A")
    results.append (KMP("AG", "A"))
    expected.append (1)

    print("Running test: " + str(i))
    print("Text: AG")
    print("Pattern: G")
    results.append (KMP("AG", "G"))
    expected.append (1)


    print("Running test: " + str(i))
    print("Text: AG")
    print("Pattern: AG")
    results.append (KMP("AG", "AG"))
    expected.append (1)

    print("Running test: " + str(i))
    print("Text: AG")
    print("Pattern: AGC")
    results.append (KMP("AG", "AGC"))
    expected.append (0)

    print("Running test: " + str(i))
    print("Text: AG")
    print("Pattern: C")
    results.append (KMP("AG", "C"))
    expected.append (0)


    print("Running test: " + str(i))
    print("Text: AGA")
    print("Pattern: A")
    results.append (KMP("AGA", "A"))
    expected.append (2)
    

    print("Running test: " + str(i))
    print("Text: AGA")
    print("Pattern: G")
    results.append (KMP("AGA", "G"))
    expected.append (1)

    print("Running test: " + str(i))
    print("Text: AGA")
    print("Pattern: AG")
    results.append (KMP("AGA", "AG"))
    expected.append (1)

    print("Running test: " + str(i))
    print("Text: AGA")
    print("Pattern: GA")
    results.append (KMP("AGA", "GA"))
    expected.append (1)


    print("Running test: " + str(i))
    print("Text: ACTGACGTACGTACGTACGTACGTACTG")
    print("Pattern: ACGTACGT")
    results.append (KMP("ACTGACGTACGTACGTACGTACGTACTG", "ACGTACGT"))
    expected.append (4)


    print ("\n\n RESULTS:\n\n")
    for i in range(len(results)):
        print ("Test " + str(i+1) +":")  
        if results[i]==expected[i]:
            successes = successes + 1
            print("        Success\n")
        else:
            failures = failures + 1
            print("                Failure\n")

    print("\n\nTOTAL RESULTS\n")
    print("Successes: " + str(successes))
    print("Failures: " + str(failures))
    print("\nEND UNIT TESTING")  
