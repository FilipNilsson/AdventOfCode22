with open('input.txt', 'r') as infile:
    data = infile.read().splitlines()

assignment = 2
if assignment == 1:
    head_curr = tail_curr = [0, 0]
    positions = [tail_curr.copy()]
    for line in data:
        steps = int(line.split()[1])
        if line[0] == 'L':
            head_curr = (head_curr[0] - steps, head_curr[1])
        elif line[0] == 'R':
            head_curr = (head_curr[0] + steps, head_curr[1])
        elif line[0] == 'U':
            head_curr = (head_curr[0], head_curr[1] - steps)
        elif line[0] == 'D':
            head_curr = (head_curr[0], head_curr[1] + steps)

        for _ in range(steps):
            if head_curr[0] - tail_curr[0] > 1:
                tail_curr[0] += 1
                tail_curr[1] = head_curr[1]
                if tail_curr not in positions:
                    positions.append(tail_curr.copy())
            elif head_curr[0] - tail_curr[0] < -1:
                tail_curr[0] -= 1
                tail_curr[1] = head_curr[1]
                if tail_curr not in positions:
                    positions.append(tail_curr.copy())
            elif head_curr[1] - tail_curr[1] > 1:
                tail_curr[1] += 1
                tail_curr[0] = head_curr[0]
                if tail_curr not in positions:
                    positions.append(tail_curr.copy())
            elif head_curr[1] - tail_curr[1] < -1:
                tail_curr[1] -= 1
                tail_curr[0] = head_curr[0]
                if tail_curr not in positions:
                    positions.append(tail_curr.copy())
    print(len(positions))
else:
    nbr_knots = 10
    knots = []
    for _ in range(nbr_knots):
        knots.append(0j)
    positions = {0j}
    for line in data:
        steps = int(line.split()[1])
        for _ in range(steps):
            for idx, knot in enumerate(knots):
                if idx == 0:
                    if line[0] == 'L':
                        knots[0] += -1
                    elif line[0] == 'R':
                        knots[0] += 1
                    elif line[0] == 'U':
                        knots[0] += -1j
                    elif line[0] == 'D':
                        knots[0] += 1j
                else:
                    if abs(knots[idx-1] - knot) >= 2:
                        change = (knots[idx-1] - knot) / abs(knots[idx-1] - knot)
                        knots[idx] += complex((change.real>0) - (change.real<0), (change.imag>0) - (change.imag<0))
                    if idx == nbr_knots - 1:
                        positions.add(knots[idx])
    print(len(positions))