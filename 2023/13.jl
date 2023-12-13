# a function to get the data
function get_data(fn)
	f = read(fn, String)
	return [[l for l in eachsplit(strip(b), "\n")] for b in eachsplit(f, "\n\n")]
end

# a function to get the transpose of a mirror
function transpose(g)
	return [[l[i] for l in g] for i = 1:length(g[1])]
end

# a function to find the axis of horizontal symmetry of a mirror (if any)
function find_sym(g,part)
	for row = 1:length(g)-1			# loop over pairs of rows
		gap = 0				# define the gap between the two rows we are looking at
		sym = true			# whether the mirror is symmetric
		canswap = Int(part == 2)	# how many smudges we are allowed to fix (0 for part 1)
		
		while row-gap >= 1 && row+1+gap <= length(g)	# loop until we reach the end of a mirror
			ndiff = count(i -> i[1] != i[2], zip(g[row-gap], g[row+gap+1]))	# find out how many difference there are between the two rows		
			if ndiff > canswap 						# if more chars differ than we are allowed to swap
				sym = false						# symmetry is broken
				break							# move on to the next pair of rows	
			elseif ndiff == 1						# if 1 char differs and we can swap a char
				canswap = 0						# remember that we can't swap another smudge
			end
			gap += 1							# move out one step in each direction		
		end
			
		(sym && canswap == 0) && return row	# if the line is symmetric and we don't have a swap still to do, return the location of the axis of symmetry
	end
	return 0	# if there is no symmetry in the mirror return 0
end	

const grids::Vector{Vector{String}} = get_data("13-data")	# get the data

# do part 1 and 2
for p = 1:2
	# for each part, get the score of each mirror and sum it
	# we look for horizontal symmetry directly, and for vertical symmetry by considering the transpose of the mirror
	map(g -> 100*find_sym(g,p) + find_sym(transpose(g),p), grids) |> sum |> println
end
