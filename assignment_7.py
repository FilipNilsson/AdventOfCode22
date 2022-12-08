with open('input.txt', 'r') as infile:
    data = infile.read().splitlines()

class Directory:
    def __init__(self, parent):
        self.parent = parent
        self.children = {}
        self.size = 0

options = []
def walk_dir(dir, limit):
    if dir.size < limit:
        return
    options.append(dir.size)
    for child in dir.children.values():
        walk_dir(child, limit)

file_system = {'/': Directory(None)}
current_node = file_system['/']

assignment = 2
if assignment == 1:
    sum = 0

    for line in data[1:]:
        if line[0].isdigit():  # File
            size = int(line.split()[0])
            current_node.size += size
            parent = current_node.parent
            while parent:
                parent.size += size
                parent = parent.parent
        elif line[0].isalpha():  # Dir
            current_node.children[line.split()[1]] = Directory(current_node)
        elif line.startswith('$ cd ..'):
            if current_node.size <= 100000:
                sum += current_node.size
            current_node = current_node.parent
        elif line.startswith('$ cd '):
            current_node = current_node.children[line.split()[2]]

    print(sum)
else:
    for line in data[1:]:
        if line[0].isdigit():  # File
            size = int(line.split()[0])
            current_node.size += size
            parent = current_node.parent
            while parent:
                parent.size += size
                parent = parent.parent
        elif line[0].isalpha():  # Dir
            current_node.children[line.split()[1]] = Directory(current_node)
        elif line.startswith('$ cd ..'):
            current_node = current_node.parent
        elif line.startswith('$ cd '):
            current_node = current_node.children[line.split()[2]]

    empty_space = 70000000 - file_system['/'].size
    needed_space = 30000000 - empty_space
    walk_dir(file_system['/'], needed_space)
    print(min(options))