fname = input("Enter the file name: ")
fl = open(fname)
count = 0
for line in fl:
    line = line.rstrip()
    if line.startswith('From '):
        count = count + 1
        listed = line.split()
        print(listed[1])
print("There were", count, "lines in the file with From as the first word")
