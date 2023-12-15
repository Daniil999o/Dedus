# -*- coding: utf-8 -*-

import re
import os
import shutil
from collections import Counter


def show_all(words):
    return '\n'.join(words)


def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def get_words_from_lines(path):
    return read(path).split('\n')


def remove_rare_words(words):
    counter = Counter(words)
    return list(filter(lambda x: counter[x] > 1, words))


def filter_text(text):
    text = re.sub(r'[a-zA-Z\s]+', ' ', text.lower())
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = ''.join([x for x in text if x not in '0123456789'])

    return remove_prepositions(remove_rare_words(text.split(' ')))


def save(string, path):
    if os.path.isfile(path):
        os.remove(path)

    with open(f'filtered/{path}', 'w', encoding='utf-8') as f:
        f.write(string)


def remove_prepositions(words):
    return list(filter(lambda x: len(x) > 3, words))


def remove_duplicates(words):
    result = []
    for x in words:
        if x not in result:
            result.append(x)

    return result


def get_roots(words):
    words = remove_duplicates(words)

    result = []
    checked_words = []

    for x in words:
        root_words = []

        for i in range(3, 5):
            pattern = x[0:i]

            if pattern:
                for word in words:
                    if word not in checked_words and re.search(pattern, word):
                        checked_words.append(word)
                        root_words.append(word)

        root = min(root_words, key=len) if len(root_words) > 0 else None
        if root:
            result.append(min(root_words, key=len))

    return result
