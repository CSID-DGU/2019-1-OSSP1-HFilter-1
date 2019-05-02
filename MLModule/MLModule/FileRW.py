#Copyright 2019. Jeongwon Her. All rights reserved.

# Write output file
def writeFileByList(path, listArray):
    """path:save path   listArray:nd array"""
    # Open output file
    output = open(path, 'w', encoding='utf8')
    # Error
    if output is None:
        print("Invalid path")
        return 1

    # Write
    for i in range(0, len(listArray)):
        for j in range(0, len(listArray[0])):
            output.write(str(listArray[i][j]) + " ")
        output.write("\n")

    output.close
    return 0
# End of writeFileByList

# Make output path
def makePathStr(path, addInfo="output.txt"):
    return path[:path.find('.')] + addInfo
# End of makePathStr