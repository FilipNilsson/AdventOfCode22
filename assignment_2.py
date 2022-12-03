with open('input.txt', 'r') as infile:
    data = infile.readlines()

assignment = 2

if assignment == 1:
    my_shapes = {'X': 1, 'Y': 2, 'Z': 3}
    elf_shapes = {'A': 1, 'B': 2, 'C': 3}
    score = 0
    for line in data:
        score += my_shapes[line[2]]
        if my_shapes[line[2]] - elf_shapes[line[0]] == 0:
            score += 3  # Draw
        elif my_shapes[line[2]] - elf_shapes[line[0]] in (-2, 1):
            score += 6  # Win
    print(score)

elif assignment == 2:
    shapes = ['A', 'B', 'C']
    shape_scores = {'A': 1, 'B': 2, 'C': 3}
    score = 0
    for line in data:
        if line[2] == 'Y':
            score += shape_scores[line[0]] + 3  # Draw
        elif line[2] == 'X':
            my_shape = shapes[(shapes.index(line[0]) - 1)%3]
            score += shape_scores[my_shape]  # Loss
        elif line[2] == 'Z':
            my_shape = shapes[(shapes.index(line[0]) + 1)%3]
            score += shape_scores[my_shape] + 6  # Win
    print(score)