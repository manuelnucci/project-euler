from collections import defaultdict


def synonym_queries(synonym_words, queries):
    '''
    synonym_words: iterable of pairs of strings representing synonymous words
    queries: iterable of pairs of strings representing queries to be tested for
             synonymous-ness
    '''
    synonyms = defaultdict(set)
    for w1, w2 in synonym_words:
        synonyms[w1].add(w2)

    def synonymous(w1, w2):
        return w1 == w2 or w2 in synonyms.get(w1, ()) or w1 in synonyms.get(w2, ())

    def synonymous_phrase(q1, q2):
        q1, q2 = q1.split(), q2.split()
        return len(q1) == len(q2) and all(synonymous(w1, w2) for w1, w2 in zip(q1, q2))

    return [synonymous_phrase(q1, q2) for q1, q2 in queries]
