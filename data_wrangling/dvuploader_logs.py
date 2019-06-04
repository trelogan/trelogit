# snipped this code from example here: https://www.computerhope.com/issues/ch001721.htm
# seems right but needs to first iterate through all the files to find which are .log files
# probably will have to do that with os. like :


errors = []                       # The list where we will store results.
linenum = 0                       # start at linenum zero
substr = "Error response when processing"          # Substring to search for.
with open ('C:/temp/DVUploaderLog__1557174528522.log', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if line.lower().find(substr) != -1:    # if case-insensitive match,
            errors.append("Line " + str(linenum) + ": " + line.rstrip('\n'))

for err in errors:
    print(err)
