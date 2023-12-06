# a function to import the race data
function get_races(ind)
	data = readlines("6-data")[ind]				# read the line we care about
	races = [parse(Int64, x) for x in split(data)[2:end]]	# shove the data into an array
	return races						# return the array
end

# a function to get how many ways to win a race there are
function get_wins(t,d)
	# literally just solve the problem
	tmin = (t - sqrt(t^2 - 4*d))/2
	tmax = (t + sqrt(t^2 - 4*d))/2
	return floor(tmax) - ceil(tmin) + 1
end

# a function to concatenate an array of numbers into a single number
function conc(int_array)
	s = ""
	for i in 1:length(int_array)		# loop over all races
		s *= string(int_array[i])	# add the numbers converted to string to the end of the string s
	end
	return parse(Int64,s)			# convert s to a number and return it
end

# main function
function main()
	# import the times and distances of each race
	times::Vector{Int64} = get_races(1)
	dist::Vector{Int64} = get_races(2)

	wins::Int64 = 1

	for race in 1:length(times)				# loop over the races
		wins *= get_wins(times[race], dist[race])	# multiply the total by the number of ways to win that race
	end

	# get the number of ways to win the long race (part 2)
	# conc(x) concatenates the times and distances to generate the long race
	wins2::Int64 = get_wins(conc(times), conc(dist))

	println(wins)
	println(wins2)
end
	
main()
