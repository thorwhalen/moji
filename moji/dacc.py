"""Data access"""


import re
from collections import defaultdict
import numpy as np

from moji.util import data_dir
from idiom import WordVec, WordVecSearch

from functools import lru_cache

from idiom import WordVec, WordVecSearch, WordVecStore


@lru_cache(maxsize=1)
def get_word_vec(*args):
    return WordVec(*args)


emo_of_description_file = data_dir / "emoji_joined.tsv"

tokenizer = re.compile("\w+").findall


def mk_words_of_emo():
    words_of_emo = defaultdict(list)
    emo_of_description = dict(
        np.genfromtxt(
            str(emo_of_description_file), delimiter="\t", dtype=str, skip_header=1
        )
    )
    for description, emo in emo_of_description.items():
        words_of_emo[emo].extend(tokenizer(description))

    return words_of_emo
