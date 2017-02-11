# -*- coding: utf-8 -*-

from .data import STOPWORDS, SUFFIXES


def tokenize_sent(text):
    '''This generates a list for sentences.'''
    sentences = text.decode('utf8').split(u'।')
    return [sentence.strip() for sentence in sentences if sentence]


def tokenize(text):
    '''This generates a list for tokens.'''
    sentences = tokenize_sent(text)
    return [token for sentence in tokenize_sent(text)
            for token in sentence.split(' ')]


def remove_hyphenated_tokens(tokens):
    '''Handles the case of words separated over hyphen'''
    for token in tokens:
        if '-' in token:
            pair = token.split('-')
            idx = tokens.index(token)
            tokens.remove(token)
            tokens.insert(idx, pair[0])
            tokens.insert(idx+1, pair[1])
    return tokens


def stem(word):
    '''
        Performs stemming for a given Hindi word

        Implementation is taken from http://research.variancia.com/hindi_stemmer/

        Credits :
        Lightweight Hindi stemmer
        Copyright © 2010 Luís Gomes <luismsgomes@gmail.com>.

        Implementation of algorithm described in

            A Lightweight Stemmer for Hindi
            Ananthakrishnan Ramanathan and Durgesh D Rao
            http://computing.open.ac.uk/Sites/EACLSouthAsia/Papers/p6-Ramanathan.pdf

            @conference{ramanathan2003lightweight,
              title={{A lightweight stemmer for Hindi}},
              author={Ramanathan, A. and Rao, D.},
              booktitle={Workshop on Computational Linguistics for South-Asian Languages, EACL},
              year={2003}
            }

        Ported from HindiStemmer.java, part of of Lucene.
    '''
    word = word.decode('utf8')
    for L in 5, 4, 3, 2, 1:
        if len(word) > L + 1:
            for suf in SUFFIXES[L]:
                if word.endswith(suf):
                    return word[:-L]
    return word


def stopwords_list():
    '''Returns list of stopwords in Hindi'''
    return STOPWORDS

