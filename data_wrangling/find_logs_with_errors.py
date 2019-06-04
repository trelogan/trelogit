# from this example:   https://stackoverflow.com/questions/27981835/searching-multiple-text-files-for-two-strings
from os import listdir

errors = []                       # The list where we will store results.
linenum = 0                       # start at linenum zero

with open("C:/temp/DVUploaderLog__1557157841872.log", 'rt') as f:           #putting open() in a with statement is good practice, helps avoid leaks
    for filename in listdir("C:/temp/"):
        if filename.endswith(".log"):
            with open('C:/temp/' + filename) as currentFile:
                text = currentFile.read()                                   #this puts the contents of each file in a variable
                for line in text:
                    linenum += 1
                    if ('Error response when processing' in text):                     #search through the contents of each file
                        #print('There was an error found in  ' + filename[:-4] + '\n')
                        errors.append("Line " + str(linenum) + ": " + line.rstrip('\n'))

for err in errors:
    print(err)




            # else:
            #     f.write('NOT ' + filename[:-4] + '\n')
