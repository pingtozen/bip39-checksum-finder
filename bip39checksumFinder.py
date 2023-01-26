import mnemonic

# example 11 words seed: abandon ability able about above absent absorb abstract absurd abuse access
# example 23 words seed: abandon ability able about above absent absorb abstract absurd abuse access accident account accuse achieve acid acoustic acquire across act action actor actress

def get_some_checksum_words(seed_words):
    seed = " ".join(seed_words)
    m = mnemonic.Mnemonic("english")
    valid_words = []
    words = m.generate(256).split(" ")
    # print(words)
    for word in words:
        candidate_seed = seed + " " + word
        if m.check(candidate_seed):
            valid_words.append(word)
    return valid_words

def get_checksum_words(seed_words):
    valid_word_length = None
    if len(seed_words) == 11:
        valid_word_length = 128
    elif len(seed_words) == 23:
        valid_word_length = 8
    else:
        print(f"Your seed had {len(seed_words)} words. It can either have 11 or 23 words.")
        return
    valid_words = []
    while len(valid_words) < valid_word_length:
        new_words = get_some_checksum_words(seed_words)
        for word in new_words:
            if not word in valid_words:
                valid_words.append(word)
    return sorted(valid_words)

# Example usage
seed_words = input("Enter your seed (11 or 23 words): ").split(" ")
result = get_checksum_words(seed_words)
if (result):
    print("\nAnd your checksum words are:\n")
    print(" ".join(result) + "\n")
