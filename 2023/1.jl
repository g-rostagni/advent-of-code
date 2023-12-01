# I must have missed something because there's no way a day 1 would be such a pain

# a function to convert words to digits
function convert_num(s)
	# if the number is a digit just return it
	if length(s) == 1
		return s
	else
		# otherwise just compare until you find the correct word and return the corresponding digit
		if s == "one"
			return "1"
		elseif s == "two"
			return "2"
		elseif s == "three"
			return "3"
		elseif s == "four"
			return "4"
		elseif s == "five"
			return "5"
		elseif s == "six"
			return "6"
		elseif s == "seven"
			return "7"
		elseif s == "eight"
			return "8"
		elseif s == "nine"
			return "9"
		else
			return "nah"
		end
	end
end

# a function that looks for instances of digits in a string
function find_nums(s,patt)
	nums = eachmatch(patt, s, overlap = true)	# create an object with all the matches
	n1 = String(collect(nums)[1].match)		# horrible syntax to retrieve the first match
	n2 = String(collect(nums)[end].match)		# horrible syntax to retrieve the last match
	return convert_num(n1), convert_num(n2)		# return the numbers converted to digits
end

# some variables
tot1 = 0
tot2 = 0

# define two matching patterns, one that looks for digits (part 1), the other looks for digits and words (part 2)
digits1 = r"[1-9]"
digits2 = r"[1-9]|one|two|three|four|five|six|seven|eight|nine"

for line in eachline("1-data")			# read the file line by line
	a,b = find_nums(line,digits1)		# get the first and last digits in the string (part 1), as strings
	global tot1 += parse(Int64, a*b)	# concatenate the two digits, convert to Int and add it to the total
	
	# same but for part 2
	a,b = find_nums(line,digits2)
	global tot2 += parse(Int64, a*b)
end

println(tot1)
println(tot2)
