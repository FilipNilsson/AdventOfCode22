with open('input.txt', 'r') as infile:
    data = infile.readlines()

assignment = 2
if assignment == 1:
    sum = 0
    for line in data:
        line = line.rstrip()
        comp_a = line[len(line)//2:]
        comp_b = line[:len(line)//2]
        for letter in comp_a:
            if letter in comp_b:
                if letter.islower():
                    sum += ord(letter) - 96
                else:
                    sum += ord(letter) - 38
                break
    print(sum)

if assignment == 2:
    sum = 0
    for line_nbr in range(0, len(data), 3):
        elf_1 = data[line_nbr].rstrip()
        elf_2 = data[line_nbr+1].rstrip()
        elf_3 = data[line_nbr+2].rstrip()
        for letter in elf_1:
            if letter in elf_2 and letter in elf_3:
                if letter.islower():
                    sum += ord(letter) - 96
                else:
                    sum += ord(letter) - 38
                break
    print(sum)