# Fetches a webpage
# Returns the content of the css elements 'dl' and the xpath '//img@/alt
# Return codes:
# 1 -> success; -1 -> requested elements not found; -2 -> error with the browser

def fetch (bruh, url) :
    try:
        bruh.visit (url)
        transcript = bruh.find_by_css ('dl').value
        alt = bruh.find_by_xpath ('//img/@alt').value # This fails wwih 'pahantomjs'
        return 1, transcript, alt
    except:
        # why am I writing pseudocode
        if (transcript is None or alt is None):
            return -1, None, None
        # what could go wrong
        else:
            return -2, None, None

# Returns the arguments in reversed order
def switchValues (a, b):
    return b, a

# Returns the two first elements of the list, sorted
# Return codes:
# 1 -> success; -1 -> Insufficient arguments; -2 Invalid arguments
def getArgs (args):
    if (len(args) == 1):
        try:
            first = abs ( int (args[0]))
            last = first
        except:
            return -2, None, None
    elif (len(args) >= 2):
        try:
            first = abs (int (args[0]))
            last = abs (int (args[1]))
        except:
            return -2, None, None
    else:
        return -1, None, None

    if (first > last):
        first, last = switchValues(first, last)

    return 1, first, last