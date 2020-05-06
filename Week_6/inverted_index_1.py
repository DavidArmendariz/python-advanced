#!/usr/bin/env python
# coding: utf-8

# In[63]:


import pickle
class InvertedIndex:
    def __init__(self, word_to_docs_mapping):
        self.word_to_docs_mapping = word_to_docs_mapping

    def query(self, words):
        common_articles = set()
        for articles in self.word_to_docs_mapping.values():
            common_articles |= articles
        for word in words:
            common_articles &= self.word_to_docs_mapping[word]
        return common_articles
    def dump(self, filepath):
        with open(filepath, "wb") as file:
            pickle.dump(self, file)
    @classmethod
    def load(cls, filepath):
        with open(filepath, 'rb') as file:
            inverted_index_object = pickle.load(file)
        return inverted_index_object


# In[64]:


def load_document(filepath):
    articles = dict()
    with open(filepath, encoding="utf8") as file:
        lines = file.readlines()
    data = map(lambda line: line.split("\t", maxsplit=1), lines)
    for x in data:
        articles[int(x[0])] = x[1].strip()
    return articles


# In[65]:


def build_inverted_index(articles):
    words = set()
    inverted_index = dict()
    for index, text in articles.items():
        for word in text.split():
            inverted_index[word] = inverted_index.setdefault(word, set()) | {index}
    return InvertedIndex(inverted_index)

