with open('input.txt', 'r') as infile:
    data = infile.read().splitlines()

assignment = 2

stacks = {}
idx_to_stack = {}
done = False
for line in data:
    if line[1] == '1':
        for idx, letter in enumerate(line):
            if letter.isdigit():
                idx_to_stack[idx] = letter
                stacks[letter] = []
        break

for start_line, line in enumerate(data):
    if line[1] == '1':
        break
    for idx, letter in enumerate(line):
        if letter.isalpha():
            stacks[idx_to_stack[idx]].insert(0, letter)

for line in data[start_line+2:]:
    _, amount, _, from_, _, to = line.split()
    if assignment == 1:
        stacks[to] += stacks[from_][-int(amount):][::-1]
    else:
        stacks[to] += stacks[from_][-int(amount):]
    stacks[from_] = stacks[from_][:-int(amount)]

answer = ''
for stack in stacks.values():
    answer += stack[-1]
print(answer)