Tokenizer for Hindi

This package tends to implement a Tokenizer and a stemmer for Hindi language.

To import the package,
```python
from HindiTokenizer import Tokenizer
```

This package implements various funcions, which are listed as below:

* [read_from_file](www.dummy.com)
* [generate_sentences]()
* [tokenize]()
* [generate_freq_dict]()
* [generate_stem_words]()
* [generate_stem_dict]()
* [remove_stopwords]()
* [clean_text]()
* [print_sentences]()
* [print_tokens]()
* [print_freq_dict]()
* [len_text]()
* [sentence_count]()
* [tokens_count]()
* [concordance]()

The Tokenizer can be created in two ways
```python
t=Tokenizer("यह वाक्य हिन्दी में है।")
```
Or
```python
t=Tokenizer()
t.read_from_file('filename_here')
```

A brief description about all the functions

<a name="readfromfile">**read_from_file**</a>

This function takes the name of the file which is present in the current directory and reads it.

```python
t.read_from_file('hindi_file.txt')
```


