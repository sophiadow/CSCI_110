# Week 10

# Problem 1

def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    text = infile.readlines()
    text.reverse()
    for everyline in text:
        outfile.write(everyline)
    infile.close()
    outfile.close()
    
