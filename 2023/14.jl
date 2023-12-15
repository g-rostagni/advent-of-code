# a function to tilt the grid in any direction
function tilt(dir::Int64)
	# a function to return a range or reversed range based on the direction
	function rev_range(d,i0,iend)
		d == -1 ? (return iend:-1:i0) : (return i0:iend)
	end
	
	dy, dx = dirs[dir]											# define y and x increments based on the direction
	for y = rev_range(dy,1,length(grid)), x = rev_range(dx,1,length(grid[1]))				# loop over the grid, starting from whichever direction is the "lowest"
		grid[y][x] != 'O' && continue									# if we are not looking at a round rock, move on
		
		iy, ix = (dy, dx)										# define the y and x displacements
		while 1 <= y-iy <= length(grid) && 1 <= x-ix <= length(grid[1]) && grid[y-iy][x-ix] == '.'	# while we haven't reached an edge or a #
			grid[y-iy][x-ix] = 'O'									# move the rock by one spot
			grid[y-iy+dy][x-ix+dx] = '.'								# reset the previous spot
			ix += dx										# increment the displacements
			iy += dy
		end
	end
	return 0
end

# a function to perform many cycles making use of repeating patterns
function many_cyc(cmax::Int64)
	scores::Dict{Int128,Int64} = Dict()				# a dictionary containing hashes and the corresponding scores 
	s = 0								# the current score
	
	p = false							# whether we are looking at a pattern
	patt = [0,0]							# an array containing the start and length of the current pattern
	
	c = 1								# the cycle we are on
	while c <= cmax							# while we haven't completed all cycles
		map(tilt, 1:4)						# do a cycle
		s = get_score()						# get the current score
		k = hash(grid)						# get a hash corresponding to the current grid
	
		if p							# if we are looking at a pattern
			if !haskey(scores, k)				# if we see a new hash
				p = false				# the pattern is broken
			elseif scores[k] == patt[1]			# if we cycled back to the first value of the pattern
				c = div(cmax-c, patt[2]) * patt[2] + c	# the pattern is completed and we can jump many iterations until we have less than 1 full pattern left to do
			elseif scores[k] == patt[1] + patt[2]		# if the next value matches the second value of the pattern
				patt[2] += 1				# increase the length of the pattern by one
			else						# otherwise
				p = false				# the pattern is broken
			end
		end
	
		if !p							# if we are not currently looking at a pattern
			if haskey(scores, k)				# if we find a value that has repeated before
				p = true				# we start searching for a pattern
				patt = [scores[k], 1]			# write down the location of the pattern start
			else						# otherwise
				scores[k] = c				# add the current score to the dictionary of scores
			end

		end
		c += 1							# increment cycles
	end
	return 0
end

# a function to get the score
function get_score()::Int64
	sum(y -> count(==('O'), grid[y]) * (length(grid) - y + 1), 1:length(grid)) # mutliply the number of rocks in a row by the row's reverse position
end

const dirs::Dict{Int64,Tuple{Int64,Int64}} = Dict(1 => (1,0), 2 => (0,1), 3 => (-1,0), 4 => (0,-1))	# define the directions NWSE respectively
grid::Vector{Vector{Char}} = [[c for c in l] for l in readlines("14-data")]				# get the data

tilt(1)			# tilt the grid to the north
get_score() |> println	# read the corresponding score (part 1)
many_cyc(Int(1e9))	# do 1e9 cycles			
get_score() |> println	# read the final score (part 2)			
