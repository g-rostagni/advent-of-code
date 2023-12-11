# a function to read the data and get the position of the galaxies and the empty lines
function get_gals(f)
	data = [line for line in eachline(f)]			# read the data

	no_gal = [Set(1:length(data)), Set(1:length(data[1]))]	# define an array containing all the empty row and column coordinates
	catalogue = []						# define a catalogue containing the coordinates of the galaxies
	for col = 1:length(data[1]), row = 1:length(data)	# loop over each point
		if data[row][col] == '#'			# if we find a galaxy
			push!(catalogue, [row, col])		# add it to the catalogue
			pop!(no_gal[1], row, 0)			# and remove its coordinates from the list of empty rows...
			pop!(no_gal[2], col, 0)			# ...and columns
		end
	end
	return catalogue, no_gal				# return the galaxies and the empty lines
end

# a function to get the distance between all the galaxies while accounting for expansion, with H0 the expansion factor
function get_dist(H0)
	dist = 0									# define the distance
	for g = 1:length(catalogue)-1, g2 = g+1:length(catalogue)			# loop over all pairs of galaxies
		for i = 1:2								# loop over the x and y coordinates
			c1 = min(catalogue[g][i], catalogue[g2][i])
			c2 = max(catalogue[g][i], catalogue[g2][i])
			dist += c2 - c1 + (H0-1) * count(j -> (c1 < j < c2), no_gal[i]) # add the difference in positions to the distance, as well as additional space for each empty row/col travelled across
		end
	end
	return dist									# return the distance
end

# get the position of the galaxies and the empty lines
const catalogue::Vector{Vector{Int64}}, no_gal::Vector{Set{Int64}} = get_gals("11-data")

# get the distances for an expansion factor of 2 (part 1) and 1 million (part 2)
get_dist(2) |> println
get_dist(1000000) |> println
