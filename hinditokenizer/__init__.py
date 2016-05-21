# -*- coding: utf-8 -*-

class Tokenizer():
    '''
        This class implements the tokenization for Hindi
    '''


    def __init__(self, text=None):

        if text:
            text = text.decode('utf-8')

        self.text = text
        self.sentences = []
        self.tokens = []

    def generate_sentences(self):
        '''
            This generates an array of sentences.
            Sentences in Hindi are split at Purn-Viram(u`|`)
        '''
        self.sentences = self.text.split(u'|')

    def generate_tokens(self):
        '''
            This generates a list for tokens.
            It also generates sentences if they are not generated
        '''

        if not self.sentences:
            self.generate_sentences()

        sentences = self.sentences
        tokens = []

        for each_sentence in sentences:
            words_list = each.split(' ')
            tokens += words_list

        self.tokens = tokens

