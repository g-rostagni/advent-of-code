# a function to calculate the number of energised tiles
function beamin(c::Tuple{Int64,Int64,Int64})::Int64
	energised::Dict{Tuple{Int64,Int64},Vector{Int64}} = Dict()	# define a dictionary that will contain the lit tiles
	
	q = [c]			# generate a queue of points to look at next
	while length(q) > 0	# while the queue isn't empty
		y,x,d = q[1]	# start from the first point in the queue and get the coordinates and direction
		
		while 1 <= y <= length(grid) && 1 <= x <= length(grid[1])	# while we haven't reached the end of the grid
			d in get(energised, (y,x), 0) && break			# if we have already gone through this tile in this direction, break
			
			haskey(energised, (y,x)) || (energised[(y,x)] = [])	# otherwise add it to the list of locations we visited
			push!(energised[(y,x)], d)
			
			if grid[y][x] == '/'			# if we meet a mirror
				d = sl[d]			# update the direction
			elseif grid[y][x] == '\\'		
				d = bs[d]						
			elseif grid[y][x] == '-' && d % 2 == 0	# if we meet a splitter perpendicularly
				d = 1				# pick a direction
				push!(q, (y, x-1, 3))		# and add the other beam direction to the queue
			elseif grid[y][x] == '|' && d % 2 != 0
				d = 2
				push!(q, (y-1, x, 4))
			end
			
			y += dirs[d][1]	# move a step in the specified direction
			x += dirs[d][2]
		end
		q = q[2:end]	# remove the beam that we just completed from the queue
	end
	return length(energised)	# return the number of tiles energised
end

const dirs::Dict{Int64,Tuple{Int64,Int64}} = Dict(1 => (0,1), 2 => (1,0), 3 => (0,-1), 4 => (-1,0))	# a dictionary translating directions to y and x steps
const sl::Dict{Int64,Int64} = Dict(1 => 4, 2 => 3, 3 => 2, 4 => 1)					# a dictionary giving the reflections across a /
const bs::Dict{Int64,Int64} = Dict(1 => 2, 2 => 1, 3 => 4, 4 => 3)					# a dictionary giving the reflections across a \

const grid::Vector{String} = [line for line in eachline("16-data")]	# get the data

const edges::Vector{Tuple{Int64,Int64,Int64}} = [[(y, 1, 1) for y = 1:length(grid)] ; [(y, length(grid[1]), 3) for y = 1:length(grid)] ; [(1, x, 2) for x = 1:length(grid[1])] ; [(length(grid), x, 4) for x = 1:length(grid[1])]]	# generate a list of starting points for part 2

beamin((1,1,1)) |> println		# start from the corner (part 1)
maximum(beamin, edges) |> println	# try all the starting points and get the max number of lit tiles (part 2)
