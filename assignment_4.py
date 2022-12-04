with open('input.txt', 'r') as infile:
    data = infile.read().splitlines()

assignment = 2
if assignment == 1:
    counter = 0
    for pair in data:
        elf_1, elf_2 = pair.split(',')
        elf_1_min, elf_1_max = [int(x) for x in elf_1.split('-')]
        elf_2_min, elf_2_max = [int(x) for x in elf_2.split('-')]
        if (elf_1_min - elf_2_min) * (elf_1_max - elf_2_max) <= 0:
            counter += 1
    print(counter)

else:
    counter = 0
    for pair in data:
        elf_1, elf_2 = pair.split(',')
        elf_1_min, elf_1_max = [int(x) for x in elf_1.split('-')]
        elf_2_min, elf_2_max = [int(x) for x in elf_2.split('-')]
        elf_1_diff = elf_1_max - elf_1_min
        elf_2_diff = elf_2_max - elf_2_min
        if max(elf_1_max, elf_2_max) - min(elf_1_min, elf_2_min) <= elf_1_diff + elf_2_diff:
            counter += 1
    print(counter)