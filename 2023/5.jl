# a function to transform a seed interval according to a set of mappings
function transform_seeds(seeds,maps)
	i_seed = 1		# define an iterator over the seed intervals
	i_map = 1		# define an iterator over the mappings
	ind = seeds[1][1]	# define an index telling us where we are in the seeds
	
	new_seeds = []
	while true
		if i_map > length(maps)					# if we have reached the end of the mappings
			push!(new_seeds, [ind, seeds[i_seed][2]])	# map the rest of the seeds in the interval to identity
			ind = seeds[i_seed][2]+1			# move the index to the end of the seed interval
			
		elseif ind > maps[i_map][2] 	# if we are past the end of the current mapping
			i_map += 1		# move on to the next one
			continue
		
		elseif maps[i_map][1] <= ind							# if we are inside the valid range of a mapping
			i_end = min(seeds[i_seed][2], maps[i_map][2])				# transform the seed until the end of the seed interval or the end of the mapping
			push!(new_seeds, [ind + maps[i_map][3], i_end + maps[i_map][3]])	# transform the seed interval according to the mapping
			ind = i_end+1								# move the index to the end of the transformed interval
			
		else							# if we are before the valid range of a mapping
			i_end = min(seeds[i_seed][2], maps[i_map][1]-1) # transform the seed until the end of the seed interval or the start of the next mapping
			push!(new_seeds, [ind, i_end])			# map the rest of the interval to identity
			ind = i_end+1					# move the index to the end of the transformed interval
		end
		
		if ind > seeds[i_seed][2]		# if the index has reached the end of the current seed interval
			i_seed += 1			# move on to the next one
			i_seed > length(seeds) && break	# when we have reached the end of the last seed interval, break the loop
			i_map = 1			# reset back to the first mapping
			ind = seeds[i_seed][1]		# reset the index back to the start of the next seed interval
		end
	end
	return new_seeds	# return the transformed list of seed intervals
end

# a function to read and parse the data from a file	
function read_data(f)
	data = split(read(f, String), "\n\n")				# separate the paragraphs

	seeds = [parse(Int64, n) for n in split(data[1])[2:end]]	# read the seeds from the first paragraph
	
	# read the steps from the other paragraphs, and parse them suitably
	allsteps = []
	for line in data[2:end]						# loop over each of the other paragraphs
		maps = []
		for l in split(line, "\n")[2:end]			# loop over each line in a paragraph (except the first)
			length(l) == 0 && continue			# if the line is empty, move on
			m = [parse(Int64, n) for n in split(l)]		# read a mapping in the format [output, input, length]
			
			# convert to the format [first_input, last_input, offset] (inclusive)
			# where offset is the difference from input to output applied by the mapping
			push!(maps, [m[2], m[2]+m[3]-1, m[1]-m[2]])	
		end
		push!(allsteps,sort(maps, by = i->i[1]))		# sort the mappings by lowest to highest input and add them to the rest 
	end
	return seeds,allsteps
end

# a function to parse seeds suitably for part 1 or part 2
# seeds are formatted as several intervals [first_seed, last_seed] (inclusive)
function parse_seeds(p,seeds)
	if p == 1
		return [[seed,seed] for seed in seeds]					# intervals of length 1 for part 1
	else
		return [[seeds[i], seeds[i]+seeds[i+1]-1] for i in 1:2:length(seeds)]	# intervals of the proper length for part 2
	end
end

# a function to find the minimum location for a set of seeds and mappings
function get_min(p,seeds,allsteps)
	s = parse_seeds(p,seeds)		# get the seeds from part 1 or part 2 in the right format 
	
	for maps in allsteps			# loop over all the steps
		s = transform_seeds(s,maps)	# transform the seeds into new values according to each mapping step until we get to the location
	end
	
	return minimum(s)[1]			# return the minimum location found
end

# main function
function main()
	seeds,allsteps = read_data("5-data")	# read the data

	println(get_min(1,seeds,allsteps))	# get the minimum loc for part 1
	println(get_min(2,seeds,allsteps))	# get the minimum loc for part 2
end

main()
