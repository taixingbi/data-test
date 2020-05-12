'''
------------------------------------------------------------
WER calculation with Levenshtein distance
PP, TL, Apr 20
------------------------------------------------------------
'''
import word_error_rate as wer
import argparse
import re
'''
------------------------------------------------------------
Name : wercheck
Purpose : checks that the wer calculation works as expected
        for a reference test case
Parameters : none
Returns : True : wer performs as expected
        False: wer has issues therefore can not be used
------------------------------------------------------------
'''
def wercheck ():
    r = ['In', 'computational', 'linguistics', 'and', 'computer', 'science', ',', 'edit', 'distance', 'is', 'a', 'way', 'of', 'quantifying', 'how', 'dissimilar', 'two', 'strings', 'are', 'to', 'one', 'another', 'by', 'counting', 'the', 'minimum', 'number', 'of', 'operations', 'required', 'to', 'transform', 'one', 'string', 'into', 'the', 'other.', 'Edit', 'distances', 'find', 'applications', 'in', 'natural', 'language', 'processing,', 'where', 'automatic', 'spelling', 'correction', 'can', 'determine', 'candidate', 'corrections', 'for', 'a', 'misspelled', 'word', 'by', 'selecting', 'words', 'from', 'a', 'dictionary', 'that', 'have', 'a', 'low', 'distance', 'to', 'the', 'word', 'in', 'question']
    h = ['In', 'linguistics', 'and', 'computer', 'science', 'theory', ',', 'edit', 'distance', 'iss', 'a', 'way', 'of', 'quantifying', 'how', 'dissimilar', 'the', 'two', 'string', 'is', 'to', 'one', 'another', 'by', 'counting', 'the', 'number', 'of', 'operations', 'required', 'to', 'transform', 'one', 'string', 'into', 'the', 'other.', 'Edit', 'distances', 'find', 'applications', 'in', 'natural', 'language', 'processing,', 'where', 'automatic', 'spelling', 'correction', 'can', 'determine', 'candidate', 'corrections', 'for', 'a', 'misspelled', 'word', 'by', 'selecting', 'words', 'from', 'a', 'dictionary', 'that', 'have', 'a', 'low', 'distance', 'to', 'the', 'words', 'in', 'question']
    REFERENCE_WER = '10.9589'
    werresult=wer.get_word_error_rate(r, h)
    TestWer = '{0:<6.6}'.format(werresult)
    if REFERENCE_WER == TestWer :
      return True
    else:
      return False
'''
------------------------------------------------------------
Name : getargs
Purpose : gets and parses command line arguments
Parameters : none
Returns : reference_name : mane of the file with rerence
        results_name : name of the file with results
------------------------------------------------------------
'''
def getargs():
  parser = argparse.ArgumentParser()
  parser.add_argument ("reference_name", help="name of the text reference file (input)")
  parser.add_argument ("results_name", help="name of the ASR results file (input)")
  parser.add_argument ("wer_name", help="name of the WER results file (output)")
  parser.add_argument ("skip_opt", help="option to skip first item in the list (1=enabled)")
  args = parser.parse_args()
  return args.reference_name, args.results_name, args.wer_name, args.skip_opt
'''
------------------------------------------------------------
Name : loadrefres
Purpose : loads a reference or an asr result from file
Parameters : input file filename
Returns : a list containing the file items
------------------------------------------------------------
'''
def loadrefres (filename):
    result = []
    with open(filename) as file :
        for line in file:
            line = line.strip()                    # removes trailing spaces
            linesub = re.sub(r"[\t\n]",' ', line)  # removes tabs end of lines
            linesub = re.sub(rf"[{'-+±#$*%@<>(),:;.!?=^'}]", "", linesub) # removes punctuation
            linesub = linesub.lower()              # lowercase all
            linelist = linesub.split()             # build a list of tokens
            result.append(linelist)                # append list to output resu
    file.close()
    return result

'''
------------------------------------------------------------
Name : calcwer
Purpose : calculates word_error_rate
Parameters : refs : reference list
             ress : results lists
             skipopt : option to skip first item in list
               ( this to be used when both reference and result
                 lists have the number or name of the file
                 added to beginning of the list)
Returns : a list containing wer calculations
------------------------------------------------------------
'''
def calcwer (refs, ress, skip_opt):
    werresult=[]
    for i in range (len(refs)):
        if skip_opt == "1":
            tmp = refs[i]
            h=tmp[1:]
            tmp = ress[i]
            r=tmp[1:]
        else:
            h=refs[i]
            r=ress[i]
        werresult.append(wer.get_word_error_rate(h,r))
    return werresult

'''
------------------------------------------------------------
Name : savewer
Purpose : saves wer calculation to file
Parameters : wer results, output filename
Returns : true : file was saved ok, false : otherwise
------------------------------------------------------------
'''
def savewer (werresult, outf):
    file = open (outf, "w")
    outputline="WER calculation results\n"
    file.write(outputline)
    for i in range (len(werresult)) :
      wer = werresult[i]
      werfmt='{:>6.4}'.format(wer) + "\n"
      file.write(werfmt)
    file.close()
    return True

def main():
    assert (wercheck())                 # fails when wer function do not perform as expected
    reff, resf, outf, skip = getargs()  # gets command line args
    refs=loadrefres (reff)              # loads reference file
    ress=loadrefres (resf)              # loads results file
    assert (len(refs) == len(ress))     # fails when lines of references != lines of results
    werresult=calcwer(refs, ress, skip) # calculates wer
    assert(savewer(werresult, outf))    # saves wer results to file

if __name__ == "__main__":
    main()
