"""Data access"""

import re
from collections import defaultdict
from functools import lru_cache

import numpy as np

from idiom import WordVec, WordVecSearch, WordVecStore

from moji.util import data_dir


@lru_cache(maxsize=1)
def get_word_vec(*args):
    return WordVec(*args)


emo_of_description_file = data_dir / 'emoji_joined.tsv'

tokenizer = re.compile(r'\w+').findall


def mk_emo_of_description():
    return dict(
        np.genfromtxt(
            str(emo_of_description_file), delimiter='\t', dtype=str, skip_header=1
        )
    )


def mk_words_of_emo():
    words_of_emo = defaultdict(list)
    emo_of_description = mk_emo_of_description()
    for description, emo in emo_of_description.items():
        words_of_emo[emo].extend(tokenizer(description))

    return words_of_emo


def mk_terms_of_emo():
    terms_of_emo = defaultdict(list)
    emo_of_description = mk_emo_of_description()
    for description, emo in emo_of_description.items():
        terms_of_emo[emo].append(tokenizer(description))


# emo_vec_search = WordVecSearch(word_vec=WordVec(vec_of_emo)).fit()
