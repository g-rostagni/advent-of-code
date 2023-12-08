# this solution makes a lot of assumptions on the input data, namely that ..Z location are only reached after full cycles, and that it is periodic with one ..A location being able to reach a single ..Z location, and that ..Z location being only able to map to itself
# either I'm incredibly lucky, or your data should fit these assumptions

# a function to get the data
function get_data(f)
	LR = Dict('L' => 1, 'R' => 2)
	
	# a function to apply a full cycle worth of instructions
	function full_cycle(loc,instr,nodes)
		for i in instr			# loop through the instructions
			loc = nodes[loc][LR[i]]	# apply every one of them
		end
		return loc			# return the final locations
	end

	data = [l for l in eachline(f)]	# read the file
	instr = data[1]			# read the instructions
	
	nodes_1step = Dict(map(data[3:end]) do l
		     	   x = eachmatch(r"\w{3}", l) |> collect
		    	   return x[1].match => [x[2].match, x[3].match]
		    	   end)										# create a dictionary containing every node
	nodes_1cycle = Dict([loc => full_cycle(loc,instr,nodes_1step) for loc in keys(nodes_1step)])	# create a dictionary containing every mapping from one location to the other after a full cycle

	return nodes_1cycle, length(instr)
end

# a function to generate a mapping that allows us to do n * n0 cycles at once
# nodes is a mapping that can do n0 cycles at once
function def_n_cycles(n,nodes)
	nodes_new = Dict([node => nodes[node] for node in keys(nodes)])				# define the new mapping as a copy of the old one
	for i in 1:n-1
		nodes_new = Dict([node => nodes[nodes_new[node]] for node in keys(nodes)])	# apply the old mapping n-1 times
	end
	return nodes_new									# return the new mapping
end

# a function to find the number of cycles required to transform all of the input locations into "..Z"
function get_all_z(locs,nodes)
	n = 0							# the number of cycles
	z = 1							# the number of ..Z we are looking for at this stage
	n_incr = 1						# how many cycles we are doing at once
	while count(i -> i[3] == 'Z', locs) != length(locs)	# while we haven't transformed all of the input
		n += n_incr					# do n_incr cycles at once
		
		locs = map(i -> nodes[i], locs)			# transform the locations
		
		if count(i -> i[3] == 'Z', locs) == z		# if one more location had reached "..Z"
			z += 1					# look for more "..Z" next time
			nodes = def_n_cycles(n/n_incr, nodes)	# generate a new mapping that allows us to do n cycles at once
			n_incr = n				# now we can do n steps at once
		end
	end
	return n						# return the number of steps
end

# get the data from the file
# nodes contains the mapping from one location to another after executing a full cycle of instructions
# n_instr is the number of steps in a cycle
const nodes::Dict{String,String}, n_instr::Int64 = get_data("8-data")

const locsA::Vector{String} = [loc for loc in keys(nodes) if loc[3] == 'A'] # get all the locations finishing in 'A'

get_all_z(["AAA"], nodes) * n_instr |> println	# get the number of steps required to go from AAA to ZZZ (this only works if AAA can only map to ZZZ and not ..Z)
get_all_z(locsA, nodes) * n_instr |> println	# get the number of steps required to go from all the locations ending in 'A' to the ones ending in 'Z'
