with open('input.txt', 'r') as infile:
    data = infile.read().splitlines()


x = [1]
cycle = 0
pixel = ''
for line in data:
    if line == 'noop':
        pixel += '.' if abs(x[-1] - cycle%40) >= 2 else '#'
        x.append(x[-1])
        cycle += 1
    else:
        change = int(line.split()[1])
        pixel += '.' if abs(x[-1] - cycle%40) >= 2 else '#'
        x.append(x[-1])
        cycle += 1
        pixel += '.' if abs(x[-1] - cycle%40) >= 2 else '#'
        x.append(x[-1] + change)
        cycle += 1

sum = 0
for idx in [20, 60, 100, 140, 180, 220]:
    sum += idx * x[idx - 1]
print(sum)

print(pixel[:40])
print(pixel[40:80])
print(pixel[80:120])
print(pixel[120:160])
print(pixel[160:200])
print(pixel[200:240])