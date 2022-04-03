from collections import Counter, defaultdict
from Vocab import Vocab
from typing import *


class BeamSearch:
    def __init__(self, vocab: Vocab, max_depth, top_k):
        self.max_depth = max_depth
        texts = vocab.corpus
        self.top_k = top_k
        self.vocab = vocab

        self.statistics = defaultdict(list)
        for text in texts:
            words = text.split()
            for i in range(len(words) - 1):
                self.statistics[words[i]].append(words[i + 1])

        for word in self.statistics:
            self.statistics[word] = Counter(self.statistics[word]).most_common(3)
            self.statistics[word] = [word for (word, occur) in self.statistics[word]]

    def search(self, queries, n=0):
        if n == self.max_depth:
            return []

        next_tokens = []
        for query in queries:
            last_token = query[-1]
            for next_word in self.statistics[last_token]:
                next_tokens.append(query + [next_word])

        return sorted(queries + self.search(next_tokens, n + 1), key=self.score, reverse=True)[:self.top_k]

    def score(self, query):
        if ' '.join(query) in self.vocab.corpus:
            return 1
        return sum(self.vocab.probability(word) for word in query) / len(query) * len(query[-1])
