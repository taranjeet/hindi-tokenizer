import unittest

from hinditokenizer import *

from . import data


class TestHindiTokenizer(unittest.TestCase):

    def test_tokenize_sent(self):
        sentences = tokenize_sent(data.TOKENIZE['SENTENCES']['SENT1']['INPUT'])
        self.assertEqual(len(sentences), len(data.TOKENIZE['SENTENCES']['SENT1']['OUTPUT']))
        for i in range(len(sentences)):
            self.assertEqual(sentences[i].encode('utf8'), data.TOKENIZE['SENTENCES']['SENT1']['OUTPUT'][i])

    def test_tokenize_only(self):
        tokens = tokenize(data.TOKENIZE['TOKENS']['SENT1']['INPUT'])
        self.assertEqual(len(tokens), len(data.TOKENIZE['TOKENS']['SENT1']['OUTPUT']))
        for i in range(len(tokens)):
            self.assertEqual(tokens[i].encode('utf8'), data.TOKENIZE['TOKENS']['SENT1']['OUTPUT'][i])

    def test_remove_hyphenated_tokens(self):
        tokens = tokenize(data.TOKENIZE['TOKENS']['SENT2']['INPUT'])
        filtered_tokens = remove_hyphenated_tokens(tokens)
        self.assertEqual(len(filtered_tokens), len(data.TOKENIZE['TOKENS']['SENT2']['OUTPUT']))
        for i in range(len(filtered_tokens)):
            self.assertEqual(filtered_tokens[i].encode('utf8'), data.TOKENIZE['TOKENS']['SENT2']['OUTPUT'][i])

    def test_stem(self):
        for key, value in data.TOKENIZE['STEM'].items():
            stem_word = stem(value['INPUT'])
            self.assertEqual(stem_word.encode('utf8'), value['OUTPUT'])

    def test_stopwords(self):
        stopwords = stopwords_list()
        self.assertIn(data.TOKENIZE['STOPWORDS']['WORD1'], stopwords)



if __name__ == '__main__':
    unittest.main()
