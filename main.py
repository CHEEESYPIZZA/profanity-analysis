import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

def profanity_degree(sentence, slurs):
    # tokenize the sentence
    tokens = word_tokenize(sentence)

    # check each token for the presence of the slurs
    for token in tokens:
        if token in slurs:
            return len(token)

    return 0

def analyze_file(filename, slurs):
    # open the file and read the sentences
    with open(filename, "r") as file:
        sentences = file.readlines()

    # compute the degree of profanity for each sentence
    results = [profanity_degree(sentence, slurs) for sentence in sentences]

    # return the results as a list of tuples (sentence, degree)
    return list(zip(sentences, results))

# example usage
slurs = ["racism", "bigotry", "discrimination"]
filename = "tweets.txt"
result = analyze_file(filename, slurs)

# print the result
for sentence, degree in result:
    print(f"Sentence: {sentence}")
    print(f"Degree of profanity: {degree}")
