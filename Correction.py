from Vocab import Vocab
from typing import *


class Correction:
    def __init__(self, vocab: Vocab, max_steps=1):
        self.max_steps = max_steps
        self.vocab = vocab

    def correction(self, word: str):
        return max(self.candidates(word), key=self.P)

    def candidates(self, word: str):
        return self.known([word]) or self.known(self.edits(word)) or [word]

    def known(self, words: List[str]):
        return set(w for w in words if w in self.vocab.vocab)

    def edits(self, word: str):
        letters    = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def get_edits(self, word: str, n=0):
        if n == self.max_steps:
            return [word]

        variants = [self.get_edits(e1, n + 1) for e1 in self.candidates(word)]
        return sorted(sum(variants, []), key=self.vocab.probability, reverse=True)
