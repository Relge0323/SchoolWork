from textblob import TextBlob

def get_words(fileName):
    myBlob = TextBlob
    paragCounter = 0
    words = []
    with open(fileName, encoding='utf8', newline='\r\n') as speech:
        line = speech.readline()
        while line:
            if line != '\r\n':
                paragCounter += 1
                myBlob = TextBlob(line)
                words += myBlob.words
                # need to download the following to make the above work
                # python -m textblob.download_corpora
                # print(f'{paragCounter} {line}')
            line = speech.readline()

    speech.close()
    return words

def clean_list(lst):
    """ Go through the list and remove words we don't need. """
    newLst = []
    for word in lst:
        if word.lower() not in stopWords:
            newLst.append(word)
    return newLst

def count_words(lst):    
    """ Create a dictionary of unique words and their 
        corresponding count. """
    wordCount = {}
    for word in lst:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    return wordCount

def get_frequency(lst):
    return lst[1]


# --- ----------------------------------------------
# List of words to NOT include in the word cloud   
# --------------------------------------------------
stopWords = ["a", "about", "above", "across", "after", "afterwards", "again", "against", 
            "ago", "all", "almost", "alone", "along", "already", "also", "although", 
            "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", 
            "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", 
            "are", "around", "as", "at", "back", "be", "became", "because", "become", 
            "becomes", "becoming", "been", "before", "beforehand", "behind", "being", 
            "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom", 
            "but", "by", "call", "came", "can", "cannot", "cant", "case","cases","cause", 
            "co", "computer", "con", "could", "couldnt", "cry", "de", "describe", "detail", 
            "do", "does", "doing", "done", "down", "due", "during", "each", "eg", "eight", 
            "either", "eleven", "else", "elsewhere", "empty", "enough", "etc", "even", 
            "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fie",
            "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", 
            "formerly", "forty", "found", "four", "from", "front", "full", "further", 
            "get", "give", "go", "had", "has", "hasnt", "have", "he", "held", "having", 
            "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", 
            "herself", "him", "himself", "his", "how", "however", "hundred", "i", "ie", 
            "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", 
            "keep", "know", "knows", "knew", "last", "latter", "latterly", "least", "less", 
            "let", "ltd", "made", "make","many", "may", "me", "meanwhile", "might", "mill", 
            "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", 
            "myself", "name", "namely", "neither", "never", "nevertheless", "next", 
            "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", 
            "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", 
            "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", 
            "own", "part", "per", "perhaps", "plainly", "please", "precisely", "put", 
            "rather", "re", "same", "said", "say", "says", "see", "seem", "seemed", 
            "seeming", "seems", "serious", "several", "shall", "she", "should", "show", 
            "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", 
            "something", "sometime", "sometimes", "somewhere", "st", "sts", "still", "such", 
            "system", "take", "ten", "th", "ths", "thx", "than", "that", "the", "their", 
            "them", "themselves", "then", "thence", "there", "thereafter", "thereby", 
            "therefore", "therein", "thereupon", "these", "they", "thick", "thin", 
            "third", "this", "those", "though", "three", "through", "throughout", 
            "thru", "thus", "to", "together", "too", "top", "toward", "towards", 
            "twelve", "twenty", "two", "un", "unless", "under", "until", "up", 
            "upon", "us", "very", "via", "was", "we", "well", "were", "weve", "what", 
            "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", 
            "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", 
            "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", 
            "with", "within", "without", "would", "year", "years", "yet", "you", 
            "your", "yours", "yourself", "yourselves"]


# JavaScript example found in: C:\Users\spreston\OneDrive - prcc.edu\Documents\JavaScript\Chapter07\chapter