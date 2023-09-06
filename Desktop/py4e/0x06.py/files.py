fhand = open('mbox-short.txt')
print(fhand)

for line in fhand:
    ly = line.rstrip()
    print (ly.upper())