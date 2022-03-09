
text = open('document.txt', 'r', encoding='utf-8').read()
words = text.split()
freqs = {}

for word in words:
    word = word.lower()
    word = ''.join(filter(lambda c: c.isalnum(), word))
    freqs[word] = freqs[word] + 1 if word in freqs else 1

freqs = sorted(freqs.items(), key=lambda x: x[1])
freqs.reverse()

for word, count in freqs:
    print(f'{word}: {count}')
