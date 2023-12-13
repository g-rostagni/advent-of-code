# a function to get the transpose of a mirror
function transpose(g)
	return [[l[i] for l in g] for i = 1:length(g[1])]
end

# a function to get the data
function get_data(f)
	data = []
	grid = []
	for line in eachline(f)
		if line == ""
			push!(data, grid)
			grid = []
		else
			push!(grid, [l for l in line])
		end	
	end
	push!(data, grid)
	return data
end
# a function to find the difference between two rows
function find_diff(r1,r2)
	n = 0					
	x = 0					
	for i in 1:length(r1)			# loop over the whole line
		if r1[i] != r2[i]		# if two points are different
			x = i			# write down their position
			n += 1			# and add 1 to the number of characters that differ
		end
	end

	# if more than 1 char differ:	the row can't be fixed, return -1
	# if zero char differ:		there is nothing to fix, return 0
	# if exactly 1 char differs:	return its position
	n > 1 ? (return -1) : (return x)
end

# a function to find the axis of horizontal symmetry of a mirror (if any)
function find_sym(g,part)
	for row = 1:length(g)-1					# loop over pairs of rows
		gap = 0						# define the gap between the two rows we are looking at
		sym = true					# whether the mirror is symmetric
		part == 1 ? canswap = false : canswap = true	# whether we are allowed to swap a single character (false for part 1)
		s = [0,0]					# the position of the smudge that we swapped
		
		while row-gap >= 1 && row+1+gap <= length(g)			# loop until we reach the end of a mirror
			xdiff = find_diff(g[row-gap], g[row+gap+1])		# find where the two rows we are looking out differ
			if xdiff == -1 || (xdiff > 0 && !canswap)		# if more than one char differ, or 1 char differs but we are not allowed to swap
				sym = false					# symmetry is broken
				break						# move on to the next pair of rows
				
			elseif xdiff > 0					# if 1 char differs and we can swap a char
				s = [row-gap, xdiff]				# write down the position of the smudge
				g[row-gap][xdiff] = dic[g[row-gap][xdiff]]	# fix the smudge
				canswap = false					# remember that we can't swap another smudge
			end
			gap += 1						# move out one step in each direction		
		end
			
		(sym && !canswap) && return row				# if the line is symmetric and we don't have a swap still to do, return the location of the axis of symmetry
		(s[1] != 0) && (g[s[1]][s[2]] = dic[g[s[1]][s[2]]])	# if we have corrected a smudge, reset it before moving on
	end
	return 0	# if there is no symmetry in the mirror return 0
end	

const dic::Dict{Char,Char} = Dict('.' => '#', '#' => '.')	# define a dictionary to swap the smudges
const grids::Vector{Vector{Vector{Char}}} = get_data("13-data")	# get the data

# do part 1 and 2
for p = 1:2
	# for each part, get the score of each mirror and sum it
	# we look for horizontal symmetry directly, and for vertical symmetry by considering the transpose of the mirror
	map(g -> 100*find_sym(g,p) + find_sym(transpose(g),p), grids) |> sum |> println
end
