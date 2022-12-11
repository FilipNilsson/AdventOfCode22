import operator

with open('input.txt', 'r') as infile:
    data = infile.read().splitlines()

class Monkey:
    items = None
    operation = None
    operation = None
    test = None
    true = None
    false = None
    inspects = 0

operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
monkeys = []

for line in data:
    line = line.lstrip()
    if line.startswith('Monkey '):
        monkeys.append(Monkey())
        idx = len(monkeys) - 1
    elif line.startswith('Starting items:'):
        monkeys[-1].items = [int(x.rstrip(',')) for x in line.split(':')[1].split()]
    elif line.startswith('Operation:'):
        monkeys[-1].operation = operations[line.split()[-2]]
        monkeys[-1].value = int(line.split()[-1]) if line.split()[-1] != 'old' else None
    elif line.startswith('Test:'):
        monkeys[-1].test = int(line.split()[-1])
    elif line.startswith('If true:'):
        monkeys[-1].true = int(line.split()[-1])
    elif line.startswith('If false:'):
        monkeys[-1].false = int(line.split()[-1])

lcm = 1
for monkey in monkeys:
    lcm = lcm*monkey.test

for round in range(10000):
    for idx, monkey in enumerate(monkeys):
        for old in monkey.items.copy():
            monkey.inspects += 1
            value = monkey.value or old
            old = monkey.operation(old % lcm, value)
            if old % monkey.test == 0:
                monkeys[monkey.true].items.append(old)
                monkey.items.pop(0)
            else:
                monkeys[monkey.false].items.append(old)
                monkey.items.pop(0)

for idx, monkey in enumerate(monkeys):
    print(f'Monkey {idx} inspected {monkey.inspects} items.')
inspects = [x.inspects for x in monkeys]
inspects.sort()
print(inspects[-2:])
print(inspects[-2] * inspects[-1])
