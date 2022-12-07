with open("7-data","r") as f:
	data = [line.strip().split(" ") for line in f.readlines()]
	
# define a path variable that contains the path, and a sizes dictionary which will contain all directories with their size
path = ""
sizes = {":/": 0}

# read all the commands
for line in data:
	if line[0] == "$":
		if line[1] == "cd":
			if line[2] == "..":				# if the command is "cd ..", move up one directory by deleting the last directory from the path
				path = path.rsplit(":",1)[0]		# remove everything after the last ":" in the path
			else:						# otherwise add the argument to the path, with folders separated by ":"
				path = path + ":" + line[2]
		elif line[1] == "ls":					# no need to do anything when reading the ls command, just read the output later
			continue
	elif line[0] == "dir" and not path + ":" + line[1] in sizes:	# if there is a directory that isn't already in sizes, add it to dirs and set its size to 0
		sizes[path + ":" + line[1]] = 0
	else:								# if we find a file, add its size to its parent directory, as well as all directories above
		parent_path = path
		while parent_path.count(":") > 0:
			sizes[parent_path] += int(line[0])
			parent_path = parent_path.rsplit(":",1)[0]
	
tot_size = 0
space_req = 3e7 - (7e7 - sizes[":/"])	# the space that needs to be cleared
min_size = 1e10				# the size of the smallest directory that can be deleted to clear enough space

for direc in sizes:
	size = sizes[direc]
	if size <= 1e5:					# if the size of a directory is less than 100000, add its size to the total (part 1)
		tot_size += size
	if size >= space_req and size <= min_size:	# if the directory is big enough to free enough space if deleted, and smaller than the previous smallest directory, update the size of the smallest directory to be deleted (part 2)
		min_size = size
		
print(tot_size)
print(min_size)
