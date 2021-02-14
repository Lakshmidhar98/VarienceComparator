#
# # Logic to get difference between value
# file1 = [x.strip() for x in open("D:/file1.txt","r").readlines()]
# print(file1)
# file2 = [x.strip() for x in open("D:/file2.txt","r").readlines()]
# print(file2)
# matches = open("D:/some_out.txt","w")
# for x in file1:
#     bool = False
#
#     for y in file2:
#         if x == y:
#             bool = True
#     if bool == False:
#         print(x)
#         matches.write(x +'\n')
#
# for y in file2:
#     bool = False
#
#     for x in file1:
#         if x == y:
#             bool = True
#     if bool == False:
#         print(y)
#         matches.write(y + '\n')
# matches.close()


def getDifferenceFrom(file1, file2, diffpath):
    print(file1)
    print(file2)



    data1 = [x.strip() for x in open(file1,"r").readlines()]
    data2 = [x.strip() for x in open(file2,"r").readlines()]
    output_file = open(diffpath,"w")
    print(data1)
    print(data2)



    for x in data1:
        bool = True
        for y in data2:
          #  print(x,'=>',y)
            if x == y:
                bool = False
        if bool == True:
            print(x)
            output_file.write(x + '\n')

    for x in data2:
        bool = True
        for y in data1:
           # print(x,'=>',y)
            if x == y:
                bool = False
        if bool == True:
            print(x)
            output_file.write(x + '\n')

















getDifferenceFrom('D:/file1.txt','D:/file2.txt','D:/some_out.txt')










