# a function to search through the data and return an array containing all instances of a specific pattern
function find_things(patt)
	return [collect(eachmatch(patt, line)) for line in eachline("3-data")]
end

# a function that returns a safe y range to iterate through
function yrange(col)
	return max(1,col-1) : min(ymax,col+1)
end

# a function that checks whether a given number has a symbol adjacent to it
# col: the line where we found the number
# ind: the index of the start of the number in that line
# len: the length of the number
function check_sym(col, ind, len, syms)
	for y in yrange(col)						# loop through the lines adjacent to the current one
		for sym in syms[y]						# loop through all the symbols found in a given line
			if ind - 1 <= sym.offset <= ind+len	# if the symbol is adjacent
				return true						# return true
			end
		end
	end	
	return false								# otherwise return false
end

# a function to determine the gear ratio of a specific gear
function gear_ratio(col, ind, nums)
	n = 0
	ratio = 1
	for y in yrange(col)												# loop through the lines adjacent to the current one
		for num in nums[y]												# loop through all the numbers in that line
			if num.offset - 1 <= ind <= num.offset + length(num.match)	# if one number is adjacent to the gear
				n += 1													# add one to the number of adjacent numbers
				ratio *= parse(Int64, num.match)						# multiply the gear ratio by the adjacent number
			end
		end
	end
	if n == 2															# if the gear has two adjacent numbers
		return ratio													# return the ratio
	else
		return 0														# otherwise return 0
	end
end


# define some variables
tot1::Int64 = 0
tot2::Int64 = 0

# create arrays with the position and value of each number, symbol, and gears in the data
const nums = find_things(r"\d+")
const syms = find_things(r"[^\d\.]")
const gears = find_things(r"\*")

# define how many lines we have to go through
const ymax = length(nums)

for col in 1:ymax												# loop through all the lines			
	for num in nums[col]										# for a given line, loop through all the numbers we found in that line
		if check_sym(col, num.offset, length(num.match), syms)	# check if that number has an adjacent symbol
			global tot1 += parse(Int64, num.match)				# if it does, add it to the total for part 1
		end
	end

	for gear in gears[col]										# for a given line, loop through all the gears we found in that line
		global tot2 += gear_ratio(col, gear.offset, nums)		# add the gear ratio to the total for part 2
	end
end

println(tot1)
println(tot2)