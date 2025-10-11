text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. " +
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)
words = text.split()

new_text = []
for word in words:
    if word.endswith(',') or word.endswith('.'):
        sign = word[-1]
        word = word[:-1]
        new_text.append(f"{word}ing{sign}")
    else:
        word = word + 'ing'
        new_text.append(word)

print(' '.join(new_text))
