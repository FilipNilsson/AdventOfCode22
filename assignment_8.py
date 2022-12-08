with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()
    data = []
    for line in lines:
        data.append([int(x) for x in line])

row_length = len(data[0])
column_length = len(data)

assignment=2

if assignment == 1:
    visibility = []

    for idx, row in enumerate(data):
        row = [int(x) for x in row]
        visibility.append([0] * row_length)
        for col_idx, column in enumerate(row):
            if col_idx in (0, row_length-1) or idx in (0, column_length-1):
                visibility[idx][col_idx] = 1
            elif max(data[idx][:col_idx]) < column:
                visibility[idx][col_idx] = 1
            elif max(data[idx][col_idx+1:]) < column:
                visibility[idx][col_idx] = 1

    for column in range(column_length):
        for row in range(row_length):
            if visibility[row][column] == 1:
                continue
            for x in range(row):
                if data[x][column] >= data[row][column]:
                    break
            else:
                visibility[row][column] = 1

    for column in range(column_length-1, 0, -1):
        for row in range(row_length-1, 0, -1):
            if visibility[row][column] == 1:
                continue
            for x in range(row+1, row_length):
                if data[x][column] >= data[row][column]:
                    break
            else:
                visibility[row][column] = 1

    visible_trees = 0
    for row in visibility:
        visible_trees += row.count(1)
    print(visible_trees)

else:
    row_length = len(data[0])
    column_length = len(data)
    scores = []

    for row in range(row_length):
        scores.append([])
        for column in range(column_length):
            if row in (0, row_length-1) or column in (0, column_length-1):
                scores[row].append(0)
                continue
            height = data[row][column]
            scores[row].append(1)
            # Left
            score = 1
            col_idx = column - 1
            while col_idx > 0 and height > data[row][col_idx]:
                score += 1
                col_idx -= 1
            scores[row][column] *= score
            # Right
            score = 1
            col_idx = column + 1
            while col_idx < column_length-1 and height > data[row][col_idx]:
                score += 1
                col_idx += 1
            scores[row][column] *= score
            # Up
            score = 1
            row_idx = row - 1
            while row_idx > 0 and height > data[row_idx][column]:
                score += 1
                row_idx -= 1
            scores[row][column] *= score
            # Down
            score = 1
            row_idx = row + 1
            while row_idx < row_length-1 and height > data[row_idx][column]:
                score += 1
                row_idx += 1
            scores[row][column] *= score

    maximum = 0
    for row in scores:
        maximum = max(maximum, max(row))
    print(maximum)