# a function that find the number of cubes of a given color required to play the game
#	eachmatch()						->	finds every number of cubes of a given color used in the game
#	[parse() for m in collect()]	->	creates a vector containing each number converted into an Int64
#	return maximum()				->	returns the largest number in that vector
function GetColorN(game, color_pattern)
	return maximum([parse(Int64, m.match) for m in collect(eachmatch(color_pattern, game))])
end

# define some variables
tot1::Int64 = 0
tot2::Int64 = 0

for game in eachline("2-data")						# loop through each game of the data
	game_id = match(r"(?<=Game )\d+", game).match	# get the id of the game we are reading, using a regex lookbehind (cf my regex talk)
	
	# for each color, get the number of cubes required to play that game
	cubes_red = GetColorN(game, r"\d+(?= red)")
	cubes_green = GetColorN(game, r"\d+(?= green)")
	cubes_blue = GetColorN(game, r"\d+(?= blue)")	
	
	# if the required number of cubes is not greater than the amount of cubes available then add the game id to the total (part 1)
	if cubes_red <= 12 && cubes_green <= 13 && cubes_blue <= 14
		global tot1 += parse(Int64, game_id)
	end
	
	# add the product of the required number of cubes to the total (part 2)
	global tot2 += cubes_red * cubes_green * cubes_blue
end

println(tot1)
println(tot2)