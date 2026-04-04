


def ion2e(word):
    if word.endswith("ion"):
        return word[:-3] + "e"
    else:
        return word


print(ion2e("congratulation"))