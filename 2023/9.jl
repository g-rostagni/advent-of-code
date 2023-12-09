# a function that returns the extra first and last numbers for a given line
function recurs(line)
	if count(i -> i == 0, line) != length(line)					# if the line isn't all 0s
		n_0, n_last = [line[i] - line[i-1] for i in 2:length(line)] |> recurs	# calculate the reduced line and send it into the recursive function
		return line[1] - n_0, line[end] + n_last				# returns the new first and last number for that line
	else
		return 0,0								# when we reach the bottom, it's just 0s
	end
end

# define some variables
tot1::Int64 = 0
tot2::Int64 = 0

for line in eachline("9-data")						# read the input
	n_0, n_last = map(i -> parse(Int64, i), split(line)) |> recurs	# send each line into the recursive function that creates the extra first and last number
	global tot1 += n_last						# add the last number to the part 1 total
	global tot2 += n_0						# add the first number to the part 2 total
end

tot1 |> println
tot2 |> println
