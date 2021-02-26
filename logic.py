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

import os

def getDifferenceFrom(file1, file2):
   # print(file1)
    #print(file2)

    if ((os.path.exists(file1)) == False) & ((os.path.exists(file2)) == False):
       print('Files are not available at' + file1, file2)
       return None

    if (os.path.exists(file1)) == False:
        print('File1 is not available at '+file1)
        return None

    if (os.path.exists(file2)) == False:
        print('File2 is not available at ' + file2)
        return None

    data1 = [x.strip() for x in open(file1,"r").readlines()]
    data2 = [x.strip() for x in open(file2,"r").readlines()]
    diff_file = open("D:/some_out.txt", "w+")
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
            diff_file.write(x + '\n')
            return diff_file

    for x in data2:
        bool = True
        for y in data1:
            if x == y:
                bool = False
        if bool == True:
            print(x)
            diff_file.write(x + '\n')
            return diff_file




diffFile = getDifferenceFrom('D:/file1.txt','D:/file2.txt')

