with open('input.txt', 'r') as infile:
    data = infile.readlines()

totals = []
current = 0
for line in data:
    line = line.rstrip()
    if not line:
        totals.append(current)
        current = 0
    else:
        current += int(line)
totals.sort()
print(sum(totals[-3:]))  # Change to 1 for part 1.