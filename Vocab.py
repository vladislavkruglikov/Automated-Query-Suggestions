from collections import Counter, defaultdict

from abc import abstractmethod


class Vocab:
    def __init__(self, path: str, n_samples: int, vocab_size: int):
        file = open(path, 'r')

        self.corpus = [line.strip() for line in file][:n_samples]
        self.corpus = [self.preprocess(text) for text in self.corpus]
        self.tokens = sum([text.split() for text in self.corpus], [])
        self.vocab = Counter(self.tokens)
        self.vocab = defaultdict(int, Counter(self.tokens).most_common(vocab_size))

        self.size = sum(self.vocab.values())

    @abstractmethod
    def preprocess(self, text: str):
        text = text.lower()
        # Remove prepositions and unions since they boost
        # text probability
        # text = ' '.join([token for token in text.split() if len(token) >= 2])
        return text

    def probability(self, word: str):
        return self.vocab[word] / self.size
