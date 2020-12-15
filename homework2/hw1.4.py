line = input('Enter words using space').split()
for ind, word in enumerate(line):
    if len(word) > 10:
        print(f'{ind}. {word[:10]}')
    else:
        print(f'{ind}. {word}')
