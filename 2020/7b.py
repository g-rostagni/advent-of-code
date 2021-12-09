f = open('7-data','r')

data = []

for line in f:
	l = line.strip('\n.').split(' contain ')
	data.append([l[0],l[1].split(', ')])

nums = [['1']]
colors = ['shiny gold']

adding = True
tot = 0

while adding == True: #Stop when you don't do stuff
	adding = False
	nums_new = []
	colors_new = []
	for i in range(len(nums)): #Loop over colors
		if colors[i] == 'no other bags':
				nums_temp = nums[i].copy()
				# nums_temp.append('0')
				nums_new.append(nums_temp)
				colors_new.append('no other bags')
		else:
			for bags in data: 	#Loop over all bags
				if colors[i] in bags[0]:	#If the bag is in the list of colors
					for bag in bags[1]:	#loop over bags contained by the color
						nums_temp = nums[i].copy()
						if bag.startswith('no'):
							nums_temp.append('0')
							nums_new.append(nums_temp)
							colors_new.append(bag)
						else:
							nums_temp.append(bag[0])
							nums_new.append(nums_temp)
							colors_new.append(bag[2:])
							adding = True
	colors = colors_new.copy()
	nums = nums_new.copy()
	for n in nums:
		n_tmp = 1
		for i in n:
			n_tmp *= int(i)
		tot += n_tmp

print(tot)