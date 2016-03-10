#Askhsh 8
with open("Tetris.txt") as textFile:
        lines = [line.split('\n') for line in textFile]
sq = []
rot = []
for i in range (8):
	sq.append([])
	sq[i] = list(lines[i][0])
for i in range (8):
	rot.append([])
	rot = zip(*sq[::-1])
	print ''.join(rot[i])
print ' '
for i in range (8):
	rot[i] = sq[7-i]
	print ''.join(rot[i])
print ' '
for i in range (8):
	sq = zip(*rot[::-1])
	print ''.join(sq[i])
print ' '
raw_input('Finish?')