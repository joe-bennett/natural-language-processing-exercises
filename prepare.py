import pandas as pd
import numpy as np
import unicodedata
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


def basic_clean(string_of_words):
    string_of_words=string_of_words.lower()
    string_of_words = unicodedata.normalize('NFKD',string_of_words)\
        .encode('ascii', 'ignore')\
            .decode('utf-8')
    string_of_words=re.sub(r'[^a-z0-9\'\s]','',string_of_words)
    return string_of_words            

def tokenize(any_string):
    tokenize=nltk.tokenize.ToktokTokenizer()
    any_string = tokenize.tokenize(any_string, return_str=True)
    return any_string

def stem(any_string):
    ps= nltk.porter.PorterStemmer()
    stems= [ps.stem(word) for word in any_string.split()]
    string_stemmed= ' '.join(stems)
    return string_stemmed

def lemmatize(any_string):
    lemmas = [wnl.lemmatize(word) for word in any_string.split()]   
    any_string_lemmatized= ' '.join(lemmas)
    return any_string_lemmatized

def remove_stopwords(any_string,extra_words='',exclude_words=''):
    stopwords_ls= stopwords.words('english')
    if exclude_words != '':
        stopwords_ls.remove(exclude_words)
    if extra_words!='':
        stopwords_ls.append(extra_words)
    words=any_string.split()
    filtered_words=[word for word in words if word not in stopwords_ls]
    print(f'Removed {(len(words)-len(filtered_words))} words from string')
    string_no_stop_words= ' '.join(filtered_words)
    return string_no_stop_words