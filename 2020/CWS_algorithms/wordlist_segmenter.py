def wordlist_segmenter(sentence, vocab):
    candidates = list()
    rest = sentence
    for word in vocab:
        length = len(word)
        result = rest.find(word)
        if result != -1:
            cut = result+length
            rest = rest[cut:]
            candidates.append(word)
        else:
            pass
    return '_'.join(candidates)
