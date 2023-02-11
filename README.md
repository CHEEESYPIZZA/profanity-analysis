# profanity-analysis
The above code is a Python program that performs profanity analysis on a file containing Twitter tweets. The program analyzes the degree of profanity in each sentence in the file by checking for the presence of racial slurs. The program uses the Natural Language Toolkit (nltk) library to perform tokenization, breaking down the sentences into individual words or tokens, before checking for the presence of the slurs.

The main function analyze_file takes as input the name of the file and a list of slurs, and returns a list of tuples, each containing a sentence and its degree of profanity. The degree of profanity is calculated as the length of the first matched slur in the sentence. If no slurs are found in the sentence, the degree is 0.

The program uses the re library to split the sentences, and the nltk.download function to download the necessary data and resources for tokenization. The profanity_degree function is called for each sentence in the file, and the results are stored in the results list. Finally, the program prints out the sentences and their degree of profanity.


Assumptions:
The file tweets.txt contains one tweet per line.
The racial slurs are provided as a list of strings, and each slur is a separate word.
The degree of profanity is defined as the length of the matched racial slur.
