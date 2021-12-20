def import_data(filename):
	f = open(filename,'r')
	algo = f.readline().strip()
	data = [[i for i in line.strip()] for line in f]
	return algo,data[1:]
		
def neighbours(y,x):
	nb = []
	for i in range(y-1,y+2):
		for j in range(x-1,x+2):
			nb.append([i,j])
	return nb
	
def read_pixel(y,x,image,algo):
	num = ''
	for nb in neighbours(y,x):
		if not 0 <= nb[0] < len(image) or not 0 <= nb[1] < len(image[0]):
			num += '0'
			continue
		px = image[nb[0]][nb[1]]
		if px == '#':
			num += '1'
		else:
			num += '0'
	numdec = int(num,2)
	return algo[numdec]
	
def generate_new_new_image(image,algo):
	image_big = [['.' for j in range(len(image[0])+6)] for i in range(len(image)+6)]
	for y in range(len(image)):
		for x in range(len(image[0])):
			image_big[y+3][x+3] = image[y][x]
			
	newimage = [['.' for j in range(len(image_big[0]))] for i in range(len(image_big))]
	for y in range(len(newimage)):
		for x in range(len(newimage[0])):
			newimage[y][x] = read_pixel(y,x,image_big,algo)
			
	newnewimage = [['.' for j in range(len(image_big[0]))] for i in range(len(image_big))]
	for y in range(len(newnewimage)):
		for x in range(len(newnewimage[0])):
			newnewimage[y][x] = read_pixel(y,x,newimage,algo)
	nni = [[px for px in line[1:len(line)-1]] for line in newnewimage[1:len(newnewimage)-1]]
	return nni


algo,image = import_data('20-data')

steps = 50
for i in range(int(steps/2)):
	image = generate_new_new_image(image,algo)

nlit = 0
for line in image:
	for px in line:
		if px =='#':
			nlit += 1
print(nlit)
