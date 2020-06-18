fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    right_stripped = line.rstrip()
    splitted = right_stripped.split()
    for i in range(len(splitted)):
        if not splitted[i] in lst:
            lst.append(splitted[i])
            lst.sort()
print(lst)
