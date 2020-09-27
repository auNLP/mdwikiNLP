"""
This script contain an example Text class

Each function contains:
An explanation as well as an example
Your job as a studygroup is to make the functions in class 2 and 3.

In class 3 we will then assemble a pipeline using the Text class at the end.


I suggest you start from the top and for each function:
    1) discuss potential solution (e.g. sentence segmentation splitting by ".")
    2) implement the simplest solution first for each function
    3) go back and improve upon the initial function

for class 2 it would be ideal if you have a simple version of the following
functions:
    sentence_segment
    tokenize
    ner_regex

Additional stuff which you might add is:
    A function for dependency parsing using stanza
    alternatives to each of the function (e.g. using tokenization using nltk)
    Add a function for stemming
    Add plotting functionality for word frequencies
    Add plotting functionality for dependency trees
"""
from nlp_functions import lemmatize_stanza as lemma
from tokenizer import *

class Text():
    def __init__(self, txt):
        self.sentences = sentence_segment()


    def tokenize(self, tokenizer="myown"):
        if tokenizer == "myown":
            self.tokens = tokenize(self.sentences)
        if tokenizer == "stanza":
            self.tokens = tokenize_stanza(self.sentences)


    def ner(self, method="regex"):
        if method == "regex":
            res = ner_regex(self.tokens)
        else:
            raise ValueError(f"method {method} is not a valid method")
        return res

    # add methods to do pos-tagging, lemmatization
    # n-grams and token frequencies

    def get_df(self):
        """
        returns a dataframe containing the columns:
        sentence number, token, lemma, pos-tag
        andd optionally named-entities
        """
        pass

    # add methods to extract tokens, sentences
    # ner, pos-tags etc.

Text("this is my text")
Text.tokenize()
Text.n_grams(n=2)
Text.ner(method="regex")













