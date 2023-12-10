# a function to find the main loop and the number of steps to reach the furthest point
function find_path()
	# a function to find the start
	function find_start()
		for col = 1:length(grid[1]), row = 1:length(grid)
			grid[row][col] == 'S' && return (row,col)
		end
		return 1
	end
		
	# a function to do the first step
	function get_first_step(coord)
		# find the two possible directions we can start in
		coords = []
		grid[coord[1]-1][coord[2]] in "|F7" && push!(coords, [(coord[1]-1,coord[2]), 'u'])
		grid[coord[1]+1][coord[2]] in "|JL" && push!(coords, [(coord[1]+1,coord[2]), 'd'])
		grid[coord[1]][coord[2]-1] in "-LF" && push!(coords, [(coord[1],coord[2]-1), 'l'])
		grid[coord[1]][coord[2]+1] in "-J7" && push!(coords, [(coord[1],coord[2]+1), 'r'])	
		
		# find what pipe 'S' stands for
		(coords[1][2] == 'u' && coords[2][2] == 'd') && (return coords, '|')
		(coords[1][2] == 'u' && coords[2][2] == 'l') && (return coords, 'J')
		(coords[1][2] == 'u' && coords[2][2] == 'r') && (return coords, 'L')
		(coords[1][2] == 'd' && coords[2][2] == 'l') && (return coords, '7')
		(coords[1][2] == 'd' && coords[2][2] == 'r') && (return coords, 'F')
		(coords[1][2] == 'l' && coords[2][2] == 'r') && (return coords, '-')
		
		return 2
	end
	
	# a function to move one step down the pipe
	function move_around(c)
		row = c[1][1]
		col = c[1][2]
		p = grid[row][col]	# the pipe we are looking at
		d = c[2]		# the direction we are coming from
		
		# depending on the pipe we are at and the direction we are coming from, figure out where we are going and return the next coordinates and new direction
		if p == '|'
			d == 'u' ? (return (row-1, col), 'u') : (return (row+1, col), 'd') 
		elseif p == '-'
			d == 'l' ? (return (row, col-1), 'l') : (return (row, col+1), 'r')
		elseif p == 'L'
			d == 'd' ? (return (row, col+1), 'r') : (return (row-1, col), 'u')
		elseif p == 'J'
			d == 'd' ? (return (row, col-1), 'l') : (return (row-1, col), 'u')
		elseif p == 'F'
			d == 'u' ? (return (row, col+1), 'r') : (return (row+1, col), 'd')
		elseif p == '7'
			d == 'u' ? (return (row, col-1), 'l') : (return (row+1, col), 'd')
		else
			return 3
		end
	end

	loop_grid = [['.' for p in l] for l in grid]		# define a grid that only contains the pipes used in the main loop
	s = find_start()					# first find where the starting point is
	points, loop_grid[s[1]][s[2]] = get_first_step(s)	# get the first step in both possible directions
	step = 1						# count how many steps we have done
	
	while points[1][1] != points[2][1]					# loop across both directions until we reach the same point
		step += 1
		points = map(move_around, points)				# move one step along the pipes
		
		for p in points
			loop_grid[p[1][1]][p[1][2]] = grid[p[1][1]][p[1][2]]	# add the pipes used to the new grid
		end
	end
	
	return step, loop_grid	# return the steps and the new grid containing the pipes used
end

# a function to find the number of points enclosed by the main loop
function find_enclosed(loop_grid)
	enclosed = 0
	for col = 1:length(grid[1]), row = 1:length(grid)		# loop over the grid
		loop_grid[row][col] == '.' || continue			# if we are looking at a point that is on the main loop, skip it
		
		# count how many times we need to cross the main loop to reach an edge of the grid (here the top edge)
		# account for squeezing by allowing us to go through pipes that don't connect to the right hand side
		crossings = count(y -> loop_grid[y][col] in "-J7", 1:row-1)
		
		crossings % 2 != 0 && (enclosed += 1)	# if we had to cross an odd number of pipes then the point is enclosed
	end
	
	return enclosed	# return the number of enclosed points
end

const grid::Vector{String} = [line for line in eachline("10-data")]	# get the data
const step::Int64, loop_grid::Vector{Vector{Char}} = find_path()	# find the main loop and the number of steps needed to reach the furthest point
const enclosed::Int64 = find_enclosed(loop_grid)			# find the number of spots enclosed in the main loop

step |> println
enclosed |> println
