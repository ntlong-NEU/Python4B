text = "sd sd aa ab aa ac ab"
fre_words = {}

for w in text.split():
    if w in fre_words:
        fre_words[w] += 1
    else:
        fre_words[w] = 1