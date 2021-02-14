
# Logic to get difference between value
file1 = [x.strip() for x in open("D:/file1.txt","r").readlines()]
print(file1)
file2 = [x.strip() for x in open("D:/file2.txt","r").readlines()]
print(file2)
matches = open("D:/some_out.txt","w")
for x in file1:
    bool = False

    for y in file2:
        if x == y:
            bool = True
    if bool == False:
        print(x)
        matches.write(x +'\n')

for y in file2:
    bool = False

    for x in file1:
        if x == y:
            bool = True
    if bool == False:
        print(y)
        matches.write(y + '\n')
matches.close()


