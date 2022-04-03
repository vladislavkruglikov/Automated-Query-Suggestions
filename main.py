from BeamSearch import BeamSearch
from Correction import Correction
from Vocab import Vocab

vocab = Vocab('dataset.txt', n_samples=10000, vocab_size=50000)
correction = Correction(max_steps=2, vocab=vocab)
beam_search = BeamSearch(max_depth=4, top_k=5, vocab=vocab)

query = input()
query_preprocessed = vocab.preprocess(query)

query_corrected = correction.get_edits(query_preprocessed)[0]

print(f'Поиск: {query}')

if query_preprocessed != query_corrected:
    print(f'Возможно вы имелли ввиду: {query_corrected} \n')

results = beam_search.search([[query_corrected]])

results = [' '.join(result) for result in results]

print(f'Результаты:')

for result in results:
    print(result)
