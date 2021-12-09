import re

f = open('7-data','r')

data = []

for line in f:
	l = line.strip('\n.').split(' contain ')
	data.append([l[0],l[1].split(', ')])

containers = {'shiny gold'}
adding =  True

while adding == True: #when you aren't doing anything, stop
	adding = False
	cont_temp = []
	for container in containers: #Loop over colors that can contain shiny gold
		for bags in data: #Loop over all bags
			bag_col = bags[0].replace('bags','') #Get color of bag
			if bag_col not in containers: #Exclude bags that were already added
				for contained_bags in bags[1]: #Loop over the colors that can be contained by $bags
					if container in contained_bags: #If $container can be contained by $bags
						cont_temp.append(bag_col) #Add bag color to containers
						adding = True #Say you have done something
	containers.update(cont_temp)
	print('')
	print('loop')
	print(containers)
	print('')
		
print('# of bags that contain shiny gold:',len(containers)-1) #exclude gold bag
print('# of bags total',len(data))