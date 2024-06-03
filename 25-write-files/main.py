with open(r'25-write-files\text.txt', 'r+') as file:
    for line in file:
        print(line)

    file.write('\nHola, Vicsito\n')
    file.write('Como estas?\n')
    file.write('Te quiero mucho\n')
