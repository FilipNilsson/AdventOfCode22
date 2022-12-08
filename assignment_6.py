with open('input.txt', 'r') as infile:
    data = infile.read().rstrip()

distinct_letters = 14  # 4 for assignment 1, 14 for assignment 2

sequence = [*data[:distinct_letters]]# * distinct_letters
for idx, letter in enumerate(data[distinct_letters:], distinct_letters):
    sequence[idx%distinct_letters] = letter
    if len(set(sequence)) == distinct_letters:
        print(idx + 1)
        break