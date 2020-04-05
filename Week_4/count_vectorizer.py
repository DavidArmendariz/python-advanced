#!/usr/bin/env python
# coding: utf-8

# In[7]:


class CountVectorizer:
    def __init__(self, ngram_size):
        self.ngram_size = ngram_size
        self.vocabulary = dict()
        self.unique_tokens = set()
        self.corpus_tokens = []
    
    def fit(self, corpus):
        self.vocabulary.clear()
        self.unique_tokens.clear()
        for word in corpus:
            i = 0
            while (i+self.ngram_size) <= len(word):
                token = word[i:(i+self.ngram_size)]
                self.unique_tokens.add(token)
                i += 1
        self.vocabulary = {token: index for index, token in enumerate(sorted(list(self.unique_tokens)))}
    
    def transform(self, corpus):
        self.corpus_tokens.clear()
        for word in corpus:
            i = 0
            tokens_per_word = []
            while (i+self.ngram_size) <= len(word):
                token = word[i:(i+self.ngram_size)]
                tokens_per_word.append(token)
                i += 1
            self.corpus_tokens.append(tokens_per_word)
        tokens = list(self.vocabulary.keys())
        transformed_corpus = []
        for index, token_list in enumerate(self.corpus_tokens):
            tokens_per_word = []
            for token in tokens:
                tokens_per_word.append(token_list.count(token))
            transformed_corpus.append(tokens_per_word)
        return transformed_corpus
                  
    def fit_transform(self, corpus):
        self.fit(corpus)
        return self.transform(corpus)

